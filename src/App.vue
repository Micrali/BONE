<template>
  <div class="app-shell">
    <aside class="side-panel">
      <div class="brand-block">
        <div class="brand-orb">B</div>
        <div>
          <strong>BoneVibAuth</strong>
          <span>骨振哨兵</span>
        </div>
      </div>
      <nav class="side-nav">
        <a href="#console">实时控制台</a>
        <a href="#workbench">认证工作台</a>
        <a href="#architecture">系统架构</a>
        <a href="#api">API 接口</a>
        <a href="#metrics">实验指标</a>
      </nav>
      <div class="side-status" :class="backendOnline ? 'online' : 'offline'">
        <span></span>
        {{ backendOnline ? 'Django API 在线' : '等待后端连接' }}
      </div>
    </aside>

    <main class="main-panel">
      <section id="console" class="hero-console">
        <div class="hero-copy">
          <el-tag class="hero-tag" effect="dark">Vue 3 · Django REST · HCR · MFCC · Siamese</el-tag>
          <h1>BoneVibAuth 真实数据隐式身份认证平台</h1>
          <p>
            前端已接入 Django API，可完成后端健康检查、HCR 样本注册、身份验证、认证结果展示和运行指标读取。
            系统围绕骨传导耳机头部接触响应构建端到端认证链路。
          </p>
          <div class="hero-actions">
            <button class="primary-btn" @click="checkBackend">连接后端</button>
            <a class="ghost-btn" href="#workbench">开始认证</a>
          </div>
        </div>

        <div class="security-card">
          <div class="security-header">
            <div>
              <span>Secure Session</span>
              <h3>{{ latestDecision }}</h3>
            </div>
            <div class="security-icon"><el-icon><Lock /></el-icon></div>
          </div>
          <div class="score-ring" :style="{ '--score': scorePercent + '%' }">
            <div>
              <strong>{{ scorePercent }}%</strong>
              <span>Confidence</span>
            </div>
          </div>
          <div class="mini-wave">
            <i v-for="bar in 46" :key="bar" :style="{ height: `${18 + Math.abs(Math.sin(bar * 0.55)) * 58}px` }"></i>
          </div>
          <div class="security-list">
            <div><span>Probe</span><b>Chirp 50-850Hz</b></div>
            <div><span>Feature</span><b>MFCC + HCR</b></div>
            <div><span>Verifier</span><b>Siamese / Template</b></div>
          </div>
        </div>
      </section>

      <section class="kpi-grid">
        <article v-for="metric in metrics" :key="metric.label" class="kpi-card">
          <span>{{ metric.label }}</span>
          <strong>{{ metric.value }}</strong>
          <small>{{ metric.note }}</small>
        </article>
      </section>

      <section id="workbench" class="section-block workbench-section">
        <div class="section-heading">
          <span>Authentication Workbench</span>
          <h2>前后端联调认证工作台</h2>
          <p>点击按钮即可调用 Django 后端接口：先注册 HCR 模板，再提交本人或攻击者样本完成身份验证。</p>
        </div>

        <div class="workbench-layout">
          <div class="glass-card control-card">
            <div class="card-title-row">
              <h3>1. 后端连接</h3>
              <span :class="backendOnline ? 'pill success' : 'pill danger'">{{ backendOnline ? 'ONLINE' : 'OFFLINE' }}</span>
            </div>
            <p class="mono-text">{{ healthStatus }}</p>
            <button class="primary-btn full" :disabled="loading" @click="checkBackend">检查 Django API</button>

            <div class="divider"></div>

            <div class="card-title-row">
              <h3>2. 用户注册</h3>
              <span class="pill">Enroll</span>
            </div>
            <label>用户 ID</label>
            <input v-model="subjectId" class="form-input" placeholder="例如 user-001" />
            <label>显示名称</label>
            <input v-model="displayName" class="form-input" placeholder="例如 测试用户" />
            <label>设备型号</label>
            <input v-model="deviceModel" class="form-input" placeholder="例如 Bone Conduction Earphone" />
            <button class="primary-btn full" :disabled="loading" @click="handleEnroll">生成 10 组 HCR 并注册</button>
          </div>

          <div class="glass-card verify-card">
            <div class="card-title-row">
              <h3>3. 身份验证</h3>
              <span class="pill accent">Verify</span>
            </div>
            <div class="mode-switch">
              <button :class="verifyMode === 'genuine' ? 'active' : ''" @click="verifyMode = 'genuine'">本人样本</button>
              <button :class="verifyMode === 'impostor' ? 'active' : ''" @click="verifyMode = 'impostor'">攻击者样本</button>
            </div>
            <button class="primary-btn full" :disabled="loading" @click="handleVerify">提交 HCR 验证</button>

            <div class="result-panel" :class="lastAccepted === true ? 'accepted' : lastAccepted === false ? 'rejected' : ''">
              <div class="result-topline">
                <span>认证结果</span>
                <b>{{ latestDecision }}</b>
              </div>
              <div class="result-stats">
                <div><span>Score</span><strong>{{ lastScore }}</strong></div>
                <div><span>Threshold</span><strong>{{ lastThreshold }}</strong></div>
                <div><span>Latency</span><strong>{{ lastLatency }}</strong></div>
              </div>
              <pre>{{ resultText }}</pre>
            </div>
          </div>

          <div class="glass-card signal-card">
            <div class="card-title-row">
              <h3>HCR 信号预览</h3>
              <span class="pill">Live</span>
            </div>
            <div ref="signalChart" class="chart signal-chart"></div>
            <div class="signal-info">
              <div><span>Sample Rate</span><b>467 Hz</b></div>
              <div><span>Enroll Samples</span><b>10 / User</b></div>
              <div><span>Duration</span><b>1.5s</b></div>
            </div>
          </div>
        </div>
      </section>

      <section id="architecture" class="section-block">
        <div class="section-heading">
          <span>Architecture</span>
          <h2>系统架构与认证流程</h2>
          <p>从前端 HCR 数据提交，到 Django API 入库，再到 Python 算法模块完成特征提取和身份判定。</p>
        </div>
        <div class="pipeline-grid">
          <article v-for="(step, index) in pipeline" :key="step.title" class="pipeline-card">
            <span>0{{ index + 1 }}</span>
            <h3>{{ step.title }}</h3>
            <p>{{ step.desc }}</p>
          </article>
        </div>
      </section>

      <section id="api" class="section-block api-section">
        <div class="section-heading">
          <span>API System</span>
          <h2>Django REST API 接口体系</h2>
          <p>前端通过统一 API 客户端与后端通信，支持 Bearer Token 配置和跨域联调。</p>
        </div>
        <div class="api-grid">
          <article v-for="item in apiList" :key="item.path" class="api-card">
            <b>{{ item.method }}</b>
            <h3>{{ item.path }}</h3>
            <p>{{ item.desc }}</p>
          </article>
        </div>
      </section>

      <section id="metrics" class="section-block metrics-section">
        <div class="section-heading">
          <span>Metrics</span>
          <h2>实验指标与系统运行态势</h2>
          <p>展示采样率影响、抗攻击测试，以及从后端读取的运行时用户、样本和认证会话统计。</p>
        </div>
        <div class="metrics-layout">
          <div class="glass-card large">
            <div class="card-title-row">
              <h3>采样率与认证表现</h3>
              <button class="ghost-mini" @click="loadRuntimeMetrics">刷新指标</button>
            </div>
            <div ref="lineChart" class="chart"></div>
          </div>
          <div class="glass-card">
            <h3>抗攻击 FAR</h3>
            <div ref="barChart" class="chart small"></div>
          </div>
          <div class="glass-card runtime-card">
            <h3>运行时指标</h3>
            <div class="runtime-grid">
              <div v-for="item in runtimeCards" :key="item.label">
                <span>{{ item.label }}</span>
                <strong>{{ item.value }}</strong>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="install" class="section-block install-section">
        <div class="section-heading">
          <span>Quick Start</span>
          <h2>本地运行命令</h2>
        </div>
        <div class="command-grid">
          <div class="command-card">
            <b>后端</b>
            <code>cd backend && python manage.py migrate && python manage.py runserver</code>
          </div>
          <div class="command-card">
            <b>前端</b>
            <code>npm install && npm run dev</code>
          </div>
          <div class="command-card">
            <b>演示数据</b>
            <code>python algorithms/scripts/demo_auth.py</code>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue';
