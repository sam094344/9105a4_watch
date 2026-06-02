# 📋 Content Inventory — KTV Helper Poster

> 海报中所有文案内容的完整清单，方便核对与修改。

---

## Page 1: 主海报

### Header
- **课程标识**：`IDEA9105 Academic Design Presentation` | `KTV Helper Smartwear Companion Poster`
- **标题**：KTV Helper: Smartwear Companion
- **副标题**：Wrist-Based Interaction Design for Real-Time Service Requests, Physiological Safeguards, and Split-Billing
- **课程信息**：Course: IDEA9105 Interaction Design / Project Code: 9105-SmartwearCompanion
- **学生信息**：Student Name: `（留空）` | Student ID: `（留空）`

### 01 Design Solution
- **主描述**：An elegant wrist-based watch companion designed specifically to bypass the auditory, cognitive, and physical challenges of high-decibel KTV entertainment environments.
- **补充描述**：Moving complex group setup and administrative friction off users' smartphones and onto a simplified, tactile wrist interface optimized for immediate, context-aware actions.
- **环境约束**：High-decibel environmental noise (>85dB), low-light conditions, cognitive/fine-motor distraction, and urgent transport/payment logistics at social event completion.
- **截图说明**：Physical Mock-up: Active Room 218 details, live song metadata, and quick action bubbles.
- **使用图片**：`screen_1.png`

### 02 Deepened Design Pain Points
- **描述**：Granular analysis outlining why standard mobile interfaces fail in high-energy social environments.
- **痛苦点 1**：**Auditory Overload & Isolation** — KTV rooms exceed 85–90 dB, rendering voice commands useless and drowning out standard audio alerts.
- **痛苦点 2**：**Cognitive & Fine-Motor Degradation** — Intoxication impairs motor coordination. Navigating nested phone menus or typing split amounts becomes a major hazard.
- **痛苦点 3**：**Physical Stress & Vitals** — High-energy singing combined with alcohol causes sudden cardiovascular spikes, frequently going unnoticed.
- **痛苦点 4**：**Chaotic Social Coordination** — Managing food orders and splitting checks while intoxicated generates social friction and delays.

### 03 Iterations & Reflections
- **描述**：Refining smartwatch screen dimensions and interaction models across development cycles.
- **Round 1: Grid** [Usability] — Replaced standard list rows with large, high-contrast tap bubbles in a symmetrical 2x2 grid to enable rapid muscle-memory selection.
- **Round 2: Alerts** [Efficiency] — Introduced intermediate confirmation screen states (Calling... / Sent!) to prevent accidental double-tap service triggers.
- **Round 3: Ride** [Safety] — Bypassed typing by auto-hailing to home coordinates with instant visual feedback of the incoming driver plate code.
- **Visual Design Consistency 面板**：Adopts a deep charcoal canvas background to support OLED energy conservation, paired with rich sunset red-orange gradients (`#E0533C` to `#11161B`) for warm room visuals and vibrant active blue triggers.
- **SUS 面板**：System Usability Scale (SUS) scores showed a significant increase from an initial **62.4** (Round 1) to a final **85.8** (Round 3), demonstrating substantial improvement in task completion rate.

### 04 Key Visual Checkpoints
- **① Tactile Room Service** — issues silent water requests to staff, confirming with a wrist haptic vibration.
- **② Physical Safety Net (Care+)** — Integrates PPG sensors to track heart rate spikes, prompting peer alerts.
- **③ Zero-Setup Safe Ride** — A single tap requests a cab to the user's home, displaying driver info.
- **④ Wrist-based Bill Split** — Displays clear personal shares directly on the wrist, synchronizing payments.
- **传感器说明**：Uses built-in **Optical PPG sensor** for heart rate tracking, **linear resonant actuator (LRA)** for haptic prompts, and **GPS** for safe dispatch.

### 05 Primary Wireflow Journey
- **描述**：Primary task flows showing navigation transitions: from the home page shortcut, category selection, vitals, active staff call, safe taxi tracking, to bill splitting.

