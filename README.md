# StyleLoop HK - 智能虛擬衣櫥與永續時尚平台 👗🇭🇰

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Status](https://img.shields.io/badge/Status-Project_Planning-orange.svg)
![Platform](https://img.shields.io/badge/Platform-iOS%20%7C%20Android-lightgrey.svg)

## 1. 項目背景與願景 (Executive Summary)
**StyleLoop HK** 是一款針對香港都市生活量身打造的時尚科技 App。我們旨在解決香港用戶三大痛點：
* **居住空間狹窄**：衣櫃管理困難，閒置衣物堆積。
* **網購尺碼不合**：退貨成本高，尤其是歐美品牌與本地小眾品牌。
* **設計師缺乏渠道**：本地時裝系學生（PolyU/HKDI）的作品難以商業化。

我們透過 **AI 影像處理**與 **3D 體感掃描技術**，提供一站式「數位造型師」服務。

---

## 2. 核心功能模組 (Core Features)

### 🤖 AI 虛擬衣櫥 (Smart Stylist)
* **一鍵數位化**：AI 自動移除背景，將用戶衣物分類存檔。
* **氣候導向建議**：串接**香港天文台 API**，根據溫濕度提供穿搭建議（例如：今日「濕滯」，建議穿透氣材質）。
* **CP 值分析**：追蹤穿著次數，提醒清理閒置衣物。

### 📏 精確身型匹配 (Body Data Matching)
* **3D 體感掃描**：透過手機鏡頭提取身高、肩寬、腰圍等數據。
* **避雷穿搭指引**：針對梨形、倒三角等身型提供專屬建議。
* **虛擬試穿 (Digital Fitting Room)**：預測特定尺碼的貼合度（如：「此款 M 號腰部略緊」）。

### 🎓 設計師與學生孵化器 (Designer Hub)
* **FYP 預購轉化**：為本地時裝設計系畢業生提供預購專區，達到產量後由合作工廠生產。
* **風格克隆**：AI 學習設計師邏輯，指導用戶用舊衣穿出名家風格。

### ♻️ 永續循環市場 (Circular Eco-Market)
* **一鍵轉售**：直接調用虛擬衣櫥數據，免去重新拍照的煩惱。
* **租借模式**：支持高價設計師作品短租，增加學生設計師收入。

---

## 3. 技術架構 (Technical Roadmap)

### Phase 1: MVP 開發 (當前階段)
- [ ] 實現基於 **Rembg / DeepLabV3** 的 AI 自動去背功能。
- [ ] 建立基礎資料庫結構 (Firebase / MongoDB)。
- [ ] 手動身型數據錄入模組。

### Phase 2: AI 進階與社群
- [ ] 接入香港天文台 API 實現智能穿搭推薦。
- [ ] 開發 **Style-to-Earn** 推薦積分系統。

### Phase 3: 深度學習與 AR
- [ ] 研發基於 **MediaPipe** 的 3D 身型自動掃描。
- [ ] AR 虛擬試穿 (Virtual Try-on) 技術對接。

---

## 4. 商業模式 (Revenue Model)
1. **佣金分成 (10%-15%)**：每筆設計師作品或二手成交抽成。
2. **Style-to-Earn**：用戶分享穿搭帶貨可獲得現金返利。
3. **B2B 數據服務**：為小眾品牌提供去識別化的身型數據統計。
4. **Premium 訂閱**：無限衣櫥儲存空間與線下試衣特權。

---

## 5. 香港市場優化 (HK Specifics)
* **物流對接**：整合順豐、順便智能櫃。
* **空間方案**：與本地「迷你倉」服務商合作管理季末衣物。
* **粵語優化**：AI 建議支持廣東話語境。

---

## 🛠️ 開發環境 (Setup)
* **Frontend**: Flutter / React Native
* **Backend**: Node.js / Python (AWS Lambda)
* **AI Models**: TensorFlow / Amazon SageMaker
* **Database**: PostgreSQL / Firebase

---

## 📬 聯繫方式
如有任何建議或合作意向，歡迎提交 Issue 或透過 Instagram [@] 聯繫。
