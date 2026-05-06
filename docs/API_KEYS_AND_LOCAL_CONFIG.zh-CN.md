# API Key 与本地配置

本插件不附带维护者自己的 API key。

如果你的 agent runtime 或论文转换流程需要外部 provider，请在本地配置自己的 key，不要提交密钥。

参考：

```text
examples/local-config.example.txt
```

把需要的值复制到你的私有 runtime config。

不要提交：

```text
.env
.env.local
.env.production
*.sqlite
*.sqlite3
```
