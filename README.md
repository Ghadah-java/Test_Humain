# CSV Report Generator

A simple Python tool that reads CSV files and generates comprehensive data analysis reports.

## Features

- **Dataset Overview**: Total rows, columns, and memory usage
- **Column Details**: Data types, non-null counts, and missing value percentages
- **Numeric Statistics**: Mean, std, min, max, quartiles for numeric columns
- **Categorical Summary**: Unique values and most common values for text columns
- **Missing Values Analysis**: Detailed breakdown of missing data
- **Sample Data Preview**: First 5 rows of the dataset

## Requirements

- Python 3.6+
- pandas

Install pandas:
```bash
pip install pandas
```

## Usage

### Basic Usage
```bash
python csv_report_generator.py your_file.csv
```

### Save Report to File
```bash
python csv_report_generator.py your_file.csv report.txt
```

## Example

```bash
python csv_report_generator.py sales_data.csv sales_report.txt
```

This will:
1. Analyze the `sales_data.csv` file
2. Print the report to console
3. Save the report to `sales_report.txt`

## Sample Output

```
======================================================================
CSV DATA ANALYSIS REPORT
Generated: 2026-04-20 12:50:00
======================================================================

1. DATASET OVERVIEW
----------------------------------------
   Total Rows: 1000
   Total Columns: 5
   Memory Usage: 45.23 KB

2. COLUMN DETAILS
----------------------------------------
   • id
     Type: int64, Non-null: 1000, Missing: 0 (0.0%)
   • name
     Type: object, Non-null: 995, Missing: 5 (0.5%)
   ...

3. NUMERIC COLUMNS STATISTICS
----------------------------------------
       id        price    quantity
count  1000.0    1000.0    1000.0
mean   500.5     45.67     12.3
...
```

## License

MIT License
