# 🚀 BoneVibAuth 安装与运行指南

BoneVibAuth 是一个已经工程化实现的完整隐式身份认证项目，包含 Vue 前端、Django 后端、HCR 真实数据接入、MFCC 特征提取和 Siamese 认证流程。

---

## 📋 环境要求

### 🖥️ 基础环境

| 环境 | 版本要求 | 说明 |
| --- | --- | --- |
| Python | 3.10+ | 后端服务和算法核心 |
| Node.js | 18+ | Vue 前端开发和构建 |
| npm | 9+ | 前端依赖管理 |
| Git | 2.x+ | 代码管理 |
| 浏览器 | Chrome 90+ / Edge 90+ / Firefox 88+ | 前端访问 |

### 🚀 推荐环境

- Python 3.11+
- Node.js 20+
- 8GB+ RAM
- 10GB+ SSD
- MySQL 8+（多人真实样本管理时推荐）
- CUDA GPU（后续训练深度 Siamese 权重时可选）

---

## 📦 方式一：本地完整运行（推荐）

### 1️⃣ 创建并激活 Python 虚拟环境

```bash
python -m venv bonevibauth_env

# Windows
bonevibauth_env\Scripts\activate

# Linux/macOS
source bonevibauth_env/bin/activate
```

### 2️⃣ 安装 Python 依赖

```bash
pip install -r requirements.txt
```

如果 Windows 安装 `mysqlclient` 失败，可以先使用默认 SQLite，不影响本地演示和真实数据接口接入。

### 3️⃣ 初始化环境变量

```bash
copy .env.example .env
```

Linux / macOS：

```bash
cp .env.example .env
```

`.env` 默认使用 SQLite。如需 MySQL，可修改：

```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=bonevibauth
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

### 4️⃣ 初始化 Django 数据库

```bash
cd backend
python manage.py migrate
python manage.py seed_demo_data
```

执行后会创建：

- `Subject` 用户信息表
- `HCRSample` HCR 样本表
- `AuthSession` 认证会话表
- 演示用户认证模板

### 5️⃣ 启动后端 API

```bash
python manage.py runserver
```

后端访问地址：

```text
http://127.0.0.1:8000/api/health/
```

### 6️⃣ 安装前端依赖

另开终端，在项目根目录执行：

```bash
npm install
```

### 7️⃣ 启动 Vue 前端

```bash
npm run dev
```

前端访问地址：

```text
http://127.0.0.1:5173
```

---

## 🌐 系统访问入口

| 入口 | 地址 | 说明 |
| --- | --- | --- |
| 项目主页 | `http://127.0.0.1:5173` | 项目介绍、架构、指标和认证工作台 |
| 认证工作台 | 首页对应区域 | 注册用户、验证身份、查看认证结果 |
| API 健康检查 | `http://127.0.0.1:8000/api/health/` | 后端服务状态 |
| Chirp 配置 | `http://127.0.0.1:8000/api/chirp-config/` | 探测信号参数 |
| 系统指标 | `http://127.0.0.1:8000/api/metrics/` | 论文指标和运行时指标 |
| Django 后台 | `http://127.0.0.1:8000/admin/` | 数据管理后台 |

---

## 🧪 核心功能验证

### 🎯 验证一：前端注册 / 验证工作台

1. 启动后端和前端；
2. 打开 `http://127.0.0.1:5173`；
3. 在“注册 / 验证联调工作台”点击“检查 API”；
4. 输入用户 ID，例如 `demo-user`；
5. 点击“生成 10 组 HCR 并注册”；
6. 选择“本人样本”并提交验证；
7. 切换“攻击者样本”并提交验证；
8. 对比 `accepted`、`score`、`distance` 和 `threshold`。

### 🎯 验证二：算法脚本演示

在项目根目录执行：

```bash
python algorithms/scripts/demo_auth.py
```

输出示例：

```text
genuine: {'accepted': True, 'score': ...}
impostor: {'accepted': False, 'score': ...}
```

### 🎯 验证三：批量评估 BAC / FAR / FRR

```bash
python algorithms/scripts/evaluate_simulated.py
```

该脚本会完成：

- 多用户样本注册
- 本人样本验证
- 攻击者样本验证
- BAC / FAR / FRR 统计

---

## 📡 真实数据接入说明

系统已支持真实 HCR 数据通过 API 接入。

### 注册接口

```text
POST /api/enroll/
```

请求体：

```json
{
  "external_id": "user-001",
  "display_name": "测试用户",
  "device_model": "Bone Conduction Earphone",
  "sample_rate": 467,
  "signals": [
    [0.012, 0.023, -0.010, 0.035],
    [0.010, 0.021, -0.012, 0.031]
  ]
}
```

### 验证接口

```text
POST /api/verify/
```

请求体：

```json
{
  "external_id": "user-001",
  "sample_rate": 467,
  "claimed_signal": [0.012, 0.020, -0.009, 0.033]
}
```

### 数据建议

- 每名用户建议至少 10 组注册样本；
- 采样率应与后端配置一致；
- 每组样本建议保持相近时长；
- 真实采集前建议完成时间同步和异常值清理；
- 对外发布数据前需完成匿名化和脱敏处理。

---

## 🐳 Docker Compose 部署

### 1️⃣ 准备配置

```bash
copy .env.example .env
```

### 2️⃣ 构建并启动

```bash
docker compose up --build
```

### 3️⃣ 访问服务

```text
前端: http://localhost:8080
后端: http://localhost:8000/api/health/
```

---

## 🏗️ 前端静态部署

GitHub Pages、Nginx 或静态服务器只适合部署前端页面。

```bash
npm run build
```

构建结果位于：

```text
dist/
```

如需完整功能，必须同时部署 Django 后端和 Python 算法服务。

---

## 🔧 常见问题

### ❌ 前端无法连接后端

检查：

1. Django 是否已启动；
2. `.env` 中 `VITE_API_BASE_URL` 是否正确；
3. Django CORS 是否包含前端地址；
4. 浏览器控制台是否存在跨域报错。

### ❌ `pip install mysqlclient` 失败

解决方式：

1. 先使用默认 SQLite；
2. 或安装 MySQL 开发依赖后重新安装；
3. Windows 可使用预编译 wheel 或改用 PyMySQL 方案。

### ❌ 验证返回 `subject not enrolled`

说明该用户未完成注册。请先调用 `/api/enroll/` 或在前端点击注册按钮。

### ❌ 分数偏低或误拒绝

检查：

1. 注册样本和验证样本是否来自同一用户；
2. 采样率是否一致；
3. 信号长度是否过短；
4. HCR 原始数据是否未归一化或存在明显噪声；
5. `BVA_AUTH_THRESHOLD` 是否需要调整。

---

## ✅ 安装完成检查清单

- [ ] Python 虚拟环境已激活
- [ ] `pip install -r requirements.txt` 成功
- [ ] `npm install` 成功
- [ ] `python manage.py migrate` 成功
- [ ] Django 后端可访问 `/api/health/`
- [ ] Vue 前端可打开主页
- [ ] 前端认证工作台能检查 API
- [ ] 注册接口能生成用户模板
- [ ] 验证接口能返回认证结果
