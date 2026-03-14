USE olist_project;

SELECT 
COUNT(order_id) AS total_orders
FROM orders;

SELECT 
ROUND(SUM(payment_value),2) AS total_revenue
FROM payments;

SELECT 
ROUND(AVG(payment_value),2) AS avg_order_value
FROM payments;

SELECT 
DATE_FORMAT(order_purchase_timestamp,'%Y-%m') AS month,
COUNT(order_id) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;

SELECT
p.product_category_name,
ROUND(SUM(pay.payment_value),2) AS revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
JOIN payments pay
ON oi.order_id = pay.order_id
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 10;