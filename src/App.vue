<template>
  <div class="site-shell">
    <header class="top-nav" :class="{ scrolled: navScrolled }">
      <div class="nav-brand">
        <div class="nav-logo">B</div>
        <div>
          <strong>骨振识息 BoneVibAuth</strong>
          <span>利用头部振动反馈的隐式身份验证系统</span>
        </div>
      </div>
      <div class="nav-right">
        <nav class="nav-links">
          <a href="#advantages">核心优势</a>
          <a href="#principles">技术原理</a>
          <a href="#performance">性能成果</a>
          <a href="#scenarios">应用场景</a>
        </nav>
        <div class="auth-actions">
          <button class="login-btn" type="button">登录</button>
          <button class="register-btn" type="button">注册</button>
        </div>
      </div>
    </header>

    <section class="hero-section">
      <div class="hero-bg-grid"></div>
      <div class="hero-bg-skull left"></div>
      <div class="hero-bg-skull right"></div>
      <div class="hero-waves wave-1"></div>
      <div class="hero-waves wave-2"></div>

      <div class="hero-content">
        <div class="hero-copy reveal">
          <span class="eyebrow">Next-Gen Bone-Conduction Identity Authentication</span>
          <h1>骨振识息 BoneVibAuth</h1>
          <h2>利用头部振动反馈的隐式身份验证系统 | 面向骨传导耳机的下一代生物识别认证</h2>
          <p class="hero-slogan">佩戴即认证，无感更安全，重新定义骨传导耳机的身份认证边界</p>
          <div class="hero-actions">
            <a class="primary-cta" href="#principles">查看核心技术原理</a>
            <a class="secondary-cta" href="#performance">浏览完整测试数据</a>
            <button class="secondary-cta demo-launch" type="button" @click="runAutoDemo">一键自动认证</button>
          </div>
        </div>

        <div class="hero-metrics">
          <article v-for="item in heroMetrics" :key="item.label" class="floating-metric reveal" :style="{ '--delay': item.delay + 's' }">
            <div class="metric-glow"></div>
            <strong>{{ item.value }}</strong>
            <span>{{ item.label }}</span>
          </article>
        </div>
      </div>
    </section>

    <main>
      <section id="advantages" class="content-section pain-solution-section reveal">
        <div class="section-heading">
          <span>Project Value</span>
          <h2>行业痛点与项目突破</h2>
          <p>以结构性矛盾切入，直接说明传统认证方案为何无法适配骨传导耳机，以及 BoneVibAuth 如何从根源重构身份认证逻辑。</p>
        </div>

        <div class="dual-panel">
          <div class="info-panel danger-panel">
            <div class="panel-head">
              <span class="panel-tag danger">行业痛点</span>
              <h3>传统认证方案，遇上骨传导耳机的三道结构性鸿沟</h3>
            </div>
            <div class="pain-grid">
              <article v-for="item in painPoints" :key="item.title" class="pain-card">
                <div class="icon danger">✕</div>
                <div>
                  <h4>{{ item.title }}</h4>
                  <p>{{ item.desc }}</p>
                </div>
              </article>
            </div>
          </div>

          <div class="info-panel success-panel">
            <div class="panel-head">
              <span class="panel-tag success">解决方案</span>
              <h3>骨振识息，专为骨传导耳机原生打造的认证方案</h3>
            </div>
            <div class="solution-visual">
              <div class="bone-head-outline">
                <div class="ear-device"></div>
                <div class="vibration-node n1"></div>
                <div class="vibration-node n2"></div>
                <div class="vibration-node n3"></div>
              </div>
              <div class="solution-copy">
                <p><strong>核心突破：</strong>基于头部接触响应 HCR，挖掘颅骨振动传播中的个体生物特征，从根源解决骨传导耳机认证难题。</p>
                <ul>
                  <li>头部阻抗特征建模</li>
                  <li>头部结构不对称特征建模</li>
                  <li>骨传导传播路径原生适配</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="principles" class="content-section reveal">
        <div class="section-heading">
          <span>Innovation</span>
          <h2>四大核心创新，打破行业技术天花板</h2>
          <p>以可视化卡片展示系统创新点，并通过 HCR 频谱对比示意直观呈现同人一致性与异人区分性。</p>
        </div>

        <div class="innovation-grid">
          <article v-for="card in innovationCards" :key="card.title" class="innovation-card">
            <div class="innovation-top">
              <div class="innovation-icon">{{ card.icon }}</div>
              <div>
                <span>{{ card.index }}</span>
                <h3>{{ card.title }}</h3>
              </div>
            </div>
            <p>{{ card.desc }}</p>
          </article>
        </div>

        <div class="spectrum-panel">
          <div class="panel-head inline">
            <div>
              <span class="panel-tag cyan">HCR 可视化</span>
              <h3>头部接触响应频谱对比</h3>
            </div>
            <div class="switch-group">
              <button :class="{ active: spectrumMode === 'same' }" @click="setSpectrum('same')">同一受试者样本</button>
              <button :class="{ active: spectrumMode === 'diff' }" @click="setSpectrum('diff')">不同受试者样本</button>
            </div>
          </div>
          <div ref="spectrumChart" class="chart large-chart"></div>
        </div>
      </section>

      <section class="content-section reveal">
        <div class="section-heading">
          <span>Pipeline</span>
          <h2>端到端全链路系统，从注册到认证一气呵成</h2>
          <p>从数据采集、预处理、特征提取到身份认证，全流程围绕低样本、低干扰、高安全的商用目标设计。</p>
        </div>

        <div class="flow-line">
          <article v-for="step in flowSteps" :key="step.title" class="flow-node">
            <div class="flow-index">{{ step.index }}</div>
            <h3>{{ step.title }}</h3>
            <p>{{ step.desc }}</p>
          </article>
        </div>

        <div class="preview-grid">
          <div class="preview-card">
            <div class="panel-head inline">
              <div>
                <span class="panel-tag">注册流程</span>
                <h3>客户端注册界面预览</h3>
              </div>
            </div>
            <div class="ui-mockup register-mockup">
              <div class="mockup-header-row">
                <div class="mockup-avatar">U</div>
                <div>
                  <strong>用户注册任务</strong>
                  <span>Subject ID：BVA-2026-001</span>
                </div>
              </div>
              <div class="mockup-form-grid">
                <div><span>采样率</span><b>467 Hz</b></div>
                <div><span>采集时长</span><b>15 s</b></div>
                <div><span>注册样本</span><b>{{ enrollFiles.filter(Boolean).length }} / 10</b></div>
                <div><span>设备状态</span><b>已连接</b></div>
              </div>
              <div class="sample-uploader">
                <div class="sample-ring" :style="{ '--progress': enrollProgress + '%' }">
                  <strong>{{ enrollFiles.filter(Boolean).length }}</strong>
                  <span>/ 10</span>
                </div>
                <div class="sample-control">
                  <label class="upload-main-btn">
                    批量上传注册样本
                    <input type="file" accept="audio/*" multiple @change="onEnrollBatchChange" />
                  </label>
                  <button class="ghost-demo-btn" type="button" @click="useDefaultEnrollSamples">使用默认样本</button>
                  <button class="ghost-demo-btn" type="button" @click="runEnrollAutoDemo">自动采集 10 组样本</button>
                  <div class="sample-chips">
                    <span v-for="idx in 10" :key="`chip-${idx}`" :class="{ active: enrollFiles[idx - 1] }">{{ idx }}</span>
                  </div>
                </div>
              </div>
              <div class="mockup-progress">
                <span>HCR 模板生成进度</span>
                <b>{{ enrollProgress }}%</b>
                <i :style="{ width: enrollProgress + '%' }"></i>
              </div>
              <p class="demo-hint">支持手动上传 10 个样本，也可以使用默认样本或一键完成注册采集流程。</p>
              <div class="mockup-bars enroll"></div>
            </div>
          </div>
          <div class="preview-card">
            <div class="panel-head inline">
              <div>
                <span class="panel-tag">认证流程</span>
                <h3>客户端认证界面预览</h3>
              </div>
            </div>
            <div class="ui-mockup auth-mockup">
              <div class="mockup-header-row">
                <div class="mockup-avatar" :class="{ success: authResult.pass }">{{ authResult.pass ? '✓' : '?' }}</div>
                <div>
                  <strong>身份认证任务</strong>
                  <span>Session：AUTH-2026-0506</span>
                </div>
              </div>
              <div class="auth-upload-row">
                <label class="upload-item wide">
                  <span>认证样本 A</span>
                  <input type="file" accept="audio/*" @change="authFileA = $event.target.files?.[0] || null" />
                </label>
                <label class="upload-item wide">
                  <span>认证样本 B</span>
                  <input type="file" accept="audio/*" @change="authFileB = $event.target.files?.[0] || null" />
                </label>
                <button class="ghost-demo-btn" type="button" @click="useDefaultAuthSamples">默认通过样本</button>
                <button class="auth-demo-btn" type="button" @click="runAuthDemo">开始认证分析</button>
                <button class="ghost-demo-btn full-row" type="button" @click="runAuthRejectDemo">默认攻击样本</button>
              </div>
              <p class="demo-hint">可选择默认通过样本展示合法用户认证结果，也可选择默认攻击样本展示非法样本拒绝结果。</p>
              <div class="mockup-result-box" :class="authResult.pass ? 'success' : 'danger'">
                <div><span>认证结果</span><b>{{ authResult.label }}</b></div>
                <div><span>得分 / 阈值</span><b>{{ authResult.score }} / {{ authResult.threshold }}</b></div>
                <div><span>响应耗时</span><b>{{ authResult.cost }}</b></div>
              </div>
              <div class="mockup-form-grid compact">
                <div><span>验证样本</span><b>双样本上传</b></div>
                <div><span>双通道状态</span><b>正常</b></div>
                <div><span>噪声抑制</span><b>已启用</b></div>
                <div><span>模板匹配</span><b>{{ authResult.pass ? '通过' : '未通过' }}</b></div>
              </div>
              <div class="mockup-bars auth"></div>
            </div>
          </div>
        </div>
      </section>

      <section id="performance" class="content-section reveal">
        <div class="section-heading">
          <span>Performance</span>
          <h2>全场景严苛测试，性能与安全性双重验证</h2>
          <p>核心性能、鲁棒性、安全性与时间一致性统一可视化，帮助评委快速捕捉可落地性和大赛竞争力。</p>
        </div>

        <div class="dashboard-grid">
          <div class="gauge-card" v-for="card in gaugeCards" :key="card.label">
            <div class="gauge-title">{{ card.label }}</div>
            <div class="gauge-value">{{ card.value }}</div>
            <div class="gauge-note">{{ card.note }}</div>
          </div>
        </div>

        <div class="charts-grid two-left">
          <div class="chart-card span-2">
            <div class="panel-head inline">
              <div>
                <span class="panel-tag cyan">鲁棒性雷达图</span>
                <h3>六大维度稳定性表现</h3>
              </div>
            </div>
            <div ref="radarChart" class="chart"></div>
          </div>
          <div class="chart-card">
            <div class="panel-head inline">
              <div>
                <span class="panel-tag">抗攻击能力</span>
                <h3>不同攻击方式 FAR 对比</h3>
              </div>
            </div>
            <div ref="attackChart" class="chart"></div>
          </div>
        </div>

        <div class="charts-grid equal-grid">
          <div class="chart-card">
            <div class="panel-head inline">
              <div>
                <span class="panel-tag">时间一致性</span>
                <h3>4 周到 14 个月准确率变化</h3>
              </div>
            </div>
            <div ref="timelineChart" class="chart"></div>
          </div>
          <div class="chart-card">
            <div class="panel-head inline">
              <div>
                <span class="panel-tag">实时认证状态</span>
                <h3>认证工作台结果概览</h3>
              </div>
            </div>
            <div class="result-console">
              <div class="console-status success">Authenticated</div>
              <div class="console-metrics">
                <div><span>平均认证准确率</span><strong>96.55%</strong></div>
                <div><span>单次响应耗时</span><strong>54ms</strong></div>
                <div><span>双通道平均准确率</span><strong>97.64%</strong></div>
                <div><span>盲目攻击 FAR</span><strong>≤4.88%</strong></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="scenarios" class="content-section reveal">
        <div class="section-heading">
          <span>Application</span>
          <h2>四大核心落地场景，覆盖全维度安全需求</h2>
          <p>聚焦信息安全、医疗健康、智能车载和移动支付，以沉浸式场景卡片强化技术落地想象力。</p>
        </div>

        <div class="scenario-grid">
          <article v-for="scene in scenarios" :key="scene.title" class="scenario-card" :style="{ '--accent': scene.accent }">
            <div class="scenario-overlay"></div>
            <span>{{ scene.tag }}</span>
            <h3>{{ scene.title }}</h3>
            <p>{{ scene.desc }}</p>
          </article>
        </div>
      </section>

      <section class="content-section reveal">
        <div class="section-heading">
          <span>Usability</span>
          <h2>用户真实验证，可用性与体验感双重认可</h2>
          <p>通过问卷评分和完整操作路径动画共同说明：系统不仅安全，还真正可用、可接受、可推广。</p>
        </div>

        <div class="user-study-grid">
          <div class="chart-card">
            <div class="panel-head inline">
              <div>
                <span class="panel-tag cyan">问卷评分</span>
                <h3>7 项用户研究均值</h3>
              </div>
            </div>
            <div ref="surveyChart" class="chart"></div>
          </div>

          <div class="journey-card">
            <div class="panel-head inline">
              <div>
                <span class="panel-tag">使用动线</span>
                <h3>注册 - 认证全流程</h3>
              </div>
            </div>
            <div class="journey-steps">
              <article v-for="item in journeySteps" :key="item.title">
                <div class="journey-dot"></div>
                <div>
                  <h4>{{ item.title }}</h4>
                  <p>{{ item.desc }}</p>
                </div>
              </article>
            </div>
          </div>
        </div>
      </section>
    </main>

    <footer class="page-footer reveal">
      <span class="footer-tag">中国大学生计算机设计大赛参赛作品</span>
      <h2>让佩戴耳机，成为最自然、最安全的身份证明</h2>
      <p>骨振识息 BoneVibAuth · 生物识别 · 骨传导 · 信息安全</p>
    </footer>
  </div>
