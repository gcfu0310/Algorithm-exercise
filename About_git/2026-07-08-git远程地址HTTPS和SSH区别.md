# Git 远程地址使用 HTTPS 和 SSH 的区别

日期：2026-07-08

## 当前仓库使用的连接方式

当前机器上，本仓库 `Algorithm-exercise` 使用的是 HTTPS 方式连接 GitHub。

通过以下命令查看：

```powershell
git remote -v
```

当前输出为：

```powershell
origin  https://github.com/gcfu0310/Algorithm-exercise.git (fetch)
origin  https://github.com/gcfu0310/Algorithm-exercise.git (push)
```

只要远程地址以 `https://` 开头，就说明当前仓库使用的是 HTTPS 连接方式。

## HTTPS 方式

HTTPS 地址通常长这样：

```powershell
https://github.com/用户名/仓库名.git
```

例如当前仓库：

```powershell
https://github.com/gcfu0310/Algorithm-exercise.git
```

HTTPS 方式的特点：

- 使用账号认证，通常配合 GitHub Personal Access Token 或 Git Credential Manager。
- 第一次认证后，凭据可能会被系统或 Git Credential Manager 保存。
- 在很多网络环境下可以直接使用，因为 HTTPS 使用的是常见的 `443` 端口。
- 如果访问 GitHub 不稳定，可能需要给 Git 配置 HTTP/HTTPS 代理。

本次遇到的 `git push` 报错：

```powershell
fatal: unable to access 'https://github.com/gcfu0310/Algorithm-exercise.git/': Recv failure: Connection was reset
```

就是 HTTPS 连接 GitHub 时网络连接被重置导致的。最终通过配置 Git 代理解决：

```powershell
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897
```

## SSH 方式

SSH 地址通常长这样：

```powershell
git@github.com:用户名/仓库名.git
```

如果当前仓库改成 SSH，地址会是：

```powershell
git@github.com:gcfu0310/Algorithm-exercise.git
```

SSH 方式的特点：

- 使用 SSH 密钥认证，不需要每次输入 GitHub 账号密码或 token。
- 需要先在本机生成 SSH key，并把公钥添加到 GitHub。
- 配置好以后，日常 `git pull`、`git push` 会比较方便。
- 默认使用 `22` 端口；如果网络环境屏蔽了 `22` 端口，可以配置 SSH 走 `443` 端口。

## 两种方式的主要区别

| 对比项 | HTTPS | SSH |
| --- | --- | --- |
| 远程地址格式 | `https://github.com/user/repo.git` | `git@github.com:user/repo.git` |
| 认证方式 | token 或 Git Credential Manager | SSH key |
| 是否需要配置密钥 | 不需要 SSH 密钥 | 需要 SSH 密钥 |
| 常用端口 | `443` | 默认 `22`，也可配置 `443` |
| 适合场景 | 临时使用、刚开始配置 Git、HTTPS 网络稳定 | 长期开发、频繁 push/pull |
| 常见问题 | 代理、token、凭据缓存 | SSH key 未配置、端口被拦截 |

## 如何判断当前仓库使用哪种方式

执行：

```powershell
git remote -v
```

判断规则：

- 如果地址以 `https://` 开头，说明使用 HTTPS。
- 如果地址以 `git@github.com:` 开头，说明使用 SSH。

## 如何从 HTTPS 切换到 SSH

如果已经配置好 GitHub SSH key，可以执行：

```powershell
git remote set-url origin git@github.com:gcfu0310/Algorithm-exercise.git
```

然后再次查看：

```powershell
git remote -v
```

如果输出变成：

```powershell
origin  git@github.com:gcfu0310/Algorithm-exercise.git (fetch)
origin  git@github.com:gcfu0310/Algorithm-exercise.git (push)
```

就说明已经切换为 SSH 连接方式。

## 如何从 SSH 切回 HTTPS

如果想切回 HTTPS，可以执行：

```powershell
git remote set-url origin https://github.com/gcfu0310/Algorithm-exercise.git
```

## 建议

当前仓库已经可以通过 HTTPS 配合代理正常 `git push`，所以可以继续使用 HTTPS。

如果以后经常遇到 HTTPS 连接被重置、token 认证麻烦、或者需要更稳定地长期使用 GitHub，可以考虑配置 SSH key，并将远程地址切换为 SSH。