import * as echarts from 'echarts';
import { Cpu, DataAnalysis, Headset, Lock, Monitor } from '@element-plus/icons-vue';
import { ElMessage } from 'element-plus';
import { enrollUser, getHealth, getMetrics, verifyUser } from './services/api';
import { buildEnrollmentSignals, synthesizeHcrSignal } from './utils/signal';

const lineChart = ref(null);
const barChart = ref(null);
const signalChart = ref(null);
const lineInstance = ref(null);
const barInstance = ref(null);
const signalInstance = ref(null);

const subjectId = ref('demo-user');
const displayName = ref('演示用户');
const deviceModel = ref('Bone Conduction Earphone');
const verifyMode = ref('genuine');
const loading = ref(false);
const backendOnline = ref(false);
const healthStatus = ref('尚未连接后端，请先启动 Django 服务。');
const resultText = ref('暂无认证结果');
const lastAccepted = ref(null);
const lastScore = ref('--');
const lastThreshold = ref('--');
const lastLatency = ref('--');
const runtimeMetrics = ref({ subjects: 0, samples: 0, sessions: 0, acceptance_rate: 0 });

const scorePercent = computed(() => {
  const score = Number(lastScore.value);
  if (Number.isNaN(score)) return 0;
  return Math.round(score * 100);
});