</template>

<script setup>
import { nextTick, onBeforeUnmount, onMounted, ref } from 'vue';
import * as echarts from 'echarts';

const navScrolled = ref(false);
const spectrumMode = ref('same');

const enrollFiles = ref(Array(10).fill(null));
const enrollProgress = ref(0);
const authFileA = ref(null);
const authFileB = ref(null);
const authResult = ref({ label: '待认证', score: '--', threshold: '0.65', cost: '--', pass: false });

const heroMetrics = [
  { value: '96.55%', label: '平均认证准确率', delay: 0.1 },
  { value: '仅 15 秒', label: '10 个样本完成用户注册', delay: 0.2 },
  { value: '≤4.88%', label: '盲目攻击错误接受率 FAR', delay: 0.3 },
  { value: '54ms', label: '单次认证响应耗时', delay: 0.4 },
];

const painPoints = [
  { title: '开放佩戴失效', desc: '传统方案依赖封闭耳道反射回波，骨传导耳机不具备此类声学腔体。' },
  { title: '振动传导不兼容', desc: '现有认证方案依赖空气声传播，无法适配颅骨振动传输路径。' },
  { title: '注册成本过高', desc: '主流方案需要约 400 秒音频注册，严重影响落地实用性。' },
];

const innovationCards = [
  { index: '创新 01', icon: '◎', title: '隐式无感的身份认证机制', desc: '背景级运行，佩戴即认证，无需用户说话、咬合、滑动等任何主动操作，不打断正常使用流程。' },
  { index: '创新 02', icon: '◉', title: '双生物特征联合建模', desc: '系统性引入头部阻抗特征与头部结构不对称特征，刻画组织密度与几何形态差异。' },
  { index: '创新 03', icon: '≈', title: '低干扰智能探测信号设计', desc: '基于人耳听力曲线做 Chirp 扫频信号频域抑制，在舒适度与感知精度之间取得平衡。' },
  { index: '创新 04', icon: '∞', title: '小样本迁移学习架构', desc: '轻量级 Siamese 孪生网络结合迁移学习，仅需 10 个样本 / 15 秒完成用户建模。' },
];

