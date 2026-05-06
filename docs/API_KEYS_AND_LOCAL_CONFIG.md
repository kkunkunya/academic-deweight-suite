# API Keys And Local Config

This plugin does not ship maintainer-owned API keys.

If your agent runtime or paper conversion workflow needs external providers, configure your own keys locally. Do not commit secrets.

Use:

```text
examples/local-config.example.txt
```

Copy the relevant values into your private runtime config.

Never commit:

```text
.env
.env.local
.env.production
*.sqlite
*.sqlite3
```
