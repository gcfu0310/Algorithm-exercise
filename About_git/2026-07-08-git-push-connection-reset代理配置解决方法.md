# Git push 报错 Recv failure: Connection was reset 的解决方法

日期：2026-07-08

## 问题现象

在执行 `git push` 时出现如下报错：

```powershell
fatal: unable to access 'https://github.com/gcfu0310/Algorithm-exercise.git/': Recv failure: Connection was reset
```

当前仓库远程地址使用的是 HTTPS：

```powershell
origin  https://github.com/gcfu0310/Algorithm-exercise.git
```

## 原因分析

该错误通常不是代码或 Git 提交记录的问题，而是本机到 GitHub HTTPS 连接过程中被重置。

常见原因包括：

- GitHub 网络连接不稳定
- 当前网络环境访问 GitHub 受限
- VPN 或代理端口配置不正确
- Git 没有走本机代理
- 防火墙或网络策略中断了 HTTPS 连接

## 解决方法

将 Git 的 HTTP 和 HTTPS 代理配置为当前可用的本机代理端口。

本次可用端口为 `7897`，执行以下命令：

```powershell
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897
```

然后重新推送：

```powershell
git push
```

## 本次操作记录

一开始尝试配置代理端口 `7890`：

```powershell
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

随后发现实际可用端口是 `7897`，因此改为：

```powershell
git config --global https.proxy http://127.0.0.1:7897
git config --global http.proxy http://127.0.0.1:7897
```

最后再次执行：

```powershell
git push
```

问题解决。

## 查看当前 Git 代理配置

可以通过以下命令确认当前代理配置：

```powershell
git config --global --get http.proxy
git config --global --get https.proxy
```

也可以查看所有相关配置：

```powershell
git config --global --list
```

## 如果以后再次遇到

1. 先确认代理软件是否正在运行。
2. 确认代理端口是否变化，例如 `7890`、`7897` 等。
3. 使用正确端口重新设置 Git 代理。
4. 再次执行 `git push`。

如果不想继续使用代理，可以清除 Git 代理配置：

```powershell
git config --global --unset http.proxy
git config --global --unset https.proxy
```
