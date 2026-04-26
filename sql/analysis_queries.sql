-- 1. Total sales by region
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales
FROM orders_clean
GROUP BY region
ORDER BY total_sales DESC;

-- 2. Monthly revenue trend
SELECT
    order_year,
    order_month,
    ROUND(SUM(sales), 2) AS monthly_revenue
FROM orders_clean
GROUP BY order_year, order_month
ORDER BY order_year, order_month;

-- 3. Top 10 customers by sales
SELECT
    customer_id,
    ROUND(SUM(sales), 2) AS total_sales,
    COUNT(order_id) AS total_orders
FROM orders_clean
WHERE customer_id != 'Unknown'
GROUP BY customer_id
ORDER BY total_sales DESC
LIMIT 10;

-- 4. Top 10 products by revenue
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    SUM(quantity) AS total_quantity
FROM orders_clean
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;

-- 5. Total business summary
SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(SUM(sales), 2) AS total_revenue,
    SUM(quantity) AS total_units_sold
FROM orders_clean;