# 📦 **Portfolio Projects Repository**
A collection of clean, end-to-end data analysis case studies focused on real-world problem solving using Python, SQL, EDA, statistics, and reporting.

---

# 🏷️ **Badges**
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Analysis-black)
![SQL](https://img.shields.io/badge/SQL-MySQL-orange)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboards-yellow)
![Status](https://img.shields.io/badge/Projects-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 🗂️ **Project Overview Table**

| Project | Domain | Goal | Skills Used | Report |
|--------|--------|------|-------------|--------|
| Olist E-commerce | Marketplace Analytics | Identify drivers of low review scores | Python, Pandas, EDA, Feature Engineering, Visualization | [View](https://www.notion.so/Reports-2b70c02bb1c7805cb0e1fe3a18fe5cb0?pvs=21) |
| Synthea Healthcare | Clinical Analytics | Understand patient readmission factors | Python, Pandas, SQL, Aggregation Pipelines, Visualization | [View](https://www.notion.so/Reports-2b70c02bb1c7800390f5f98b551a7e9c?pvs=21) |
| OULAD Education | Learning Analytics | Identify dropout & disengagement patterns | Python, Pandas, MySQL, Feature Aggregation, Visualization, Statistics | [View](https://www.notion.so/Reports-2b70c02bb1c78081a929e39ca65b64dd?pvs=21) |

---

# 🔍 **1️⃣ Olist E-commerce Dataset — Review Score Impact Analysis**

<details>
<summary><strong>📌 Problem Summary</strong></summary>

Customer reviews directly influence seller visibility and revenue. Low scores often stem from delivery delays, unmet expectations, or category-specific issues.  
Goal: Analyze how **delivery delays, product category, payment method, and price range** correlate with review scores.

</details>

### ❓ **Key Question**  
**What leads to low review scores?**

### 🛠️ **Technologies / Skills**  
- Python, Pandas, NumPy  
- Exploratory Data Analysis  
- Feature Engineering (delivery delays, price buckets, volume metrics)  
- Data Visualization (Seaborn, Matplotlib)  
- Reporting & Insight Summaries  

👉 **[Read Full Report](https://www.notion.so/Reports-2b70c02bb1c7805cb0e1fe3a18fe5cb0?pvs=21)**

---

# 🏥 **2️⃣ Synthea Healthcare — Patient Readmission & Care Quality**

<details>
<summary><strong>📌 Problem Summary</strong></summary>

Hospitals face high load when patients are readmitted soon after discharge.  
Using encounters, conditions, procedures, and care plans, we identify **clinical patterns, chronic conditions, and treatment gaps** that contribute to early readmission.

</details>

### ❓ **Key Question**  
**Why do patients get readmitted?**

### 🛠️ **Technologies / Skills**  
- Python, Pandas  
- SQL-based validation  
- Data cleaning & merging across multi-table healthcare datasets  
- Care pathway analysis  
- Visualizing trends (conditions, procedures, medications)  
- Statistical reasoning  

👉 **[Read Full Report](https://www.notion.so/Reports-2b70c02bb1c7800390f5f98b551a7e9c?pvs=21)**

---

# 🎓 **3️⃣ OULAD — Student Dropout & Retention Analysis**

<details>
<summary><strong>📌 Problem Summary</strong></summary>

Many students register for courses but fail to complete them.  
This project analyzes **demographic differences, registration behavior, assessment trends, and online engagement** to identify dropout drivers.

</details>

### ❓ **Key Question**  
**Why do students drop out or stop engaging?**

### 🛠️ **Technologies / Skills**  
- Python, Pandas  
- MySQL (joins, aggregations, preprocessing)  
- Feature aggregation (per course, per student, per assessment)  
- EDA & visualization  
- Hypothesis testing & comparison metrics  
- Insight summarization  

👉 **[Read Full Report](https://www.notion.so/Reports-2b70c02bb1c78081a929e39ca65b64dd?pvs=21)**

### Folder Structure

olist review analysis/
    ├── data/
        ├── processed_data/
            └── readme.md
        └── raw_data/
            └── link_to_data.txt
    ├── logs/
        ├── logs.md
        └── olist_data_upload_logs.log
    ├── notebooks/
        ├── pandas_analysis.ipynb
        ├── sql_cleaning.ipynb
        └── sql_understanding.ipynb
    ├── outputs/
        └── summary.md
    ├── src/
        ├── functions.py
        ├── plots.py
        ├── stat_tests.py
        └── upload_data.py
    ├── README.md
    └── requirements.txt
oulad dropout analysis/
    ├── data/
        └── raw_data/
            └── link_to_data.txt
    ├── logs/
        ├── logs.md
        └── oulad_data_upload_logs.log
    ├── notebooks/
        ├── pandas_analysis.ipynb
        ├── sql_cleaning.ipynb
        └── sql_understanding.ipynb
    ├── outputs/
        └── summary.md
    ├── src/
        ├── functions.py
        ├── plots.py
        ├── stat_tests.py
        └── upload_data.py
    ├── README.md
    └── requirements.txt
synthea readmission analysis/
    ├── data/
        └── raw_data/
            ├── allergies.csv
            ├── careplans.csv
            ├── conditions.csv
            ├── devices.csv
            ├── encounters.csv
            ├── imaging_studies.csv
            ├── immunizations.csv
            ├── medications.csv
            ├── observations.csv
            ├── organizations.csv
            ├── patients.csv
            ├── payer_transitions.csv
            ├── payers.csv
            ├── procedures.csv
            ├── providers.csv
            └── supplies.csv
    ├── logs/
        ├── logs.md
        └── synthea_data_uploads.log
    ├── notebooks/
        ├── pandas_analysis.ipynb
        ├── sql_cleaning.ipynb
        └── sql_understanding.ipynb
    ├── outputs/
        └── summary.md
    ├── src/
        ├── functions.py
        ├── plots.py
        ├── stat_tests.py
        └── upload_data.py
    ├── README.md
    └── requirements.txt
README.md