const latestDecision = computed(() => {
  if (lastAccepted.value === true) return 'Authenticated';
  if (lastAccepted.value === false) return 'Rejected';
  return backendOnline.value ? 'Ready' : 'Disconnected';
});

const runtimeCards = computed(() => [
  { label: '用户数', value: runtimeMetrics.value.subjects ?? 0 },
  { label: 'HCR 样本', value: runtimeMetrics.value.samples ?? 0 },
  { label: '认证会话', value: runtimeMetrics.value.sessions ?? 0 },
  { label: '通过率', value: `${Math.round((runtimeMetrics.value.acceptance_rate ?? 0) * 100)}%` },
]);

const metrics = [
  { value: '96.55%', label: 'Balanced Accuracy', note: '作品书核心指标' },
  { value: '< 60ms', label: '认证延迟', note: '轻量推理链路' },
  { value: '10 samples', label: '注册样本', note: '每名用户模板生成' },
  { value: '467 Hz', label: '采样率', note: '低采样可用性验证' },
];

const pipeline = [
  { title: 'Chirp 激励', desc: '生成 50Hz-850Hz 扫频探测信号，触发头部接触响应。' },
  { title: 'HCR 数据入库', desc: '真实采集信号或前端演示信号通过 Django API 写入样本表。' },
  { title: 'MFCC 特征提取', desc: '完成滤波、频响估计、MFCC 与差分统计特征计算。' },
  { title: '身份判定', desc: '通过 Siamese / 模板距离得到认证分数和通过/拒绝结果。' },
];

const apiList = [
  { path: '/api/health/', method: 'GET', desc: '返回系统状态与核心模块信息' },
  { path: '/api/chirp-config/', method: 'GET', desc: '返回 Chirp 参数和探测样本' },
  { path: '/api/enroll/', method: 'POST', desc: '提交多段 HCR 信号，生成用户注册模板' },
  { path: '/api/verify/', method: 'POST', desc: '提交待验证 HCR 信号，返回认证分数与接受结果' },
  { path: '/api/metrics/', method: 'GET', desc: '返回论文指标和运行时认证指标' },
];

async function checkBackend() {
  loading.value = true;
  try {
    const response = await getHealth();
    backendOnline.value = true;
    healthStatus.value = `后端在线：${response.system} / ${response.status}\n核心模块：${response.core.join(' · ')}`;
    ElMessage.success('Django API 连接成功');
    await loadRuntimeMetrics(false);
  } catch (error) {
    backendOnline.value = false;
    healthStatus.value = `连接失败：${error.message}\n请确认 backend 服务已启动并允许跨域访问。`;
    ElMessage.error(`后端连接失败：${error.message}`);
  } finally {
    loading.value = false;
  }
}

async function handleEnroll() {
  loading.value = true;
  try {
    const signals = buildEnrollmentSignals(10, 10);
    updateSignalChart(signals[0], '注册 HCR 样本');
    const payload = await enrollUser({
      external_id: subjectId.value,
      display_name: displayName.value,
      device_model: deviceModel.value,
      sample_rate: 467,
      signals,
    });
    resultText.value = JSON.stringify(payload, null, 2);
    lastAccepted.value = null;
    ElMessage.success('注册成功，用户模板已生成');
    await loadRuntimeMetrics(false);
  } catch (error) {
    resultText.value = error.message;
    ElMessage.error(`注册失败：${error.message}`);
  } finally {
    loading.value = false;
  }
}

