# 📐 Project Architecture — KTV Helper Smartwear Companion

## 1. File Structure

```
c:\Users\rumia\Desktop\9105a4\
├── index.html                    # 主文件（1396 行，纯 HTML/CSS/JS，无框架）
├── poster_page_1.png             # Page 1 渲染预览截图
├── appendix_page_2.png           # Page 2 渲染预览截图
├── .gitignore
│
├── assets/                       # 所有图片素材
│   ├── screen_1.png ~ screen_10.png   # 10 个高保真手表界面截图
│   ├── hand_sketches_ideation.png     # B.1 手绘概念草图（Week 8）
│   ├── hand_sketches_lofi.png         # B.2 纸质线框图（Week 9）
│   └── digital_lofi_wireflow.png      # B.3 数字低保真线框流（Week 10）
│
├── skills/
│   └── skill.md                  # frontend-design 设计规范
│
├── archive_split_bill/           # 旧版本归档（不再使用）
│   ├── index.html                # 旧版海报代码
│   ├── *.pdf / *.docx / *.fig    # 原始参考文件
│   └── ...
│
├── Final Yingtai Yan.pdf         # 原始 Figma 导出高保真设计稿
└── A4_Smartwatch.pdf             # Demo 参考 PDF（奥运垃圾回收主题，仅参考排版）
```

## 2. HTML 架构（index.html）

```
<body>
  <div class="workspace">                    # 1280px 居中容器

    <!-- 交互工具栏 -->
    <div class="interactive-utility-bar">     # 毛玻璃主题切换面板
      [Classic Cream] [Exhibition Dark]
    </div>

    <!-- PAGE 1: 主海报 (1190×1684px A4) -->
    <div class="a4-page" id="page-poster">
      .page-header-line                       # 顶部课程标识横条
      .poster-header                          # 标题 + 课程信息（2:1 Grid）

      .grid-row-1                             # 第一横排（1.62fr : 1.38fr）
        ├── 01 Design Solution                # 方案描述 + 手表截图 + 环境约束
        └── 02 Deepened Design Pain Points    # 4 个痛苦点卡片

      .grid-row-2                             # 第二横排（1.62fr : 1.38fr）
        ├── 03 Iterations & Reflections       # 3 轮迭代时间线 + 2 个评估面板
        └── 04 Key Visual Checkpoints         # 4 个功能检查点 + 传感器说明

      .wireflow-section                       # 05 Wireflow Journey（6 步通栏）
      .footer-note                            # 页脚
    </div>

    <!-- PAGE 2: 附录 (1190×1684px A4) -->
    <div class="a4-page" id="page-appendix">
      .page-header-line
      .poster-header

      Section A: 10-Screen Interface Set      # 5×2 网格，10 个手表界面
      Section B: Hand-Drawn Sketches          # 3 列草图卡片
      Section C: Usability Heuristic Table    # 4 行启发式评估表格

      .appendix-bottom-grid                   # 3 列底部面板
        ├── Consultation Meeting Logs
        ├── Interactive Prototypes (Figma)
        └── Academic References
      .footer-note
    </div>

  </div>
  <script> setTheme() </script>               # 明暗主题切换逻辑
</body>
```

## 3. CSS Design System

| Token | Value | 用途 |
|-------|-------|------|
| `--bg-workspace` | `#EAE5DE` | 外层暖灰画廊背景 |
| `--page-bg` | `#FAF8F5` | A4 页面奶油白底 |
| `--card-bg` | `#FFFFFF` | 卡片纯白底 |
| `--card-border` | `#E8E2D9` | 卡片暖色边框 |
| `--text-main` | `#24292E` | 深炭灰主文字 |
| `--text-muted` | `#656E75` | 柔和灰色辅助文字 |
| `--accent-rust` | `#BE5C4A` | 赤陶色强调 |
| `--accent-rust-light` | `#FBF4F2` | 赤陶色浅底 |
| `--transition-smooth` | `all 0.5s cubic-bezier(0.16, 1, 0.3, 1)` | 统一贝塞尔过渡 |

**字体体系：**
- **标题**：`Playfair Display` 900 weight，衬线，斜体数字编号
- **正文**：`Plus Jakarta Sans` 300–800，无衬线
- **标签/元数据**：`Outfit` 700，大写字母间距

## 4. 交互特性

| 特性 | 实现方式 |
|------|----------|
| 明暗主题切换 | `body.theme-dark` CSS 类切换，所有变量覆盖 |
| 纸质颗粒肌理 | `body::before` SVG fractalNoise 伪元素 |
| 卡片悬浮抬升 | `translateY(-4px)` + `box-shadow` 扩散 |
| 手表屏幕高光 | `::after` 伪元素 `linear-gradient` 扫过效果 |
| 页面入场动画 | `@keyframes fadeInUp` + `animation-delay` 错开 |
| 呼吸灯 | `.pulse-dot` `@keyframes pulseGlow` |

## 5. 已知待优化区域

1. **Page 1 底部空白**：Section 05 Wireflow 上方约有 50–80px 空白间距
2. **Page 2 Heuristic Table 下方空白**：表格到 bottom-grid 之间约 60px 空白
3. **暗色主题细节**：部分内联样式的颜色未响应主题变量
4. **Page 2 底部三栏**：高度不完全等齐
5. **图片分辨率**：screen_*.png 为裁剪后的界面截图，边缘可能有轻微锯齿