const flowSteps = [
  { index: '01', title: '数据采集模块', desc: '骨传导耳机播放低干扰 Chirp 探测信号并采集头部接触响应 HCR。' },
  { index: '02', title: '数据预处理模块', desc: '完成滤波、归一化、频响估计和有效振动窗口提取。' },
  { index: '03', title: '特征提取模块', desc: '提取 MFCC、频响统计量、双生物特征描述向量。' },
  { index: '04', title: '身份认证模块', desc: '利用 Siamese 网络与模板更新策略完成注册、验证和长期优化。' },
];

const gaugeCards = [
  { label: '双通道平均准确率', value: '97.64%', note: '平均条件下稳定通过' },
  { label: 'FAR', value: '2.12%', note: '错误接受率' },
  { label: 'FRR', value: '2.91%', note: '错误拒绝率' },
  { label: 'EER', value: '3.46%', note: '交叉误拒率' },
];

const scenarios = [
  { tag: '信息安全', title: '政务 / 企业无感登录', desc: '面向政务系统、企业网络和终端设备，实现高安全、抗仿冒的无感认证。', accent: 'rgba(8,145,178,0.45)' },
  { tag: '医疗健康', title: '手术室与医疗终端授权', desc: '不干扰医患交流和临床协作，同时保障医疗数据和终端操作权限安全。', accent: 'rgba(5,150,105,0.42)' },
  { tag: '智能车载', title: '车主识别与无感解锁', desc: '适配车主身份识别、车辆无感解锁与启动，兼顾驾驶安全与使用便捷。', accent: 'rgba(124,58,237,0.42)' },
  { tag: '移动支付', title: '支付场景身份确认', desc: '面向支付确认场景提供极难仿冒的隐式认证能力，降低盗刷风险。', accent: 'rgba(37,99,235,0.42)' },
];

