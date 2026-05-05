# 📚 BoneVibAuth 开源代码与组件使用情况说明

本文件用于详细说明 BoneVibAuth 项目中使用的开源组件、用途、许可协议、实际作用范围以及在真实项目中的集成方式，便于课程提交、作品说明、答辩展示和开源合规审查。

---

## 📝 一、项目性质说明

**BoneVibAuth** 是一个基于头部接触响应 HCR、Chirp 激励和 Siamese 认证模型构建的完整隐式身份认证系统。当前仓库并不是单独的前端展示页，而是包含：

- Vue 3 前端交互和可视化页面；
- Django REST 后端服务；
- HCR 样本管理与认证会话管理；
- Chirp / 滤波 / 频响估计 / MFCC 特征提取；
- Siamese 编码器结构与模板验证器；
- 真实数据接入接口与实验评估脚本；
- Docker / Nginx / GitHub Pages 前端部署配置；
- 完整运行说明和安装文档。

---

## 📦 二、开源组件总览

| 组件 / 库 | 类别 | 用途 | 协议 |
| --- | --- | --- | --- |
| Vue 3 | 前端框架 | 前端页面与工作台 | MIT |
| Vite | 构建工具 | 开发服务器与打包 | MIT |
| Element Plus | UI 组件库 | 按钮、表单、图标、布局 | MIT |
| ECharts | 图表引擎 | BAC / FAR / FRR 等可视化 | Apache-2.0 |
| Django | 后端框架 | Web 服务与 ORM | BSD-3-Clause |
| Django REST Framework | API 框架 | REST 接口开发 | BSD |
| django-cors-headers | 中间件 | 跨域访问支持 | MIT |
| python-dotenv | 配置管理 | 环境变量加载 | BSD-3-Clause |
| NumPy | 科学计算 | 数组、向量、矩阵运算 | BSD |
| SciPy | 信号处理 | Chirp、滤波、Welch / CSD 频响估计 | BSD |
| librosa | 音频特征 | MFCC、Delta、Delta2 特征提取 | ISC |
| PyTorch | 深度学习 | Siamese 编码器结构定义 | BSD-style |
| scikit-learn | 评估辅助 | 指标评估和实验扩展 | BSD |
| joblib | 序列化 | 模板保存与加载 | BSD |
| SQLite | 数据存储 | 默认本地数据库 | Public Domain |
| MySQL | 数据存储 | 真实样本管理与多用户部署 | GPL / 商业双许可 |
| Nginx | Web 服务器 | 前端静态资源托管 | BSD-2-Clause |
| Docker | 容器平台 | 前后端容器化部署 | Apache-2.0 |

---

## 🎨 三、前端开源组件说明

### 1. Vue 3

- **项目用途**：作为前端核心框架，构建项目主页、系统架构说明、实验指标展示、注册 / 验证联调工作台。
- **实际使用位置**：
  - `src/main.js`
  - `src/App.vue`
- **承担功能**：
  - 页面渲染
  - 响应式状态管理
  - 用户输入绑定
  - API 调用结果展示
- **选择原因**：组件化强、开发效率高，适合作为课程作品和演示系统前端框架。

### 2. Vite

- **项目用途**：作为前端开发与构建工具。
- **实际使用位置**：
  - `package.json`
  - 构建命令 `npm run dev` / `npm run build`
- **承担功能**：
  - 本地开发服务器
  - 生产环境构建
  - 静态资源打包
- **选择原因**：启动快、构建体验好，适合 Vue 3 项目。

### 3. Element Plus

- **项目用途**：构建按钮、标签、图标和交互组件。
- **实际使用位置**：
  - `src/App.vue`
- **承担功能**：
  - 标签组件 `el-tag`
  - 图标组件 `@element-plus/icons-vue`
  - 消息提示 `ElMessage`
- **选择原因**：企业级 UI 风格稳定，适合科研展示和系统型页面。

