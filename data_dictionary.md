# Mutual Fund Analytics - Data Dictionary

## dim_fund

| Column | Type | Description |
|---|---|---|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Fund scheme name |
| category | Text | Equity/Debt/Hybrid category |
| sub_category | Text | Fund type |
| plan | Text | Direct/Regular plan |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Annual expense ratio |
| risk_category | Text | Fund risk level |


## fact_nav

| Column | Type | Description |
|---|---|---|
| amfi_code | Integer | Fund identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |


## fact_transactions

| Column | Type | Description |
|---|---|---|
| investor_id | Text | Investor identifier |
| transaction_date | Date | Transaction date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| kyc_status | Text | KYC verification status |


## fact_performance

| Column | Type | Description |
|---|---|---|
| amfi_code | Integer | Fund code |
| return_1yr | Float | One year return |
| return_3yr | Float | Three year return |
| return_5yr | Float | Five year return |
| expense_ratio | Float | Fund expense ratio |


## fact_aum

| Column | Type | Description |
|---|---|---|
| fund_house | Text | AMC name |
| year | Integer | Year |
| aum_value | Float | Assets under management |