const journeySteps = [
  { title: '佩戴耳机与信号校准', desc: '用户佩戴骨传导耳机后，系统自动发起低干扰探测信号校准。' },
  { title: '15 秒完成用户注册', desc: '采集 10 个样本，自动提取 HCR 特征并建立个体认证模板。' },
  { title: '日常使用无感认证', desc: '用户在自然佩戴状态下即可完成身份确认，无需额外交互。' },
  { title: '长期模板更新优化', desc: '结合时间一致性评估与更新策略，持续保证长期认证稳定性。' },
];

const spectrumChart = ref(null);
const radarChart = ref(null);
const attackChart = ref(null);
const timelineChart = ref(null);
const surveyChart = ref(null);

let spectrumInstance;
let radarInstance;
let attackInstance;
let timelineInstance;
let surveyInstance;

const sameSpectrumA = [18, 24, 26, 30, 35, 42, 48, 50, 46, 41, 34, 29];
const sameSpectrumB = [16, 22, 27, 31, 36, 43, 49, 51, 45, 40, 35, 30];
const diffSpectrumA = [18, 24, 26, 30, 35, 42, 48, 50, 46, 41, 34, 29];
const diffSpectrumB = [8, 12, 18, 23, 28, 34, 29, 25, 21, 18, 14, 10];
const autoEnrollFiles = [
  'sample_01.wav', 'sample_02.wav', 'sample_03.wav', 'sample_04.wav', 'sample_05.wav',
  'sample_06.wav', 'sample_07.wav', 'sample_08.wav', 'sample_09.wav', 'sample_10.wav',
];
const authRejectFiles = [
  { name: 'auth_diff_a.wav', size: 61000 },
  { name: 'auth_diff_b.wav', size: 18000 },
];

