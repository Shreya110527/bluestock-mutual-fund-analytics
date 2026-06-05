-- 1 Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav) FROM nav_history;

-- 3 Transactions by State
SELECT state, COUNT(*)
FROM investor_transactions
GROUP BY state;

-- 4 Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 5 Top Performing Funds
SELECT scheme_name, return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 6 Average SIP Inflow
SELECT AVG(sip_inflow_crore)
FROM monthly_sip_inflows;

-- 7 Risk Category Count
SELECT risk_grade, COUNT(*)
FROM scheme_performance
GROUP BY risk_grade;

-- 8 Fund House Wise Schemes
SELECT fund_house, COUNT(*)
FROM fund_master
GROUP BY fund_house;

-- 9 Top States by Transactions
SELECT state, SUM(amount_inr)
FROM investor_transactions
GROUP BY state
ORDER BY SUM(amount_inr) DESC;

-- 10 Category Wise Funds
SELECT category, COUNT(*)
FROM fund_master
GROUP BY category;