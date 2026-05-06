# GitHub Pages 前端部署说明

本项目的 Vue 前端已经构建为静态文件，并放置在仓库根目录，可直接通过 GitHub Pages 展示前端页面。

## 1. 当前根目录静态文件

根目录中用于 GitHub Pages 展示的关键文件包括：

```text
index.html
assets/
```

其中：

- `index.html`：前端页面入口；
- `assets/`：Vite 构建生成的 CSS、JavaScript 等静态资源。

## 2. GitHub Pages 部署步骤

1. 将 `BONE` 项目上传到 GitHub 仓库。
2. 打开仓库页面，进入 `Settings`。
3. 在左侧菜单中选择 `Pages`。
4. 在 `Build and deployment` 中选择 `Deploy from a branch`。
5. `Branch` 选择 `main`，目录选择 `/root`。
6. 点击保存，等待 GitHub Pages 自动部署完成。

部署成功后，访问地址格式如下：

```text
https://你的GitHub用户名.github.io/仓库名/
```

例如仓库名为 `BONE`，则访问地址通常为：

```text
https://你的GitHub用户名.github.io/BONE/
```

## 3. 修改前端后如何重新部署

如果修改了 `src/` 中的 Vue 前端源码，需要重新构建：

```bash
npm install
npm run build
```

构建完成后，将 `dist/` 中生成的内容同步到仓库根目录：

```text
dist/index.html  ->  index.html
dist/assets/     ->  assets/
```

提交并推送到 GitHub 后，GitHub Pages 会自动更新页面。

## 4. 本地预览方式

可以使用 Vite 本地预览：

```bash
npm run preview
```

也可以使用任意静态文件服务器打开根目录的 `index.html`。