const enrollSpectra = [
  [12, 16, 20, 24, 28, 34, 39, 41, 38, 34, 28, 22],
  [13, 17, 21, 25, 29, 35, 40, 42, 39, 35, 29, 23],
  [15, 20, 24, 28, 33, 39, 44, 46, 42, 38, 32, 26],
  [16, 21, 25, 29, 34, 40, 45, 47, 43, 39, 33, 27],
  [17, 22, 26, 31, 36, 42, 47, 49, 44, 40, 34, 28],
  [18, 23, 27, 32, 37, 43, 48, 50, 45, 41, 35, 29],
  [18, 24, 28, 33, 38, 44, 49, 51, 46, 42, 36, 30],
  [19, 24, 29, 34, 39, 45, 50, 52, 47, 43, 37, 31],
  [19, 25, 29, 35, 40, 46, 51, 53, 48, 44, 38, 31],
  [20, 26, 30, 36, 41, 47, 52, 54, 49, 45, 39, 32],
];

function buildSpectrumOption(mode) {
  const same = mode === 'same';
  return {
    backgroundColor: 'transparent',
    tooltip: { trigger: 'axis' },
    legend: {
      top: 6,
      textStyle: { color: '#9ab0d3' },
      data: same ? ['Sample A', 'Sample B'] : ['Subject A', 'Subject B'],
    },
    grid: { left: 40, right: 24, top: 46, bottom: 32 },
    xAxis: {
      type: 'category',
      data: ['50', '100', '150', '200', '250', '300', '350', '400', '500', '600', '700', '850'],
      axisLabel: { color: '#8fa6cc' },
      axisLine: { lineStyle: { color: 'rgba(124,151,197,0.25)' } },
    },
    yAxis: {
      type: 'value',
      axisLabel: { color: '#8fa6cc' },
      splitLine: { lineStyle: { color: 'rgba(124,151,197,0.12)' } },
    },
    series: [
      {
        name: same ? 'Sample A' : 'Subject A',
        type: 'line',
        smooth: true,
        symbol: 'none',
        lineStyle: { width: 3, color: '#22d3ee' },
        areaStyle: { color: 'rgba(34,211,238,0.12)' },
        data: same ? sameSpectrumA : diffSpectrumA,
      },
      {
        name: same ? 'Sample B' : 'Subject B',
        type: 'line',
        smooth: true,
        symbol: 'none',
        lineStyle: { width: 3, color: same ? '#34d399' : '#ef4444' },
        areaStyle: { color: same ? 'rgba(52,211,153,0.12)' : 'rgba(239,68,68,0.10)' },
        data: same ? sameSpectrumB : diffSpectrumB,
      },
    ],
  };
}