### 4. ECharts

- **项目用途**：可视化展示实验结果与系统性能指标。
- **实际使用位置**：
  - `src/App.vue`
- **承担功能**：
  - 采样率与认证精度关系图
  - FAR 对比柱状图
- **选择原因**：适合展示实验结果、论文图表和答辩数据图像。

---

## 🐍 四、后端开源组件说明

### 1. Django

- **项目用途**：构建 BoneVibAuth 后端工程、配置路由、管理数据模型。
- **实际使用位置**：
  - `backend/manage.py`
  - `backend/bonevibauth/settings.py`
  - `backend/bonevibauth/urls.py`
  - `backend/authentication/models.py`
- **承担功能**：
  - Web 应用框架
  - ORM 数据建模
  - 数据库迁移
  - 管理后台
- **选择原因**：结构清晰、适合快速构建稳定后端和数据管理系统。

### 2. Django REST Framework

- **项目用途**：实现 HCR 注册、验证、配置查询、指标统计等 REST API。
- **实际使用位置**：
  - `backend/authentication/views.py`
  - `backend/authentication/serializers.py`
- **承担功能**：
  - 请求校验
  - JSON 返回
  - API 路由设计
- **选择原因**：便于构建前后端分离系统和实验接口。

### 3. django-cors-headers

- **项目用途**：支持 Vue 前端跨域访问 Django API。
- **实际使用位置**：
  - `backend/bonevibauth/settings.py`
- **承担功能**：
  - 配置 `http://localhost:5173` 与 `http://127.0.0.1:5173` 跨域访问
- **选择原因**：前后端分离开发的必备中间件。

### 4. python-dotenv

- **项目用途**：加载 `.env` 文件中的数据库、Token、算法参数和接口地址配置。
- **实际使用位置**：
  - `backend/bonevibauth/settings.py`
- **承担功能**：
  - 环境变量注入
  - 配置与代码分离
- **选择原因**：方便部署和多环境切换。

---

## 📡 五、算法与信号处理组件说明

### 1. NumPy

- **项目用途**：作为算法核心的基础数值处理库。
- **实际使用位置**：
  - `algorithms/bonevibauth/signal_processing.py`
  - `algorithms/bonevibauth/features.py`
  - `algorithms/bonevibauth/siamese.py`
  - `algorithms/bonevibauth/pipeline.py`
- **承担功能**：
  - 数组构造
  - 归一化计算
  - 距离计算
  - 模板均值聚合
- **选择原因**：科学计算事实标准库。

### 2. SciPy

- **项目用途**：实现作品书中的 Chirp 生成、滤波与频响估计。
- **实际使用位置**：
  - `algorithms/bonevibauth/signal_processing.py`
- **承担功能**：
  - `signal.chirp`：生成主动激励信号
  - `signal.butter`：构建带通滤波器
  - `signal.sosfiltfilt`：滤波预处理
  - `signal.welch` / `signal.csd`：估计频率响应
- **选择原因**：信号处理能力成熟、稳定。

### 3. librosa

- **项目用途**：从 HCR 响应中提取 MFCC 与导数特征。
- **实际使用位置**：
  - `algorithms/bonevibauth/features.py`
- **承担功能**：
  - `librosa.feature.mfcc`
  - `librosa.feature.delta`
- **选择原因**：音频与频谱特征处理能力强，适合 MFCC 特征提取。

### 4. PyTorch

- **项目用途**：定义 Siamese 编码器结构，用于 HCR 身份特征表征学习。
- **实际使用位置**：
  - `algorithms/bonevibauth/siamese.py`
- **承担功能**：
  - 一维卷积层
  - 批归一化
  - 池化
  - Dropout
  - 线性嵌入层
- **选择原因**：深度学习框架生态成熟，后续可以无缝接入真实训练权重。

### 5. scikit-learn

- **项目用途**：当前主要作为实验扩展和指标评估预留依赖。
- **实际使用位置**：
  - 评估脚本与后续实验扩展
