# 🎯 JobTracker

一个基于 **Vue 3 + Vite + TailwindCSS + Flask + SQLite** 的全栈求职进程管理应用。  
可以方便地记录、查询和管理投递岗位的进度。

---

## ✨ 功能特性
- 🏢 记录公司、官网、岗位、投递状态、投递日期
- ➕ 支持新增、编辑、删除岗位记录
- 🎨 使用 TailwindCSS 美化页面
- 🔍 支持公司名称搜索 & 状态/日期筛选（待开发）
- 🗄️ 使用 Flask + SQLite 作为后端和数据库

---

## 🛠️ 技术栈
- **前端**：Vue 3 + Vite + TailwindCSS
- **后端**：Flask (Python)
- **数据库**：SQLite
- **接口通信**：Axios

---

## 🚀 启动项目

### 1. 克隆仓库
```bash
git clone https://github.com/Kindred471/JobTracker.git
cd JobTracker
# 进入后端目录（项目根目录就是 app.py）
python -m venv venv
source venv/bin/activate  # Windows 用 venv\Scripts\activate
pip install -r requirements.txt

# 初始化数据库
python app.py
后端服务默认运行在 http://127.0.0.1:5000


启动前端 (Vue)
cd frontend  
npm install
npm run dev
前端服务默认运行在 http://127.0.0.1:5173

📌 TODO

 增加搜索功能（按公司名）

 增加筛选功能（状态 / 日期）

 增加数据持久化交互优化

 部署上线（可能使用 Vercel + Render 或其他方案）
