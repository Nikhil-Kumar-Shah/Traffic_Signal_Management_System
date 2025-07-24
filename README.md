<!-- Header Banner: Typing SVG for animated effect -->
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=30&duration=4000&pause=1000&color=F97316&center=true&vCenter=true&width=800&lines=🚦+Welcome+to+My+GitHub+Profile!;👨‍💻+Developer+%7C+Learner+%7C+Creator;💡+Explore+Projects+and+Ideas!" alt="Typing Animation Banner" />
</p>



<h1 align="center">🚦 Traffic Signal Management System</h1>

<p align="center">
  <b>Python CLI for traffic signal data, powered by MySQL — modern, maintainable, and easy to use!</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/MySQL-8.0%2B-orange?logo=mysql" />
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg" />
</p>

---



## 🚦 Features

- 🔄 **Full CRUD:** Create, view, update, and delete signal records
- 📋 **Clean CLI menu:** Simple interactive interface for all actions
- 💾 **MySQL backend:** Safe, scalable storage for your signal data
- 🔒 **Input validation & error handling** for smooth use
- 🧱 **Modular, commented code** (see `.py` file)
- 💡 **Ready for web dashboard** (expandable with Flask, JS, and CSS)

---

## ⚡️ Quick Setup & Usage

### 1. Clone and Install Python Dependencies
```
pip install pymysql flask
```

### 2. MySQL Database Setup

Copy and run this in your MySQL client:

```
CREATE DATABASE IF NOT EXISTS traffic_db;
USE traffic_db;

CREATE TABLE IF NOT EXISTS TrafficData (
SignalID INT PRIMARY KEY,
VehicleCount INT NOT NULL,
SignalDuration INT NOT NULL,
Location VARCHAR(100) NOT NULL,
LastUpdated DATETIME NOT NULL
);
```

### 3. Run the Application (CLI)

```
python Traffic_Signal_Management_System.py
```
##
You’ll see a menu like:
```
Traffic Signal Management System
1. Ensure Signal Exists
2. Update Signal
3. View Signals
4. Delete Signal
5. Exit
```

---

## 👀 Signal Table Preview

| 🚦 SignalID | 🚗 VehicleCount | ⏰ Duration | 📍 Location           | 📝 LastUpdated           |
|:----------:|:--------------:|:----------:|:--------------------:|:-----------------------:|
| 1          | 12             | 60         | Main St & 5th Ave    | 2025-07-24 15:15:00     |
| 2          | 23             | 45         | MG Road & 11th Main  | 2025-07-24 16:30:45     |

---

## 🗂️ Project Structure

```
Traffic_Signal_Management_System/
├── README.md
├── Traffic_Signal_Management_System.py
└── SQL_Commands-Traffic_Signal_Management_System.txt
```

---


## 🤝 Contributing

Pull requests are welcome!  
<strong>How to contribute:</strong>
1. Fork this repo  
2. Create a branch: `git checkout -b feature/your-feature`  
3. Make changes
4. Commit: `git commit -m "Add feature"`
5. Push: `git push origin feature/your-feature`
6. Open a Pull Request 🚀

---

## 👤 Author

<p align="center">
  <a href="https://github.com/Nikhil-Kumar-Shah">
    <img src="https://github.com/user-attachments/assets/c857258e-ec0a-43c1-973a-4c8af874b0a3" width="90" style="border-radius: 50% " /><br>
    <b>Nikhil Kumar Shah</b>
  </a>
  <br>
  💻 Made with Python and passion
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red?style=flat-square" /> <br>
  <sub>© 2025 Nikhil Kumar Shah. All rights reserved.</sub>
</p>

---

<p align="center">
<b>Drive safe. Code smarter. 🚦</b>
</p>