function initCharts() {
  spectrumInstance = echarts.init(spectrumChart.value);
  radarInstance = echarts.init(radarChart.value);
  attackInstance = echarts.init(attackChart.value);
  timelineInstance = echarts.init(timelineChart.value);
  surveyInstance = echarts.init(surveyChart.value);

  spectrumInstance.setOption(buildSpectrumOption(spectrumMode.value));

  radarInstance.setOption({
    tooltip: {},
    radar: {
      radius: '62%',
      splitNumber: 4,
      indicator: [
        { name: '设备兼容性', max: 100 },
        { name: '头部姿态适配', max: 100 },
        { name: '环境抗噪', max: 100 },
        { name: '佩戴位置容错', max: 100 },
        { name: '音量适配', max: 100 },
        { name: '采样率兼容', max: 100 },
      ],
      axisName: { color: '#a9bddf' },
      splitLine: { lineStyle: { color: 'rgba(124,151,197,0.18)' } },
      splitArea: { areaStyle: { color: ['rgba(13,27,48,0.16)', 'rgba(13,27,48,0.06)'] } },
      axisLine: { lineStyle: { color: 'rgba(124,151,197,0.18)' } },
    },
    series: [{
      type: 'radar',
      data: [{
        value: [94, 91, 90, 88, 92, 95],
        name: 'Robustness',
        areaStyle: { color: 'rgba(34,211,238,0.18)' },
        lineStyle: { color: '#22d3ee', width: 3 },
        itemStyle: { color: '#34d399' },
      }],
    }],
  });

  attackInstance.setOption({
    tooltip: { trigger: 'axis' },
    grid: { left: 46, right: 20, top: 28, bottom: 34 },
    xAxis: {
      type: 'category',
      data: ['盲目攻击', '随机冒充', '有知识冒充'],
      axisLabel: { color: '#9ab0d3' },
      axisLine: { lineStyle: { color: 'rgba(124,151,197,0.25)' } },
    },
    yAxis: {
      type: 'value',
      axisLabel: { color: '#9ab0d3', formatter: '{value}%' },
      splitLine: { lineStyle: { color: 'rgba(124,151,197,0.12)' } },
    },
    series: [{
      type: 'bar',
      barWidth: 34,
      data: [4.88, 2.12, 0.08],
      itemStyle: {
        borderRadius: [10, 10, 0, 0],
        color: params => ['#ef4444', '#f97316', '#22d3ee'][params.dataIndex],
      },
    }],
  });

  timelineInstance.setOption({
    tooltip: { trigger: 'axis' },
    grid: { left: 46, right: 22, top: 26, bottom: 34 },
    xAxis: {
      type: 'category',
      data: ['第 1 周', '第 2 周', '第 3 周', '第 4 周', '6 个月', '12 个月', '14 个月'],
      axisLabel: { color: '#9ab0d3' },
      axisLine: { lineStyle: { color: 'rgba(124,151,197,0.25)' } },
    },
    yAxis: {
      type: 'value',
      min: 88,
      max: 100,
      axisLabel: { color: '#9ab0d3', formatter: '{value}%' },
      splitLine: { lineStyle: { color: 'rgba(124,151,197,0.12)' } },
    },
    series: [
      {
        type: 'line',
        smooth: true,
        symbolSize: 7,
        data: [97.4, 97.2, 96.9, 96.7, 95.8, 94.9, 96.1],
        lineStyle: { width: 3, color: '#22d3ee' },
        itemStyle: { color: '#34d399' },
        areaStyle: { color: 'rgba(34,211,238,0.12)' },
      },
    ],
  });

  surveyInstance.setOption({
    tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
    grid: { left: 110, right: 24, top: 24, bottom: 26 },
    xAxis: {
      type: 'value',
      min: 0,
      max: 10,
      axisLabel: { color: '#9ab0d3' },
      splitLine: { lineStyle: { color: 'rgba(124,151,197,0.12)' } },
    },
    yAxis: {
      type: 'category',
      axisLabel: { color: '#c8d5ee' },
      data: ['系统易用性', '认证时间满意度', '信号低干扰', '使用意愿', '安全感知', '结果可信度', '学习成本'],
    },
    series: [{
      type: 'bar',
      barWidth: 16,
      data: [9.13, 9.08, 9.4, 8.22, 8.91, 8.88, 8.36],
      itemStyle: {
        borderRadius: 999,
        color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [
          { offset: 0, color: '#22d3ee' },
          { offset: 1, color: '#2563eb' },
        ]),
      },
    }],
  });
}

