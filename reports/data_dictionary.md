# Mutual Fund Analytics Data Dictionary

## fund_master
- amfi_code : Unique scheme identifier
- fund_house : Mutual fund company
- scheme_name : Scheme name
- category : Equity/Debt
- sub_category : Scheme category
- plan : Direct/Regular
- fund_manager : Fund manager
- risk_category : Risk level

## nav_history
- amfi_code : Scheme identifier
- date : NAV date
- nav : Net Asset Value

## investor_transactions
- investor_id : Unique investor
- transaction_date : Transaction date
- transaction_type : SIP/Lumpsum/Redemption
- amount_inr : Transaction amount

## scheme_performance
- return_1yr_pct : 1 Year Return
- return_3yr_pct : 3 Year Return
- return_5yr_pct : 5 Year Return
- alpha : Alpha value
- beta : Beta value
- sharpe_ratio : Sharpe Ratio

Source:
Provided Bluestock Mutual Fund Analytics datasets.