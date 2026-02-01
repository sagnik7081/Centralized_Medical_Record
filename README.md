# 🩺 Centralized Medical Record Repository

<div align="center">

![Medical Records](https://img.shields.io/badge/Medical-Records-blue?style=for-the-badge&logo=heart&logoColor=white)
![React](https://img.shields.io/badge/React-18.3-61DAFB?style=for-the-badge&logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

**✨ A lightweight and modular web application for organizing, summarizing, and visualizing personal medical records ✨**

[🚀 Get Started](#-installation--setup) • [✨ Features](#-key-features) • [🧰 Tech Stack](#-tech-stack) • [👥 Contributors](#-contributors)

</div>

---

## 🎯 Overview

> 💡 Managing medical records can be messy and overwhelming. This application streamlines the process!

Upload your medical PDFs and watch the magic happen:

| Step | Action | Result |
|:----:|:------:|:------:|
| 📤 | **Upload** | Drop your PDF files |
| 🏷️ | **Categorize** | Auto-sorted by type |
| 🔍 | **Parse** | Extract key details |
| 📝 | **Summarize** | Plain language summaries |
| 📊 | **Visualize** | Interactive health trends |

🎯 **Goal**: Make medical information more accessible and meaningful to both patients and healthcare professionals.

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🔐 Security
- Secure user authentication
- Hashed password storage
- Protected data access

### 📁 File Management
- Upload medical PDFs
- Auto-categorization
- Organized storage

### 🧠 Smart Extraction
- Symptom detection
- Medicine identification
- Test outcome parsing

</td>
<td width="50%">

### 📝 Summaries
- Clean, readable format
- Plain language output
- Key highlights

### 📊 Visualization
- Interactive charts
- Health trend analysis
- Data insights

### ⚙️ Architecture
- Modular codebase
- Reusable components
- Easy to extend

</td>
</tr>
</table>

---

## 🧰 Tech Stack

<div align="center">

| Category | Technologies |
|:--------:|:------------:|
| ⚛️ **Frontend** | React • TypeScript • Vite |
| 🎨 **Styling** | Tailwind CSS • shadcn/ui |
| 📊 **Visualization** | Recharts |
| 🧭 **Routing** | React Router |
| 🔄 **State** | TanStack Query |
| 📦 **Build** | Vite • ESBuild |

</div>

---

## 📂 Project Structure

```
📁 centralized-medical-repo/
│
├── 📄 src/
│   ├── 🧩 components/      # Reusable UI components
│   │   └── ui/             # shadcn/ui components
│   ├── 📄 pages/           # Route pages
│   ├── 🎣 hooks/           # Custom React hooks
│   ├── 🛠️ lib/             # Utility functions
│   └── 🎨 index.css        # Global styles
│
├── 📁 public/              # Static assets
├── ⚙️ vite.config.ts       # Vite configuration
├── 🎨 tailwind.config.ts   # Tailwind configuration
└── 📦 package.json         # Dependencies
```

---

## 🛠️ Installation & Setup

### Prerequisites

> 📋 Make sure you have **Node.js** installed on your machine

### Quick Start

```bash
# 1️⃣ Clone the Repository
git clone <YOUR_GIT_URL>
cd <YOUR_PROJECT_NAME>

# 2️⃣ Install Dependencies
npm install

# 3️⃣ Start Development Server
npm run dev
```

### 🌐 Access the App

Once running, open your browser and navigate to:

```
🔗 http://localhost:5173
```

> ⚠️ **Important Note**: The patient's name and username should be the same.

---

## ⚠️ Known Challenges

| Challenge | Description |
|:---------:|:------------|
| 📄 **PDF Formatting** | Inconsistent formatting across different medical PDFs made parsing and data extraction challenging |
| 🔧 **Regex Logic** | Fine-tuning regex patterns for reliable data extraction required significant effort |
| 🔄 **Data Normalization** | Standardizing medical terminology across different sources |

---

## 📌 Future Improvements

- [ ] ☁️ Cloud storage integration for multi-device access
- [ ] 🔍 OCR support for image-based PDFs
- [ ] 👨‍⚕️ Multi-user dashboard for doctors and caregivers
- [ ] 📱 Mobile-responsive design improvements
- [ ] 🔔 Health reminder notifications
- [ ] 📤 Export to multiple formats (PDF, CSV, JSON)

---

## 🧑‍💻 Contributors

<div align="center">

| 👤 | Name | Role |
|:--:|:----:|:----:|
| 🧑‍💻 | **Sagnik Ghosh** | Developer |
| 🧑‍💻 | **Shantanu** | Developer |
| 🧑‍💻 | **Shaurya Pratap Singh** | Developer |
| 🧑‍💻 | **Vishal Singh** | Developer |

</div>

---

## 🤝 Contributing

Contributions are always welcome! 🎉

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

---

## 📄 License

<div align="center">

This project is open-source and available under the **MIT License** 📜

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

<sub>Made with ❤️ by the Medical Records Team</sub>

</div>