| Step | Label | Description | Image |
|------|-------|-------------|-------|
| 1 | Home View | Active room & song status | screen_1.png |
| 2 | Service List | Select service category | screen_2.png |
| 3 | Vitals Check | Live heart rate sensor tracking | screen_3.png |
| 4 | Water Calling | 2-second hold cancellation state | screen_4.png |
| 5 | Ride Active | Taxi incoming plate code tracking | screen_7.png |
| 6 | Split Payment | Instant equal bill division summary | screen_9.png |

### Footer
- `KTV Helper Smartwear Companion Poster | Exhibition Layout`
- `Page 1 of 2 | Supporting Evidence Level: High`

---

## Page 2: 附录

### Header
- **课程标识**：`Supporting Appendix & Design Evidence` | `Split Mate Appendix Details`
- **标题**：KTV Helper: Smartwear Companion Appendix
- **副标题**：Supporting Evidence: High-Fidelity Interface Sets, Hand-Drawn Sketches, and Academic References
- **课程信息**：Course: IDEA9105 Interaction Design / Evidence Level: Comprehensive Academic Submission / Document Code: IDEA9105-A4-SMARTWEAR-APPENDIX

### Section A: Full 10-Screen Smartwatch Interface Set

| # | Label | Description | Image |
|---|-------|-------------|-------|
| 1 | Home View | Room, track, shortcuts. | screen_1.png |
| 2 | Service List | Health, Service, Ride options. | screen_2.png |
| 3 | Heart Rate | PPG sensor display. | screen_3.png |
| 4 | Call Water 1 | Intermediate calling state. | screen_4.png |
| 5 | Water Request | Staff confirmation alert. | screen_5.png |
| 6 | Hail Ride 1 | Taxi booking loader. | screen_6.png |
| 7 | Ride Arrived | Driver plate code. | screen_7.png |
| 8 | View Bill | Total room fees list. | screen_8.png |
| 9 | Settle Split | Equal split payment. | screen_9.png |
| 10 | Settings | Vibration & toggles. | screen_10.png |

### Section B: Hand-Drawn Sketches & Low-Fidelity Wireflows
- **B.1 Ideation Sketches (Week 8)** — Pencil concepts mapping round watch target sizing and circular button bubble trials. → `hand_sketches_ideation.png`
- **B.2 Paper Wireframes (Week 9)** — Sketched rectangular casing dimensions, cancel delay rings, and swipe target outlines. → `hand_sketches_lofi.png`
- **B.3 Digital Lo-Fi Flow (Week 10)** — Figma grey-box interactive wireflow tracing the primary watch assistant journey paths. → `digital_lofi_wireflow.png`

### Section C: Usability Review & Heuristic Reflections

| Heuristic Category | Watch Friction Point | Design Correction |
|----|----|----|
| Visibility of System Status | Lack of audio feedback in loud rooms | Full-screen status + **long-vibration tactile haptic pulse** |
| Error Prevention | Fine-motor degraded by alcohol | **2-second touch-and-hold delay buffer** |
| Match System & Real World | Complex banking labels | Simplified to **"Total Amount", "You Pay", "Equal Split"** |
| Flexibility & Efficiency | Nested pages require tedious swipes | Persistent **top-left escape route** + crown-press shortcuts |

### Bottom Grid
- **Consultation Meeting Logs**：Week 8 Review + Week 11 Evaluation
- **Interactive Prototypes**：Figma 链接 `https://www.figma.com/proto/UAzEmNfMZdeTrRSIGjmM0f/Final-Yingtai-Yan?node-id=102-39&scaling=scale-down&starting-point-node-id=102%3A39`
- **Academic References**：Batchu (2020), Ogbanufe & Gerhart (2020), Nielsen (1994)

### Footer
- `KTV Helper Smartwear Companion Appendix | Prepared for Grade Verification`
- `Page 2 of 2 | Supporting Evidence Density: Max`