async function handleVerify() {
  loading.value = true;
  try {
    const seed = verifyMode.value === 'genuine' ? 12 : 99;
    const claimedSignal = synthesizeHcrSignal(seed);
    updateSignalChart(claimedSignal, verifyMode.value === 'genuine' ? '本人验证样本' : '攻击者验证样本');
    const payload = await verifyUser({
      external_id: subjectId.value,
      claimed_signal: claimedSignal,
      sample_rate: 467,
    });
    resultText.value = JSON.stringify(payload, null, 2);
    lastAccepted.value = payload.accepted;
    lastScore.value = Number(payload.score).toFixed(4);
    lastThreshold.value = Number(payload.threshold).toFixed(2);
    lastLatency.value = `${payload.latency_ms}ms`;
    ElMessage.success(payload.accepted ? '认证通过' : '认证拒绝');
    await loadRuntimeMetrics(false);
  } catch (error) {
    resultText.value = error.message;
    lastAccepted.value = false;
    ElMessage.error(`验证失败：${error.message}`);
  } finally {
    loading.value = false;
  }
}

async function loadRuntimeMetrics(showMessage = true) {
  try {
    const response = await getMetrics();
    runtimeMetrics.value = response.runtime_metrics || runtimeMetrics.value;
    if (showMessage) ElMessage.success('运行指标已刷新');
  } catch (error) {
    if (showMessage) ElMessage.error(`指标读取失败：${error.message}`);
  }
}

function updateSignalChart(signal, title = 'HCR Signal') {
  if (!signalInstance.value) return;
  signalInstance.value.setOption({
    title: { text: title, textStyle: { color: '#dbe7ff', fontSize: 13 }, left: 8, top: 4 },
    grid: { top: 42, right: 16, bottom: 24, left: 36 },
    xAxis: { type: 'category', show: false, data: signal.map((_, index) => index) },
    yAxis: { type: 'value', axisLabel: { color: '#8aa0c7' }, splitLine: { lineStyle: { color: 'rgba(255,255,255,0.08)' } } },
    series: [{ data: signal, type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 2, color: '#49d8ff' }, areaStyle: { color: 'rgba(73,216,255,0.16)' } }],
    tooltip: { trigger: 'axis' },
  });
}

function initCharts() {
  lineInstance.value = echarts.init(lineChart.value);
  lineInstance.value.setOption({
    grid: { top: 24, right: 18, bottom: 28, left: 40 },
    xAxis: { type: 'category', data: ['50', '100', '200', '300', '400', '467'], axisLabel: { color: '#dbe7ff' } },
    yAxis: { type: 'value', min: 70, max: 100, axisLabel: { color: '#dbe7ff' }, splitLine: { lineStyle: { color: 'rgba(255,255,255,0.08)' } } },
    series: [{ data: [75.49, 82.97, 86.95, 89.43, 91.35, 96.22], type: 'line', smooth: true, symbolSize: 8, lineStyle: { width: 4, color: '#49d8ff' }, itemStyle: { color: '#7c5cff' }, areaStyle: { color: 'rgba(73,216,255,0.18)' } }],
    tooltip: { trigger: 'axis' },
  });

  barInstance.value = echarts.init(barChart.value);
  barInstance.value.setOption({
    grid: { top: 18, right: 12, bottom: 24, left: 34 },
    xAxis: { type: 'category', data: ['BMI', 'BFR', 'SMR'], axisLabel: { color: '#dbe7ff' } },
    yAxis: { type: 'value', axisLabel: { color: '#dbe7ff' }, splitLine: { lineStyle: { color: 'rgba(255,255,255,0.08)' } } },
    series: [{ data: [0.32, 0.08, 1.92], type: 'bar', barWidth: 28, itemStyle: { borderRadius: [8, 8, 0, 0], color: '#49d8ff' } }],
    tooltip: { trigger: 'axis' },
  });

  signalInstance.value = echarts.init(signalChart.value);
  updateSignalChart(synthesizeHcrSignal(12), 'HCR 信号预览');
}

onMounted(() => {
  initCharts();
  checkBackend();
  window.addEventListener('resize', () => {
    lineInstance.value?.resize();
    barInstance.value?.resize();
    signalInstance.value?.resize();
  });
});
</script>
