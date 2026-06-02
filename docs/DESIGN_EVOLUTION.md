# 📜 Design Evolution History — KTV Helper Poster

## Git Commit Timeline

| # | Hash | Message | Key Changes |
|---|------|---------|-------------|
| 1 | `4f4af65` | initial commit | 从 `Final Yingtai Yan.pdf` 提取内容，构建初版 HTML 海报 |
| 2 | `fb03a54` | add rendering screenshots | 首次生成 poster_page_1.png / appendix_page_2.png |
| 3 | `b16b615` | rollback to 3-column layout | 回退到对称三栏布局（用户反馈非对称版有大片空白） |
| 4 | `335c3da` | optimize spacing, add metrics | 添加第 4 个痛苦点、SUS 评分数据、传感器集成说明、放大 Wireflow |
| 5 | `15d0db1` | premium asymmetric editorial | 重新设计为非对称双栏画报风格，但仍出现列高不平衡导致的空白 |
| 6 | `a299bf1` | balance with horizontal rows | **关键突破**：改用横向行隔离栅格（Row-Based Grid），彻底解决空白 |
| 7 | `e5f8358` | add frontend-design skill | 加载 frontend-design 设计规范文件 |
| 8 | `2b0d71d` | interactive utility bar | 添加毛玻璃工具栏、纸质肌理、hover 动效、明暗主题切换 |

## 关键设计决策记录

### 决策 1：从三栏到双栏

- **问题**：初始的对称三栏布局过于工整、呆板，用户反馈"太像之前做的另一个海报了"
- **方案**：改为非对称双栏（golden ratio 约 1.62:1.38），模仿高端杂志/画报排版
- **结果**：视觉层次感大幅提升，但引入了列高不平衡问题

### 决策 2：Row-Based Grid 解决空白

- **问题**：非对称双栏中，左栏只有 2 个小模块，右栏有大量卡片，导致左栏被拉长出现大片空白
- **方案**：将内容拆分为独立的 `.grid-row-1` 和 `.grid-row-2`，每行左右独立对齐
- **结果**：每行的两个模块高度自然匹配，空白彻底消除

### 决策 3：主题确认

- **问题**：最初误以为项目是单纯的"分账单应用"
- **确认**：通过分析 `Final Yingtai Yan.pdf` 的 10 个高保真界面，确认主题是 **KTV 助手智能手表伴侣**，分账只是 4 个功能之一
- **结果**：将标题、副标题、所有文案统一修正为 KTV Helper 主题

### 决策 4：Interactive Premium 层

- **触发**：用户加载了 `frontend-design` skill，要求应用该设计规范
- **实现**：
  - 纸质 fractalNoise 颗粒肌理
  - 毛玻璃（backdrop-filter）交互工具栏
  - 贝塞尔曲线 hover 动效
  - CSS-only 明暗主题切换
  - staggered fadeInUp 入场动画

## 用户反复强调的核心要求

1. **不要大片空白** — 这是整个迭代过程中被提及最多次的问题
2. **不要和之前的海报太像** — 需要在排版风格上有明确区分
3. **视觉要高端、精致** — 画报级审美，不要简单的MVP
4. **内容要准确** — 主题是 KTV 智能手表，不是单纯的分账
