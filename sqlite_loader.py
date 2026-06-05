import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

files = {
    "fund_master": "data/processed/01_fund_master.csv",
    "nav_history": "data/processed/02_nav_history_cleaned.csv",
    "aum_by_fund_house": "data/processed/03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "data/processed/04_monthly_sip_inflows.csv",
    "category_inflows": "data/processed/05_category_inflows.csv",
    "industry_folio_count": "data/processed/06_industry_folio_count.csv",
    "scheme_performance": "data/processed/07_scheme_performance_cleaned.csv",
    "investor_transactions": "data/processed/08_investor_transactions_cleaned.csv",
    "portfolio_holdings": "data/processed/09_portfolio_holdings.csv",
    "benchmark_indices": "data/processed/10_benchmark_indices.csv"
}

for table_name, file_path in files.items():
    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded: {len(df)} rows")

print("\nDatabase Loaded Successfully!")