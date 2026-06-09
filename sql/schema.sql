-- Create Fund Master Table

CREATE TABLE IF NOT EXISTS fund_master (

    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date TEXT,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount REAL,
    min_lumpsum_amount REAL,
    fund_manager TEXT,
    risk_category TEXT
);


-- Create NAV History Table

CREATE TABLE IF NOT EXISTS nav_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date TEXT,
    nav REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES fund_master(amfi_code)

);


-- Create AUM Table

CREATE TABLE IF NOT EXISTS aum (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    aum_value REAL,
    date TEXT

);


-- Create Benchmark Table

CREATE TABLE IF NOT EXISTS benchmark_indices (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    index_name TEXT,
    date TEXT,
    value REAL

);