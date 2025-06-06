from sqlalchemy import create_engine
import pandas as pd

# Connect to PostgreSQL
db_engine = create_engine("postgresql://postgres:password@localhost:5433/postgres")

# Define queries
queries = {
    "Total_Sales": "SELECT ROUND(SUM(Weekly_Sales),2) AS Total_Sales FROM walmart_sales;",
    "Sales_by_Store": "SELECT Store, ROUND(SUM(Weekly_Sales),2) AS Store_Sales FROM walmart_sales GROUP BY Store ORDER BY Store_Sales DESC;",
    "Total_Weekly_Sales": "SELECT Date, ROUND(SUM(Weekly_Sales),2) AS Weekly_Sales FROM walmart_sales GROUP BY Date;",
    "Avg_Weekly_Sales": "SELECT ROUND(AVG(Weekly_Sales), 2) AS Avg_Weekly_Sales FROM walmart_sales;",
    "Avg_Sales_Holiday": "SELECT Holiday_Flag, ROUND(AVG(Weekly_Sales), 2) AS Avg_Sales FROM walmart_sales GROUP BY Holiday_Flag;",
    "Top_5_Sales": "SELECT Date, Store, Weekly_Sales FROM walmart_sales ORDER BY Weekly_Sales DESC LIMIT 5;",
    "Avg_Sales_Fuel": "SELECT Fuel_Price, ROUND(AVG(Weekly_Sales), 2) AS Avg_Sales FROM walmart_sales GROUP BY Fuel_Price ORDER BY Fuel_Price;",
    "Avg_Sales_Temp": """
        SELECT 
            CASE 
                WHEN Temperature < 40 THEN 'Cold'
                WHEN Temperature BETWEEN 40 AND 70 THEN 'Moderate'
                ELSE 'Hot'
            END AS Temp_Range,
            ROUND(AVG(Weekly_Sales), 2) AS Avg_Sales
        FROM walmart_sales
        GROUP BY Temp_Range;""",
    "Avg_Sales_Unempl": """ 
        SELECT 
            CASE 
                WHEN Unemployment < 6 THEN 'Low'
                WHEN Unemployment BETWEEN 6 AND 8 THEN 'Medium'
                ELSE 'High'
            END AS Unemployment_Level,
            ROUND(AVG(Weekly_Sales), 2) AS Avg_Sales
        FROM walmart_sales
        GROUP BY Unemployment_Level;"""
}

# Export SQL queries results to Excel 
with pd.ExcelWriter("Walmart_SQL_Analysis.xlsx", engine="openpyxl") as writer:
    for sheet_name, query in queries.items():
        df = pd.read_sql(query, db_engine)
        df.to_excel(writer, sheet_name=sheet_name, index=False)
