# 新电脑 Git 设置和连接 GitHub 的完整流程

日期：2026-07-08

## 总体思路

拿到一台新电脑后，如果想用 Git 管理代码，并把代码上传到 GitHub，整体流程可以分成几步：

1. 安装 Git。
2. 配置 Git 用户信息。
3. 选择连接 GitHub 的方式：HTTPS 或 SSH。
4. 如果选择 SSH，需要生成 SSH 密钥，并把公钥添加到 GitHub。
5. 在 GitHub 页面创建远程仓库。
6. 在本地仓库中添加 GitHub 远程地址。
7. 提交代码并推送到 GitHub。

## 第一步：安装 Git

先在电脑上安装 Git。

安装完成后，可以在终端中执行：

```powershell
git --version
```

如果能看到 Git 版本号，说明 Git 已经安装成功。

## 第二步：配置 Git 用户信息

Git 需要知道每次提交代码的人是谁。

常用配置命令：

```powershell
git config --global user.name "你的名字或GitHub用户名"
git config --global user.email "你的GitHub邮箱"
```

查看配置：

```powershell
git config --global user.name
git config --global user.email
```

这一步影响的是提交记录中的作者信息，不等于登录 GitHub。

## 第三步：选择连接 GitHub 的方式

Git 连接 GitHub 常见有两种方式：

- HTTPS
- SSH

它们都可以用于 `git clone`、`git pull`、`git push`，但认证方式不同。

## HTTPS 方式

HTTPS 远程地址通常长这样：

```powershell
https://github.com/用户名/仓库名.git
```

例如：

```powershell
https://github.com/gcfu0310/Algorithm-exercise.git
```

HTTPS 方式通常依赖：

- GitHub 账号登录
- Personal Access Token
- Git Credential Manager 保存凭据
- 必要时配置 HTTP/HTTPS 代理

如果使用 HTTPS，SSH 密钥并不会参与认证。

## SSH 方式

SSH 远程地址通常长这样：

```powershell
git@github.com:用户名/仓库名.git
```

例如：

```powershell
git@github.com:gcfu0310/Algorithm-exercise.git
```

SSH 方式依赖 SSH key。

使用 SSH 时，本机需要先生成一对密钥：

- 私钥：保存在本机，不能泄露。
- 公钥：添加到 GitHub 账号中。

GitHub 通过公钥识别这台机器是否有权限访问对应账号下的仓库。

## 第四步：生成 SSH 密钥并添加到 GitHub

如果选择 SSH 方式，需要先生成 SSH key。

常用命令：

```powershell
ssh-keygen -t ed25519 -C "你的GitHub邮箱"
```

生成后，一般会在用户目录下的 `.ssh` 文件夹中看到类似文件：

```powershell
id_ed25519
id_ed25519.pub
```

其中：

- `id_ed25519` 是私钥，留在本机。
- `id_ed25519.pub` 是公钥，可以添加到 GitHub。

把公钥内容添加到 GitHub：

```text
GitHub -> Settings -> SSH and GPG keys -> New SSH key
```

添加完成后，可以用下面的命令测试 SSH 是否能连接 GitHub：

```powershell
ssh -T git@github.com
```

如果成功，通常会看到类似提示：

```powershell
Hi gcfu0310! You've successfully authenticated, but GitHub does not provide shell access.
```

这说明本机 SSH key 已经能被 GitHub 识别。

## 第五步：在 GitHub 页面创建仓库

进入 GitHub 页面，点击新建仓库。

创建仓库时需要注意：

- 仓库名要和本地项目含义对应。
- 可以选择公开或私有。
- 如果本地已经有代码，远程仓库可以先不勾选 README、.gitignore、license，避免后续合并冲突。

## 第六步：本地仓库添加远程地址

如果本地还没有初始化 Git 仓库，可以执行：

```powershell
git init
```

然后添加远程地址。

如果选择 HTTPS：

```powershell
git remote add origin https://github.com/用户名/仓库名.git
```

如果选择 SSH：

```powershell
git remote add origin git@github.com:用户名/仓库名.git
```

查看当前远程地址：

```powershell
git remote -v
```

判断规则：

- 以 `https://` 开头，说明当前仓库使用 HTTPS。
- 以 `git@github.com:` 开头，说明当前仓库使用 SSH。

## 第七步：提交并推送代码

常用流程：

```powershell
git add .
git commit -m "初始化提交"
git push -u origin main
```

后续继续提交时，一般执行：

```powershell
git add .
git commit -m "提交说明"
git push
```

## 当前这台机器的情况

当前 GitHub 账号页面中已经添加过 SSH key，说明这台机器曾经配置过 SSH 密钥，并把公钥添加到了 GitHub。

当前仓库 `Algorithm-exercise` 的远程地址为：

```powershell
origin  git@github.com:gcfu0310/Algorithm-exercise.git (fetch)
origin  git@github.com:gcfu0310/Algorithm-exercise.git (push)
```

因此，当前这个仓库现在实际使用的是 SSH 方式连接 GitHub。

## 容易混淆的地方

SSH key 添加到 GitHub 后，只代表这台机器具备了使用 SSH 连接 GitHub 的条件。

但某个具体仓库到底使用 HTTPS 还是 SSH，要看这个仓库的远程地址。

执行：

```powershell
git remote -v
```

如果看到：

```powershell
https://github.com/用户名/仓库名.git
```

说明这个仓库使用 HTTPS，即使 GitHub 账号里已经添加了 SSH key，也不会用到 SSH key。

如果看到：

```powershell
git@github.com:用户名/仓库名.git
```

说明这个仓库使用 SSH，会用 SSH key 进行认证。

## 建议记忆方式

可以把 GitHub 连接方式理解成两条路线：

```text
HTTPS 路线：Git -> HTTPS 地址 -> GitHub，认证靠 token / 凭据管理器 / 代理
SSH 路线：Git -> SSH 地址 -> GitHub，认证靠 SSH key
```

新电脑上如果想长期稳定使用 GitHub，建议优先配置 SSH。

如果只是临时使用，或者所在网络环境 HTTPS 更方便，也可以使用 HTTPS。
