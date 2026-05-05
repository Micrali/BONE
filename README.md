# 🦴 骨振识息

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-REST-092E20?style=flat-square&logo=django&logoColor=white)
![Vue](https://img.shields.io/badge/Vue.js-3.x-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-Siamese-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Signal](https://img.shields.io/badge/HCR-MFCC-49D8FF?style=flat-square)

**骨振识息** 是基于 **头部接触响应 HCR（Head Contact Response）**、**Chirp 主动探测** 与 **Siamese 深度度量学习** 的智能隐式身份认证系统，名称统一采用“骨振识息”。

[🚀 快速开始](#-快速开始) • [📖 功能特性](#-功能特性) • [🏗️ 系统架构](#️-系统架构) • [📂 代码结构](#-代码结构) • [🎯 API 接口体系](#-api-接口体系)

---

## 📝 项目概述

**骨振识息** 面向耳机、可穿戴设备和连续身份认证场景，利用骨传导耳机与头部组织之间形成的接触振动响应进行隐式身份验证。系统播放短时 Chirp 扫频激励信号，采集用户头部结构、软组织、佩戴姿态共同作用下产生的 HCR（Head Contact Response）响应，并从响应信号中提取 MFCC、频率响应和统计特征，最终通过 Siamese 度量学习模型判断当前佩戴者是否与注册模板一致。

系统围绕“主动激励—振动响应采集—HCR 特征提取—Siamese 相似度匹配—认证决策”构建完整认证流程：

- ✅ Vue 3 前端展示与认证工作台
- ✅ Django REST API 后端服务
- ✅ HCR 真实数据接入与样本管理接口
- ✅ Chirp 激励、滤波、频响估计、MFCC 特征提取
- ✅ Siamese 编码器结构与模板认证流程
- ✅ 用户注册、样本入库、身份验证与指标统计
- ✅ Docker / Nginx / GitHub Pages 前端部署支持

> 说明：项目整体不是纯 JS 项目。前端使用 JavaScript / Vue.js，后端服务与认证算法核心使用 Python。

---

## 🎯 核心技术

- 🧠 **Siamese 认证模型**：共享权重的一维卷积编码器，学习用户 HCR 特征相似度
- 🦴 **头部接触响应 HCR**：利用骨骼、软组织、佩戴姿态形成的个体差异进行身份认证
- 📡 **Chirp 主动探测**：通过 50Hz-850Hz 短时扫频信号激发头部振动反馈
- 🎧 **骨传导耳机适配**：面向骨传导耳机、可穿戴设备和无感认证场景
- 📊 **MFCC + 频响特征**：融合声学特征、频域响应与统计特征
- ⚡ **低样本注册**：支持 10 组样本快速建立用户模板
- 🛡️ **抗攻击验证**：支持本人验证、攻击者样本验证与 FAR / FRR 指标统计
- 🌐 **前后端联调**：Vue 工作台可直接调用 Django API 完成注册与验证

---

## 🚀 快速开始

### 📦 环境准备

```bash
# 1. 创建虚拟环境（推荐）
python -m venv guzhen_env

# 2. 激活虚拟环境
# Windows:
bonevibauth_env\Scripts\activate
# Linux/macOS:
source bonevibauth_env/bin/activate

# 3. 安装 Python 依赖
pip install -r requirements.txt
```

### 方式一：完整系统启动（推荐）

```bash
# 1. 初始化后端数据库
cd backend
python manage.py migrate
python manage.py seed_demo_data

# 2. 启动 Django API 服务
python manage.py runserver
```

另开一个终端：

```bash
# 3. 安装前端依赖
npm install

# 4. 启动 Vue 前端
npm run dev
```

启动成功后访问：

```text
前端主页: http://127.0.0.1:5173
后端 API: http://127.0.0.1:8000/api/health/
```

### 方式二：算法核心直接演示

```bash
# 注册 demo-user 并执行本人 / 攻击者验证
python algorithms/scripts/demo_auth.py
```

### 方式三：真实数据 / 样本批处理

```bash
# 生成或导入 HCR 样本后执行评估
python algorithms/scripts/evaluate_simulated.py
```

### 方式四：Docker Compose 部署

```bash
copy .env.example .env

docker compose up --build
```

---

## 🌐 系统访问

启动成功后，访问以下地址：

- 🏠 **项目主页**：`http://127.0.0.1:5173`
- 🧪 **认证工作台**：主页中的“注册 / 验证联调工作台”区域
- 🔌 **API 健康检查**：`http://127.0.0.1:8000/api/health/`
- 📡 **Chirp 配置**：`http://127.0.0.1:8000/api/chirp-config/`
- 📊 **系统指标**：`http://127.0.0.1:8000/api/metrics/`
- 🛠️ **Django 后台**：`http://127.0.0.1:8000/admin/`

---

## 🎉 功能特性

### 🤖 AI 隐式认证

- 🎯 **用户注册模板生成**：上传或接入多组 HCR 响应样本，自动生成用户模板
- 🔍 **身份验证决策**：输入待验证 HCR 信号，输出认证分数、距离、阈值与接受结果
- 🧠 **Siamese 特征编码**：一维卷积网络结构学习 HCR 深层表征
- 📊 **MFCC 特征提取**：从振动响应中提取声学倒谱特征与差分统计量
- 📡 **频响估计**：基于 Welch / CSD 估计输入激励到响应信号的频率响应

### 🛡️ 安全防护

- 🧬 **生物特征认证**：利用用户头部结构差异，降低密码泄露风险
- 🎭 **攻击者样本验证**：支持 impostor 模式检测攻击样本
- 🚨 **FAR / FRR 指标统计**：记录误接受率、误拒绝率和运行时认证结果
- 🔐 **Bearer Token 鉴权**：后端支持轻量 API Token 保护
- 📋 **会话审计**：数据库记录每次认证分数、阈值、延迟和结果

### 📈 数据分析

- 📊 **认证准确率展示**：展示作品书中的 BAC、FAR、FRR、响应时间等指标
- 📉 **采样率影响分析**：展示 50Hz-467Hz 不同采样率下的认证表现
- 🧪 **攻击鲁棒性分析**：展示 BMI、BFR、SMR 等攻击场景 FAR
- 📁 **真实样本管理**：后端模型保存用户样本、特征向量与认证会话
- 🧾 **实验脚本评估**：提供批处理评估脚本用于指标复现

### 🔧 系统管理

- ⚙️ **Django 后台管理**：可查看 Subject、HCRSample、AuthSession
- 🗄️ **数据库切换**：默认 SQLite，可切换 MySQL
- 🐳 **容器化部署**：提供前后端 Dockerfile 与 Compose 配置
- 🌐 **前端静态部署**：支持 Vite build 后部署到 GitHub Pages / Nginx
- 🔄 **前后端分离联调**：支持 CORS 配置与独立部署

---

## 🏗️ 系统架构

```text
┌────────────────────────────────────────────────────────────────┐
│                        Vue 3 前端展示层                         │
│  项目主页 / 系统流程 / 实验指标 / 注册验证工作台 / API 联调       │
└───────────────────────────────┬────────────────────────────────┘
                                │ HTTP / JSON
┌───────────────────────────────▼────────────────────────────────┐
│                    Django REST API 服务层                       │
│  health / chirp-config / enroll / verify / metrics / admin       │
└───────────────────────────────┬────────────────────────────────┘
                                │ ORM / Service Call
┌───────────────────────────────▼────────────────────────────────┐
│                     骨振识息 算法核心层                      │
│  Chirp 生成 → HCR 预处理 → 频响估计 → MFCC → Siamese / 模板验证  │
└───────────────────────────────┬────────────────────────────────┘
                                │ Feature / Template / Session
┌───────────────────────────────▼────────────────────────────────┐
│                         数据持久化层                            │
│  Subject / HCRSample / AuthSession / 用户模板 / 真实 HCR 数据     │
└────────────────────────────────────────────────────────────────┘
```

### 🔄 核心认证流程

```text
1. 用户佩戴骨传导耳机
2. 系统播放短时 Chirp 激励
3. 采集 IMU / HCR 头部振动响应
4. 对响应信号进行归一化和滤波
5. 估计 HCR 频率响应并提取 MFCC
6. Siamese 编码器 / 模板验证器计算相似度
7. 后端返回 accepted、score、distance、threshold
8. 前端展示认证结果和运行指标
```

---

## 📂 代码结构

### 🗂️ 项目根目录

```text
骨振识息/
├── 🚀 package.json                 # 前端依赖与 Vite 脚本
├── 📦 requirements.txt             # Python 后端与算法依赖
├── 📋 README.md                    # 项目说明文档
├── 🧾 INSTALL.md                   # 安装部署说明
├── 📜 OPEN_SOURCE_COMPONENTS.md    # 开源组件使用说明
├── ⚙️ .env.example                 # 环境变量模板
├── 🐳 docker-compose.yml           # 前后端容器编排
└── 📄 LICENSE                      # MIT License
```

### 🌐 前端架构 `src/`

```text
src/
├── 📱 main.js                      # Vue 应用入口
├── 📦 App.vue                      # 首页、系统介绍、认证工作台
├── 🎨 styles.css                   # 全局视觉样式
├── 🔌 services/
│   └── api.js                      # Django API 客户端封装
└── 📡 utils/
    └── signal.js                   # 前端 HCR / Chirp 信号生成工具
```

### 🐍 后端架构 `backend/`

```text
backend/
├── 🚀 manage.py                    # Django 管理入口
├── ⚙️ bonevibauth/
│   ├── settings.py                 # 项目配置、数据库、CORS、算法参数
│   ├── urls.py                     # 全局 URL 路由
│   └── wsgi.py                     # WSGI 服务入口
└── 🔐 authentication/
    ├── models.py                   # Subject / HCRSample / AuthSession
    ├── serializers.py              # 请求与响应序列化
    ├── views.py                    # REST API 视图
    ├── urls.py                     # 认证模块路由
    ├── security.py                 # Bearer Token 鉴权
    ├── admin.py                    # Django Admin 管理
    ├── migrations/                 # 数据库迁移
    └── management/commands/
        └── seed_demo_data.py       # 真实项目演示数据初始化
```

### 🧠 算法核心 `algorithms/`

```text
algorithms/
├── bonevibauth/
│   ├── signal_processing.py        # Chirp 生成、归一化、滤波、频响估计
│   ├── features.py                 # MFCC + HCR 频响特征提取
│   ├── siamese.py                  # SiameseEncoder + TemplateVerifier
│   ├── pipeline.py                 # 端到端认证管线
│   └── __init__.py
└── scripts/
    ├── simulate_dataset.py         # HCR 数据生成 / 数据导入辅助
    ├── demo_auth.py                # 注册与验证演示
    └── evaluate_simulated.py       # BAC / FAR / FRR 指标评估
```

### 🐳 部署配置 `deploy/`

```text
deploy/
├── Dockerfile.backend              # Django + Python 算法服务镜像
├── Dockerfile.frontend             # Vue 构建 + Nginx 静态服务镜像
└── nginx.frontend.conf             # 前端 Nginx 配置
```

---

## 🎯 API 接口体系

### 🔐 系统健康与配置

| API | 方法 | 功能 |
| --- | --- | --- |
| `/api/health/` | GET | 返回系统健康状态、核心模块列表 |
| `/api/chirp-config/` | GET | 返回采样率、Chirp 频率范围、持续时间和探测样本 |
| `/api/metrics/` | GET | 返回作品书指标、运行时指标和近期认证会话 |

### 🧬 HCR 注册与认证

| API | 方法 | 功能 |
| --- | --- | --- |
| `/api/enroll/` | POST | 提交多组真实 HCR 样本，生成用户认证模板 |
| `/api/verify/` | POST | 提交待验证 HCR 样本，返回身份认证结果 |

### 📥 注册请求示例

```json
{
  "external_id": "user-001",
  "display_name": "测试用户",
  "device_model": "Bone Conduction Earphone",
  "sample_rate": 467,
  "signals": [[0.01, 0.02, -0.01], [0.03, 0.01, -0.02]]
}
```

### 📤 验证响应示例

```json
{
  "session_id": 1,
  "subject": "user-001",
  "accepted": true,
  "score": 0.936421,
  "distance": 0.065693,
  "threshold": 0.65,
  "latency_ms": 54.05
}
```

---

## ⚡ 核心特性示例

### 🧠 Python 端认证管线

```python
from bonevibauth.pipeline import BoneVibAuthPipeline

pipeline = BoneVibAuthPipeline()
features = [pipeline.extract_feature(signal) for signal in enrollment_signals]
template = pipeline.build_template(features)
pipeline.save_template('user-001', template)

claimed = pipeline.extract_feature(claimed_signal)
result = pipeline.verify('user-001', claimed)
```

### 🌐 前端调用后端认证

```javascript
import { enrollUser, verifyUser } from './services/api'

await enrollUser({
  external_id: 'user-001',
  sample_rate: 467,
  signals: enrollmentSignals
})

const result = await verifyUser({
  external_id: 'user-001',
  sample_rate: 467,
  claimed_signal: hcrSignal
})
```

---

## 🎮 使用指南

### 1️⃣ 用户注册

1. 启动 Django 后端和 Vue 前端；
2. 打开前端主页；
3. 进入“注册 / 验证联调工作台”；
4. 输入用户 ID 和显示名称；
5. 点击“生成 10 组 HCR 并注册”；
6. 后端将保存用户样本并生成认证模板。

### 2️⃣ 身份验证

1. 在工作台中选择“本人样本”或“攻击者样本”；
2. 点击“提交验证”；
3. 后端执行 HCR 特征提取和模板匹配；
4. 页面展示 `accepted`、`score`、`distance`、`threshold`。

### 3️⃣ 真实数据接入

真实数据可通过 `/api/enroll/` 和 `/api/verify/` 接口提交。数据格式为一维时间序列数组，建议先完成：

- 采样率统一；
- 时间同步；
- 去除明显异常值；
- 按用户 ID 分组；
- 每名用户至少 10 组注册样本。

---

## 🔧 技术栈

### 🎨 前端技术

- ⚡ **Vue 3**：现代响应式前端框架
- 🧩 **Element Plus**：企业级 UI 组件库
- 📊 **ECharts**：实验指标与认证数据可视化
- 🛠️ **Vite**：前端构建与开发服务器
- 🔌 **Fetch API**：前后端接口通信

### 🐍 后端技术

- 🚀 **Django**：后端 Web 框架
- 🔗 **Django REST Framework**：REST API 构建
- 🌐 **django-cors-headers**：跨域联调支持
- 🗄️ **SQLite / MySQL**：样本、模板和认证会话存储
- 🔐 **Bearer Token**：轻量接口鉴权

### 🤖 AI / 信号处理技术

- 🧠 **PyTorch**：Siamese 网络结构定义
- 📊 **NumPy**：数值计算和向量处理
- 📡 **SciPy**：Chirp 生成、滤波、Welch / CSD 频响估计
- 🎼 **librosa**：MFCC 与音频特征提取
- 📦 **joblib**：用户认证模板持久化

---

## 📋 系统要求

### 🖥️ 最低配置

- Python：3.10+
- Node.js：18+
- npm：9+
- 内存：4GB RAM
- 存储：2GB 可用空间
- 浏览器：Chrome 90+ / Edge 90+ / Firefox 88+

### 🚀 推荐配置

- Python：3.11+
- Node.js：20+
- 内存：8GB+ RAM
- 存储：10GB+ SSD
- 数据库：MySQL 8+（用于多人真实样本管理）
- GPU：CUDA 兼容 GPU（用于后续训练深度 Siamese 权重，可选）

---

## 📦 核心依赖包

- 🌐 `Django`：后端服务框架
- 🔌 `djangorestframework`：API 服务
- 🌍 `django-cors-headers`：跨域请求支持
- 🔢 `numpy`：数组与数值运算
- 📡 `scipy`：信号处理
- 🎼 `librosa`：MFCC 特征提取
- 🔥 `torch`：Siamese 网络结构
- 🧪 `scikit-learn`：评估与实验扩展
- 📦 `joblib`：模板保存和加载
- 🎨 `vue`：前端框架
- 🧩 `element-plus`：前端 UI
- 📊 `echarts`：数据可视化

---

## 📄 许可证

本项目采用 MIT License，详见 `LICENSE`。
