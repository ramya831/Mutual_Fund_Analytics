-- 1. Top 5 funds by AUM

SELECT 
fund_house,
aum_value
FROM fact_aum
ORDER BY aum_value DESC
LIMIT 5;


-- 2. Average NAV per month

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;


-- 3. Transaction count by state

SELECT
state,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;


-- 4. SIP total amount by year

SELECT
strftime('%Y', transaction_date) AS year,
SUM(amount_inr) AS total_sip
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year;


-- 5. Funds with expense ratio below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;


-- 6. Category wise funds

SELECT
category,
COUNT(*) AS total
FROM dim_fund
GROUP BY category;


-- 7. Highest NAV funds

SELECT
amfi_code,
MAX(nav) AS max_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY max_nav DESC;


-- 8. Investor city tier

SELECT
city_tier,
COUNT(*) 
FROM fact_transactions
GROUP BY city_tier;


-- 9. KYC status count

SELECT
kyc_status,
COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;


-- 10. Transaction type amount

SELECT
transaction_type,
SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;