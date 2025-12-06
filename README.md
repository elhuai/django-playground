# Django Playground 🎯

一個使用 Django 5.2 構建的部落格系統，採用日系暖色系 UI 設計，實現完整的文章管理功能。

## ✨ 功能特色

- 📝 **文章管理系統** - 完整的 CRUD 功能
- 👤 **作者管理** - 管理部落格作者資訊
- 🏷️ **標籤系統** - 文章分類與標籤功能
- 🎨 **日系暖色系設計** - 簡約優雅的 UI 介面
- 📱 **響應式設計** - 支援各種裝置瀏覽
- 🔐 **後台管理** - Django Admin 完整功能

## 🛠️ 技術架構

### 後端技術
- **Django 5.2.8** - Python Web 框架
- **SQLite** - 輕量級資料庫
- **Django Extensions** - 開發工具擴充

### 前端技術
- **Bootstrap 5** - UI 框架
- **Bootstrap Icons** - 圖示系統
- **自訂 CSS** - 日系暖色系主題

### 開發工具
- **UV** - Python 套件管理工具
- **djlint** - Django 模板格式化工具
- **IPython** - 互動式 Python Shell

## 📋 系統需求

- Python >= 3.13
- UV 套件管理工具

## 🚀 快速開始

### 1. 安裝相依套件

```bash
uv sync
```

### 2. 資料庫遷移

```bash
uv run manage.py migrate
```

### 3. 建立超級使用者

```bash
uv run manage.py createsuperuser
```

### 4. 啟動開發伺服器

```bash
uv run manage.py runserver
```

訪問 http://127.0.0.1:8000/ 即可瀏覽網站

## 📂 專案結構

```
django-playground/
├── blog/                   # 部落格應用
│   ├── models.py          # 資料模型 (Article, Author, Tag)
│   ├── views.py           # 視圖邏輯
│   ├── urls.py            # URL 路由
│   └── templates/         # 模板檔案
├── core/                   # 專案核心設定
│   ├── settings.py        # Django 設定
│   └── urls.py            # 主 URL 設定
├── practices/             # 練習應用
├── templates/             # 共用模板
│   ├── base.html          # 基礎模板
│   └── style.css          # 自訂樣式
└── static/                # 靜態檔案
```

## 🎨 設計特色

### 色彩配置
- 主色調：溫暖米色 (#FAF3E0)
- 強調色：柔和珊瑚色 (#E8AE9D)
- 導航欄：暖陶土色 (#eebcb0)
- 文字色：溫暖棕色 (#5D4E37)

### UI 特點
- 簡約的日系美學
- 柔和的陰影與圓角
- 流暢的懸停動畫效果
- 舒適的閱讀體驗

## 📱 主要頁面

- `/blog/articles/` - 文章列表
- `/blog/authors/` - 作者列表
- `/blog/tags/` - 標籤列表
- `/admin/` - 後台管理介面

## 🔧 開發指令

### 執行資料庫遷移
```bash
uv run manage.py makemigrations
uv run manage.py migrate
```

### 進入 Django Shell
```bash
uv run manage.py shell_plus
```

### 檢查程式碼格式
```bash
uv run djlint --reformat templates/
```

## 📝 資料模型

### Article (文章)
- 標題、內容
- 發布狀態
- 作者關聯
- 多對多標籤

### Author (作者)
- 姓名、Email
- 個人簡介
- 建立時間

### Tag (標籤)
- 標籤名稱
- 唯一性約束

---

# Django Playground 🎯

A blog system built with Django 5.2, featuring a Japanese-inspired warm color UI design and complete article management functionality.

## ✨ Features

- 📝 **Article Management** - Full CRUD functionality
- 👤 **Author Management** - Manage blog author information
- 🏷️ **Tag System** - Article categorization and tagging
- 🎨 **Japanese Warm Color Design** - Simple and elegant UI
- 📱 **Responsive Design** - Support for various devices
- 🔐 **Admin Panel** - Full Django Admin functionality

## 🛠️ Tech Stack

### Backend
- **Django 5.2.8** - Python Web Framework
- **SQLite** - Lightweight Database
- **Django Extensions** - Development Tools

### Frontend
- **Bootstrap 5** - UI Framework
- **Bootstrap Icons** - Icon System
- **Custom CSS** - Japanese Warm Color Theme

### Development Tools
- **UV** - Python Package Manager
- **djlint** - Django Template Formatter
- **IPython** - Interactive Python Shell

## 📋 Requirements

- Python >= 3.13
- UV Package Manager

## 🚀 Quick Start

### 1. Install Dependencies

```bash
uv sync
```

### 2. Database Migration

```bash
uv run manage.py migrate
```

### 3. Create Superuser

```bash
uv run manage.py createsuperuser
```

### 4. Run Development Server

```bash
uv run manage.py runserver
```

Visit http://127.0.0.1:8000/ to browse the website

## 📂 Project Structure

```
django-playground/
├── blog/                   # Blog Application
│   ├── models.py          # Data Models (Article, Author, Tag)
│   ├── views.py           # View Logic
│   ├── urls.py            # URL Routing
│   └── templates/         # Template Files
├── core/                   # Project Core Settings
│   ├── settings.py        # Django Settings
│   └── urls.py            # Main URL Configuration
├── practices/             # Practice Application
├── templates/             # Shared Templates
│   ├── base.html          # Base Template
│   └── style.css          # Custom Styles
└── static/                # Static Files
```

## 🎨 Design Features

### Color Scheme
- Primary: Warm Cream (#FAF3E0)
- Accent: Soft Coral (#E8AE9D)
- Navbar: Warm Terracotta (#eebcb0)
- Text: Warm Brown (#5D4E37)

### UI Highlights
- Minimalist Japanese aesthetics
- Soft shadows and rounded corners
- Smooth hover animations
- Comfortable reading experience

## 📱 Main Pages

- `/blog/articles/` - Article List
- `/blog/authors/` - Author List
- `/blog/tags/` - Tag List
- `/admin/` - Admin Panel

## 🔧 Development Commands

### Database Migration
```bash
uv run manage.py makemigrations
uv run manage.py migrate
```

### Django Shell
```bash
uv run manage.py shell_plus
```

### Code Formatting
```bash
uv run djlint --reformat templates/
```

## 📝 Data Models

### Article
- Title, Content
- Publication Status
- Author Relationship
- Many-to-Many Tags

### Author
- Name, Email
- Biography
- Created At

### Tag
- Tag Name
- Unique Constraint