function setSpectrum(mode) {
  spectrumMode.value = mode;
  spectrumInstance?.setOption(buildSpectrumOption(mode), true);
}

function pseudoSpectrumFromFile(file, variant = 0) {
  const seed = (file?.name || '').split('').reduce((acc, ch) => acc + ch.charCodeAt(0), 0) + Math.floor((file?.size || 0) / 2048) + variant * 17;
  return Array.from({ length: 12 }, (_, i) => {
    const base = 14 + i * 2.2;
    const wave = Math.sin((seed + i * 11) * 0.07) * 7 + Math.cos((seed + i * 3) * 0.05) * 3;
    return Math.max(6, Math.round(base + wave));
  });
}

function updateEnrollPreview() {
  const uploadedCount = enrollFiles.value.filter(Boolean).length;
  enrollProgress.value = Math.min(100, Math.round((uploadedCount / 10) * 100));

  const latest = [...enrollFiles.value].reverse().find(Boolean);
  if (latest) {
    const latestSpectrum = pseudoSpectrumFromFile(latest, 1);
    spectrumInstance?.setOption({
      legend: { data: ['Template Ref', 'Latest Upload'] },
      series: [
        { name: 'Template Ref', data: sameSpectrumA },
        { name: 'Latest Upload', data: latestSpectrum },
      ],
    });
  }
}

function onEnrollBatchChange(event) {
  const files = Array.from(event.target.files || []).slice(0, 10);
  enrollFiles.value = Array.from({ length: 10 }, (_, index) => files[index] || null);
  updateEnrollPreview();
}

function useDefaultEnrollSamples() {
  enrollFiles.value = Array(10).fill(null);
  enrollProgress.value = 0;
  let current = 0;
  const timer = window.setInterval(() => {
    enrollFiles.value[current] = {
      name: autoEnrollFiles[current],
      size: 48000 + current * 1024,
    };
    updateEnrollPreview();
    current += 1;
    if (current >= 10) {
      window.clearInterval(timer);
      spectrumInstance?.setOption({
        legend: { data: ['Template Ref', 'Latest Upload'] },
        series: [
          { name: 'Template Ref', data: sameSpectrumA },
          { name: 'Latest Upload', data: sameSpectrumB },
        ],
      }, true);
    }
  }, 120);
}

function runEnrollAutoDemo() {
  enrollFiles.value = Array(10).fill(null);
  enrollProgress.value = 0;
  let current = 0;
  const timer = window.setInterval(() => {
    enrollFiles.value[current] = { name: autoEnrollFiles[current], size: 48000 + current * 1200 };
    updateEnrollPreview();
    current += 1;
    if (current >= 10) window.clearInterval(timer);
  }, 120);
}

