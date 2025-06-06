SELECT ROUND(SUM(Weekly_Sales),2) AS Total_Sales
FROM walmart_sales;

SELECT COUNT(DISTINCT Store) 
FROM walmart_sales;

SELECT ROUND(AVG(Weekly_Sales), 2) AS Avg_Weekly_Sales
FROM walmart_sales

SELECT ROUND(AVG(Store_Sales), 2) AS Avg_Store_Sales
FROM (
    SELECT Store, ROUND(SUM(Weekly_Sales), 2) AS Store_Sales
    FROM walmart_sales
    GROUP BY Store
) AS Store_Total_Sales;


SELECT Store, ROUND(SUM(Weekly_Sales),2) AS Store_Sales
FROM walmart_sales
GROUP BY Store
ORDER BY Store_Sales DESC;

SELECT 
    Date,
    ROUND(SUM(Weekly_Sales), 2) AS total_weekly_sales_bydate
FROM 
    walmart_sales
GROUP BY 
    Date
ORDER BY 
    total_weekly_sales_bydate DESC;

SELECT Holiday_Flag, ROUND(SUM(Weekly_Sales), 2) AS Total_Sales
FROM walmart_sales
GROUP BY Holiday_Flag;

SELECT Holiday_Flag, ROUND(AVG(Weekly_Sales), 2) AS Avg_Sales
FROM walmart_sales
GROUP BY Holiday_Flag;

SELECT Date, Store, Weekly_Sales 
FROM walmart_sales 
ORDER BY Weekly_Sales DESC LIMIT 5;

SELECT Fuel_Price, ROUND(AVG(Weekly_Sales), 2) AS Avg_Sales 
FROM walmart_sales 
GROUP BY Fuel_Price 
ORDER BY Fuel_Price;

SELECT 
  CASE 
    WHEN Temperature < 40 THEN 'Cold'
    WHEN Temperature BETWEEN 40 AND 70 THEN 'Moderate'
    ELSE 'Hot'
  END AS Temp_Range,
  ROUND(AVG(Weekly_Sales), 2) AS Avg_Sales
FROM walmart_sales
GROUP BY Temp_Range;

SELECT 
  CASE 
    WHEN Unemployment < 6 THEN 'Low'
    WHEN Unemployment BETWEEN 6 AND 8 THEN 'Medium'
    ELSE 'High'
  END AS Unemployment_Level,
  ROUND(AVG(Weekly_Sales), 2) AS Avg_Sales
FROM walmart_sales
GROUP BY Unemployment_Level;


