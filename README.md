# 📊 Enterprise Financial Report & Dashboard Generator

An advanced, production-grade Python automation data pipeline that ingests raw business transaction ledgers, executes complex financial analytical modeling, and outputs a client-ready, fully-formatted Excel Executive Dashboard complete with corporate branding, styling, data charts, and dynamic performance metrics.

<div>
  <strong>💻 Runtime:</strong> Python 3.8+ &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>📊 Framework:</strong> Pandas Dataframe &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>📄 License:</strong> MIT
</div>

## 💼 Core Architecture & Workflow
* **`raw_sales_ledger.csv`:** The baseline comma-separated ledger file serving as the ingested unstructured corporate record pool.
* **`data_pipeline.py`:** Simulates a high-volume enterprise data source by generating a realistic 1,500-row transaction ledger spanning 12 months with calculated costs, discounts, and revenue cohorts.
* **`analytics_engine.py`:** Acts as the analytical layer. Ingests raw data using pandas to process and compute complex core business KPIs, product portfolio margins, and Month-over-Month (MoM) growth matrices.
* **`main.py`:** The UI/Presentation layer. Translates the computed numerical data via openpyxl into a styled spreadsheet complete with dark navy executive grid views, customized fonts, number/currency formats, and dynamic automated column sizing.
* **`Corporate_Financial_Dashboard.xlsx`:** The final client-ready output sheet integrated with corporate styles and chart parameters.

## 🚀 Key Automation Features
* **Automated KPI Dashboarding:** Instantly structures gross system revenue, margins, operating net cash, and net profit summaries into standard executive presentation blocks.
* **Dynamic Visual Chart Injection:** Programmatically generates and embeds a professional clustered column bar chart mapping Monthly Net Revenue against Net Profits directly into the active spreadsheet.
* **Enterprise-Grade Styling:** Bypasses basic grid outputs using professional stylesheets (Zebra striping for readability, specialized borders, custom branding colors, and automatic cell column adjustments).
* **Decoupled Architecture:** Designed following industry-standard clean coding practices—separating data extraction, heavy statistical logic, and the UI generation layer.

## 📊 Sample System Output Preview
```text
--- EXECUTIVE SUMMARY CONSOLE PREVIEW ---
Total Corporate Revenue: \$7,741,201.50
Total Discounts Managed: \$3,844,510.35
Net Corporate Profit: \$3,896,691.15
Average System Operational Margin: 50.34%
```

## 🛠️ Tech Stack & Dependencies

| Component / Library | Purpose |
| :--- | :--- |
| **Python 3.8+** | Primary computational runtime engine |
| **Pandas** | High-performance enterprise data framework and multi-matrix grouping |
| **Openpyxl** | Programmatic Excel spreadsheet construction, styling engine, and chart injection |
| **Numpy** | Advanced mathematical functions and automated computational arrays |

## 📋 Prerequisites
Make sure to install the required data and spreadsheet processing dependencies before launching the pipeline:
```bash
pip install pandas openpyxl numpy
```

## 💻 Deployment & Execution
1. **Clone the project repository:**
   ```bash
   git clone https://github.com
   ```
2. **Navigate into the project directory:**
   ```bash
   cd enterprise-financial-automation
   ```
3. **Trigger the automated system pipeline:**
   ```bash
   python main.py
   ```
4. **Output Artifact:** Open the generated `Corporate_Financial_Dashboard.xlsx` spreadsheet file in Excel or Google Sheets to inspect the automated visual execution.

## 📄 License
Distributed under the **MIT License**. See `LICENSE` for more detailed legal terms.
