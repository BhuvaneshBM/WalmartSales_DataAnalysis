# 📊 Walmart Weekly Sales Analysis 2010-2012 (Tableau + SQL(PostgreSql) + Python)

"This project explores business insights by analyzing store performance, holiday trends, and external factors such as temperature, unemployment, and fuel prices."

---
## 🛠 Tools Used
- **SQL(PostgreSQL)** – data extraction, transformation, and efficient querying.
- **Python (pandas +SQLAlchemy + Prophet)** – data manipulation, query automation, Excel export, and time series forecasting.
- **Tableau** – Dashboard design and data storytelling.


---
## 🔍 Key Insights

### 📌 Overview
- 💰 **Total Sales**: \$6.74 billion
- 🏬 **Stores Analyzed**: 45
- 📆 **Avg Weekly Sales (All Stores)**: \$1.05 million 
- 🏪 **Avg Sales per Store**: \$149.71 million

---
## 🏬 Top Performing Stores
- Store 20 had the highest total sales: $301 million
- Other high performers:
- Store 4: $299M
- Store 14: $289M
- These stores consistently averaged over $2M/week in sales.

---
### 📅 Weekly Sales Trends
- Sales spike predictably in **November–December**, especially around **Black Friday and Christmas**
- **Top 6 highest sales weeks** include:
  - 24 December 2010 – \$80.9M
  - 23 December 2011 – \$76.9M

---
### 🧨 Holiday Impact
- Holiday weeks generated **7.5% of total sales**:
  - **Holiday weeks**: \$0.51B
  - **Non-holiday weeks**: \$6.23B
- **Per-store avg weekly sales**:
  - Holiday: \$1.12M  
  - Non-holiday: \$1.04M

---
### 🌡️ External Factors Influence

#### 🔥 Temperature
- **Moderate temps (40–70°F)** see slightly higher sales  
  - Moderate: \$1.07M
  - Cold: \$1.08M  
  - Hot: \$1.01M  

#### 📉 Unemployment
- Highest avg sales at **low unemployment levels**  
  - Low: \$1.18M  
  - High: \$1.00M

#### ⛽ Fuel Price
- Slight sales dip as **fuel price increases**
- Avg sales cluster around fuel price of \$2.5–\$3.5

- All queries used for business insights—covering store performance, holiday trends, and external factors like fuel prices are available in the Walmart.sql file.

---
## 📊 Dashboard Highlights

![dashboard1](output/Charts1.jpg)

![dashboard2](output/Charts2.jpg)


---
## 📈 Forecasting Future Sales


![Walmart Sales Forecast](output\actual_vs_forecast.jpg)

- Sales forecasts were generated using **Prophet**, projecting 24 future weeks based on trends, seasonality, and historical patterns. 
- Forecasts can be integrated into decision-making on staffing, inventory, and promotions.
