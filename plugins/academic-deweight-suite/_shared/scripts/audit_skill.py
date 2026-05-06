#!/usr/bin/env python3
"""
技能目录轻量审计器（Lightweight auditor for a skill folder）。

检查项（Checks）:
- SKILL.md 存在且 frontmatter 合法
- frontmatter 仅包含 name/description
- description 含有明确触发表达
- 无占位符泄漏（TODO/TBD/template 标记）
- SKILL.md 资源声明完整（声明存在）
- 资源目录无孤儿文件（存在但未在 SKILL.md 声明）
- 全目录无悬空路径引用（scripts/references/assets 路径指向不存在文件）
- 可选结构卫生检查（额外噪音文档）
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None


MAJOR_DOC_NOISE = {
    "README.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
    "CHANGELOG.md",
}

PLACEHOLDER_PATTERNS = [
    r"\[TODO[^\]]*\]",
    r"\[TBD[^\]]*\]",
    r"\bTODO:\b",
    r"\bTBD:\b",
    r"Replace with",
    r"请替换为",
]

TRIGGER_HINTS_EN = [
    "use when",
    "used when",
    "when ",
    "trigger",
    "used for",
    "especially",
]

TRIGGER_HINTS_ZH = [
    "使用时",
    "用于",
    "适用于",
    "当",
    "触发",
]

RESOURCE_DIRS = ("scripts", "references", "assets")
# 仅匹配相对路径形式，避免将绝对路径中的 ".../scripts/xxx" 误判为本 skill 资源。
RESOURCE_REF_RE = re.compile(r"(?<!/)\b((?:scripts|references|assets)/[A-Za-z0-9._/-]+)")
TEXT_SUFFIXES = {".md", ".markdown", ".yaml", ".yml", ".py", ".json", ".txt"}


def load_frontmatter(skill_md: Path):
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text, "文件开头缺少 YAML frontmatter 分隔符（Missing YAML frontmatter delimiter at file start）."

    marker = "\n---\n"
    idx = text.find(marker, 4)
    if idx == -1:
        return None, text, "YAML frontmatter 结束分隔符不合法（Invalid YAML frontmatter closing delimiter）."

    raw = text[4:idx]
    body = text[idx + len(marker) :]

    if yaml is None:
        return None, text, "缺少 PyYAML，无法解析 frontmatter（PyYAML is not available; cannot parse frontmatter）."

    try:
        data = yaml.safe_load(raw)
    except Exception as exc:  # pragma: no cover
        return None, text, f"frontmatter YAML 非法（Invalid frontmatter YAML）: {exc}"

    if not isinstance(data, dict):
        return None, text, "frontmatter 必须是 YAML 映射（Frontmatter must be a YAML mapping）."

    return data, body, None


def has_trigger_language(description: str) -> bool:
    desc_en = description.lower()
    if any(h in desc_en for h in TRIGGER_HINTS_EN):
        return True

    if any(h in description for h in TRIGGER_HINTS_ZH):
        return True

    return False


def iter_skill_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part.startswith(".") for part in rel.parts):
            continue
        if "__pycache__" in rel.parts:
            continue
        if path.suffix.lower() == ".pyc":
            continue
        yield path


def extract_resource_refs(text: str) -> set[str]:
    refs: set[str] = set()
    for match in RESOURCE_REF_RE.finditer(text):
        ref = match.group(1).rstrip("/")
        if not ref:
            continue
        parts = ref.split("/")
        if len(parts) < 2:
            continue
        filename = parts[-1]
        # 目录级引用用于说明，不纳入“文件存在性”审计。
        if "." not in filename:
            continue
        refs.add(ref)
    return refs


def collect_resource_files(skill_dir: Path) -> set[str]:
    files: set[str] = set()
    for folder in RESOURCE_DIRS:
        base = skill_dir / folder
        if not base.exists():
            continue
        for path in iter_skill_files(base):
            files.add(path.relative_to(skill_dir).as_posix())
    return files


def scan_text_refs(skill_dir: Path) -> dict[str, list[str]]:
    ref_to_files: dict[str, list[str]] = defaultdict(list)
    for path in iter_skill_files(skill_dir):
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        refs = extract_resource_refs(text)
        rel_file = path.relative_to(skill_dir).as_posix()
        for ref in refs:
            ref_to_files[ref].append(rel_file)
    return ref_to_files


def main() -> int:
    parser = argparse.ArgumentParser(description="审计一个 skill 目录（Audit a skill folder）")
    parser.add_argument(
        "skill_dir",
        type=Path,
        help="目标 skill 目录路径（Path to target skill directory）",
    )
    args = parser.parse_args()

    skill_dir = args.skill_dir.resolve()
    majors: list[str] = []
    warns: list[str] = []

    if not skill_dir.exists() or not skill_dir.is_dir():
        print(f"FAIL: 找不到 skill 目录（skill directory not found）: {skill_dir}")
        return 1

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        print("FAIL: 缺少 SKILL.md（missing SKILL.md）")
        return 1

    frontmatter, body, fm_err = load_frontmatter(skill_md)
    raw_text = skill_md.read_text(encoding="utf-8")

    if fm_err:
        majors.append(fm_err)
    else:
        keys = set(frontmatter.keys())
        required = {"name", "description"}
        if keys != required:
            majors.append(
                "frontmatter 只能包含 name 与 description "
                f"（Frontmatter must contain only name and description; found: {sorted(keys)}）."
            )

        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")

        if not isinstance(name, str) or not name.strip():
            majors.append("frontmatter 的 name 缺失或为空（Frontmatter name is missing or empty）.")
        if not isinstance(description, str) or len(description.strip()) < 24:
            majors.append(
                "frontmatter 的 description 缺失或过短（Frontmatter description is missing or too short）."
            )
        elif not has_trigger_language(description):
            majors.append(
                "frontmatter 的 description 必须包含明确触发表达 "
                "（Frontmatter description must include explicit trigger phrasing, "
                "for example: 'Use when ...' or '用于...'）."
            )

    for pat in PLACEHOLDER_PATTERNS:
        if re.search(pat, raw_text, flags=re.IGNORECASE):
            majors.append(f"检测到占位符标记（Placeholder marker detected）: pattern '{pat}'")

    skill_declared_refs = extract_resource_refs(raw_text)
    existing_resources = collect_resource_files(skill_dir)

    missing_declared = sorted(ref for ref in skill_declared_refs if not (skill_dir / ref).exists())
    for ref in missing_declared:
        majors.append(f"SKILL.md 声明了不存在的资源（Missing declared resource）: {ref}")

    orphan_resources = sorted(res for res in existing_resources if res not in skill_declared_refs)
    for res in orphan_resources:
        majors.append(f"存在未在 SKILL.md 声明的资源（Orphan resource）: {res}")

    ref_hits = scan_text_refs(skill_dir)
    for ref, files in sorted(ref_hits.items()):
        if (skill_dir / ref).exists():
            continue
        sample = ", ".join(sorted(files)[:3])
        extra_count = max(0, len(files) - 3)
        extra_suffix = f" ... +{extra_count}" if extra_count else ""
        majors.append(
            "检测到悬空路径引用（Dangling resource reference）: "
            f"{ref} <- {sample}{extra_suffix}"
        )

    line_count = raw_text.count("\n") + 1
    if line_count > 500:
        warns.append(
            f"SKILL.md 偏长（{line_count} 行），建议将细节拆到 references/ "
            "(SKILL.md is long; consider splitting details into references/)."
        )

    for bad in sorted(MAJOR_DOC_NOISE):
        if (skill_dir / bad).exists():
            warns.append(f"发现非必要文档（Non-essential document present）: {bad}")

    if not (skill_dir / "agents" / "openai.yaml").exists():
        warns.append("缺少 agents/openai.yaml（agents/openai.yaml is missing）.")

    status = "PASS" if not majors else "FAIL"
    print(f"{status}: {skill_dir}")

    if majors:
        print("\n重大问题（Major issues）:")
        for item in majors:
            print(f"- {item}")

    if warns:
        print("\n警告（Warnings）:")
        for item in warns:
            print(f"- {item}")

    return 0 if not majors else 1


if __name__ == "__main__":
    sys.exit(main())