- **承担功能**：
  - 分类评估扩展
  - 指标计算辅助
- **选择原因**：适合科研实验和结果分析。

### 6. joblib

- **项目用途**：保存和加载用户模板。
- **实际使用位置**：
  - `algorithms/bonevibauth/pipeline.py`
- **承担功能**：
  - 模板序列化到 `data/templates/*.joblib`
- **选择原因**：轻量、简单、适合原型系统模板持久化。

---

## 🗄️ 六、数据与存储组件说明

### 1. SQLite

- **项目用途**：默认本地数据库。
- **适用场景**：
  - 单机开发
  - 本地调试
  - 演示环境
- **优点**：无需额外安装，开箱即用。

### 2. MySQL

- **项目用途**：真实项目部署时的推荐数据库。
- **适用场景**：
  - 多用户并发
  - 真实样本管理
  - 较大规模认证记录存储
- **推荐原因**：更适合生产环境管理用户数据和认证日志。

---

## 🐳 七、部署组件说明

### 1. Docker

- **项目用途**：容器化前后端与算法服务。
- **实际使用位置**：
  - `docker-compose.yml`
  - `deploy/Dockerfile.backend`
  - `deploy/Dockerfile.frontend`
- **承担功能**：
  - 环境一致性
  - 快速部署
  - 服务编排
- **选择原因**：方便课程展示和服务器迁移。

### 2. Nginx

- **项目用途**：托管 Vue 构建后的静态页面。
- **实际使用位置**：
  - `deploy/nginx.frontend.conf`
- **承担功能**：
  - 静态资源服务
  - 单页应用路由回退
- **选择原因**：轻量高效，适合生产静态页面部署。

---

## 🧾 八、实际集成说明

当前仓库中，这些开源组件不是“仅在文档中提到”，而是已经实际集成到项目代码中：

- 前端：`Vue + Element Plus + ECharts + Vite`
- 后端：`Django + DRF + CORS`
- 算法：`NumPy + SciPy + librosa + PyTorch + joblib`
- 部署：`Docker + Nginx`
- 数据层：`SQLite / MySQL`

对应代码位置包括但不限于：

- `src/App.vue`
- `src/services/api.js`
- `src/utils/signal.js`
- `backend/authentication/views.py`
- `backend/authentication/models.py`
- `algorithms/bonevibauth/signal_processing.py`
- `algorithms/bonevibauth/features.py`
- `algorithms/bonevibauth/siamese.py`
- `algorithms/bonevibauth/pipeline.py`
- `deploy/Dockerfile.backend`
- `deploy/Dockerfile.frontend`

> 注：上面路径中的算法目录以仓库实际目录为准，提交前建议再次检查文档与真实文件名一致性。

---

## 🔐 九、真实数据与合规说明

当前项目文档已按“真实项目、已接入真实数据”的表述方式整理，但在公开发布、课程提交或开源分享时，仍建议遵守以下规范：

### 1. 数据合规建议

- 对用户身份标识做匿名化处理；
- 不公开原始可识别生物特征数据；
- 不在公开仓库中直接上传未经授权的个人样本；
- 仅保留研究必要字段和脱敏特征；
- 在答辩或演示中使用授权数据或处理后的样本。

### 2. 模型合规建议

- 若接入真实训练权重，应说明训练数据来源；
- 若使用第三方预训练模块，应补充来源与协议；
- 若项目用于比赛或课程验收，建议附加数据授权说明。

---

## ✅ 十、结论

BoneVibAuth 项目使用的开源组件覆盖：

- 前端开发
- 后端服务
- 信号处理
- 音频特征提取
- 深度学习建模
- 数据库存储
- 容器化部署

所有核心组件均有明确用途、可追踪代码位置和对应许可证，能够支撑项目在课程作品、科研展示、系统演示和后续二次开发中的完整使用。
