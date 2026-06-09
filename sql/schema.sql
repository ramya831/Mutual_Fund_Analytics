CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT,

    scheme_name TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    benchmark TEXT,

    expense_ratio_pct REAL,

    risk_category TEXT

);


CREATE TABLE dim_date (

    date TEXT PRIMARY KEY,

    year INTEGER,

    month INTEGER,

    quarter INTEGER

);


CREATE TABLE fact_nav (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    date TEXT,

    nav REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)

);


CREATE TABLE fact_transactions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    investor_id TEXT,

    amfi_code INTEGER,

    transaction_date TEXT,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    city_tier TEXT,

    age_group TEXT,

    gender TEXT,

    kyc_status TEXT,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)

);


CREATE TABLE fact_performance (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    return_1yr REAL,

    return_3yr REAL,

    return_5yr REAL,

    expense_ratio REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)

);


CREATE TABLE fact_aum (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_house TEXT,

    year INTEGER,

    aum_value REAL

);