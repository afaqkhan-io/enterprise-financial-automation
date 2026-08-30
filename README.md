# 📊 Financial Report & Dashboard Generator

A Python data-processing project that generates a business transaction dataset, calculates financial KPIs with Pandas, and produces a formatted Excel dashboard with summaries and charts.

`Python 3.x` · `Pandas` · `NumPy` · `OpenPyXL` · `MIT License`

## 🚀 Features

- **Transaction data generation:** Creates a sample 1,500-row transaction ledger for demonstration.
- **Financial analytics:** Calculates revenue, discounts, costs, profit, margins, and monthly performance metrics.
- **Excel dashboard:** Builds a formatted workbook with KPI sections, tables, number formats, and charts.
- **Separated workflow:** Data generation, analytics, and report generation are kept in separate modules.

## 🧩 Project Structure

- `data_pipeline.py` — creates the sample transaction dataset.
- `analytics_engine.py` — performs KPI and performance calculations.
- `main.py` — generates the Excel report.
- `raw_sales_ledger.csv` — sample input ledger.
- `Corporate_Financial_Dashboard.xlsx` — generated/sample dashboard output.

## 📋 Setup

```bash
git clone https://github.com/afaqkhan-io/enterprise-financial-automation.git
cd enterprise-financial-automation
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install pandas openpyxl numpy
```

## ▶️ Run

```bash
python main.py
```

Then open `Corporate_Financial_Dashboard.xlsx` in Excel or another compatible spreadsheet application.

> **Note:** All transaction figures are sample/demo data and are not real company financial records.

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.