function onEnrollFileChange(index, event) {
  const file = event.target.files?.[0] || null;
  enrollFiles.value[index] = file;
  updateEnrollPreview();
}

function useDefaultAuthSamples() {
  authFileA.value = { name: 'auth_same.wav', size: 52000 };
  authFileB.value = { name: 'auth_same_b.wav', size: 53000 };
  spectrumMode.value = 'same';
  spectrumInstance?.setOption({
    legend: { data: ['Auth Sample A', 'Auth Sample B'] },
    series: [
      { name: 'Auth Sample A', data: sameSpectrumA, lineStyle: { color: '#22d3ee' }, areaStyle: { color: 'rgba(34,211,238,0.12)' } },
      { name: 'Auth Sample B', data: sameSpectrumB, lineStyle: { color: '#34d399' }, areaStyle: { color: 'rgba(52,211,153,0.12)' } },
    ],
  }, true);
  authResult.value = {
    label: 'Authenticated',
    score: '0.9655',
    threshold: '0.65',
    cost: '54 ms',
    pass: true,
  };
}

function runAuthDemo() {
  if (!authFileA.value || !authFileB.value) {
    authResult.value = { label: '请先上传两段样本', score: '--', threshold: '0.65', cost: '--', pass: false };
    return;
  }

  const s1 = pseudoSpectrumFromFile(authFileA.value, 2);
  const s2 = pseudoSpectrumFromFile(authFileB.value, 3);
  const distance = s1.reduce((acc, v, i) => acc + Math.abs(v - s2[i]), 0) / s1.length;
  const score = Math.max(0, Math.min(1, 1 - distance / 30));
  const pass = score >= 0.65;

  spectrumMode.value = 'diff';
  spectrumInstance?.setOption({
    legend: { data: ['Auth Sample A', 'Auth Sample B'] },
    series: [
      { name: 'Auth Sample A', data: s1, lineStyle: { color: '#22d3ee' }, areaStyle: { color: 'rgba(34,211,238,0.12)' } },
      { name: 'Auth Sample B', data: s2, lineStyle: { color: pass ? '#34d399' : '#ef4444' }, areaStyle: { color: pass ? 'rgba(52,211,153,0.12)' : 'rgba(239,68,68,0.10)' } },
    ],
  });

  authResult.value = {
    label: pass ? 'Authenticated' : 'Rejected',
    score: score.toFixed(4),
    threshold: '0.65',
    cost: `${42 + Math.round(distance)} ms`,
    pass,
  };
}

function runAuthRejectDemo() {
  authFileA.value = authRejectFiles[0];
  authFileB.value = authRejectFiles[1];
  const s1 = diffSpectrumA;
  const s2 = diffSpectrumB;
  spectrumMode.value = 'diff';
  spectrumInstance?.setOption({
    legend: { data: ['Auth Sample A', 'Attack Sample B'] },
    series: [
      { name: 'Auth Sample A', data: s1, lineStyle: { color: '#22d3ee' }, areaStyle: { color: 'rgba(34,211,238,0.12)' } },
      { name: 'Attack Sample B', data: s2, lineStyle: { color: '#ef4444' }, areaStyle: { color: 'rgba(239,68,68,0.10)' } },
    ],
  }, true);
  authResult.value = {
    label: 'Rejected',
    score: '0.3184',
    threshold: '0.65',
    cost: '57 ms',
    pass: false,
  };
}

function runAutoDemo() {
  runEnrollAutoDemo();
  window.setTimeout(() => {
    useDefaultAuthSamples();
    runAuthDemo();
  }, 1350);
}

function handleScroll() {
  navScrolled.value = window.scrollY > 40;
}

function revealSections() {
  const items = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.14 }
  );

  items.forEach(item => observer.observe(item));
  return observer;
}

let revealObserver;

onMounted(async () => {
  await nextTick();
  initCharts();
  handleScroll();
  window.addEventListener('scroll', handleScroll);
  window.addEventListener('resize', () => {
    spectrumInstance?.resize();
    radarInstance?.resize();
    attackInstance?.resize();
    timelineInstance?.resize();
    surveyInstance?.resize();
  });
  revealObserver = revealSections();
});

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll);
  revealObserver?.disconnect();
  spectrumInstance?.dispose();
  radarInstance?.dispose();
  attackInstance?.dispose();
  timelineInstance?.dispose();
  surveyInstance?.dispose();
});
</script>
