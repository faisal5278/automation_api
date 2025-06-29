# 🧪 Process Automation Dashboard

A full-stack process automation system built with **FastAPI**, **SQLite**, and **Streamlit**. This project simulates internal QA tooling used in business process automation, embedded system test result tracking, and KPI reporting.

---

## 🚀 Features

🔧 **FastAPI Backend**  
- `POST /log_test_result` – Log new test results  
- `GET /get_all_results` – Retrieve all test records  
- `GET /get_summary` – View total, pass, and fail counts  
- `PUT /update_test_status/{id}` – Update result status  
- `GET /health` – API status check  

📊 **Streamlit Frontend**  
- Interactive form to submit test results  
- Live summary of passed/failed/total tests  
- Scrollable data table of all results  
- Form to update any existing test entry  
- Compact side-by-side layout (laptop-friendly)

🗃 **SQLite Database**  
- Stores test results persistently  
- Auto-creates table on first run  
- Easy to back up or export

---

## 🖼 Interface Preview

> 📸 Screenshot of full dashboard (no scrolling required):

![Dashboard Screenshot](screenshot.png) 

---

## 🛠 Technologies Used

| Layer     | Tech Stack                     |
|-----------|--------------------------------|
| Backend   | FastAPI, SQLite, Pydantic      |
| Frontend  | Streamlit, Requests            |
| Tools     | Python 3.13, Git, Swagger UI   |

---


## 🎯 Use Case
This project simulates a real-world internal QA system for tracking and optimizing automated tests — relevant for roles in:

- Process Automation

- Data Engineering / KPI Monitoring

- QA Tooling

- Embedded Testing

- DevOps Dashboards
"# automation_api" 
