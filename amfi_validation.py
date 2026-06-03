import pandas as pd

fund_df = pd.read_csv("data/raw/01_fund_master.csv")
nav_df = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_df["amfi_code"])
nav_codes = set(nav_df["amfi_code"])

missing_codes = fund_codes - nav_codes

print("Total Fund Master Codes:", len(fund_codes))
print("Total NAV Codes:", len(nav_codes))
print("Missing Codes:", missing_codes)

if len(missing_codes) == 0:
    print("\nAll AMFI Codes are present in NAV History.")
else:
    print("\nSome codes are missing.")