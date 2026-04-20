#!/usr/bin/env python3
"""
CSV Report Generator
A tool to analyze CSV files and generate comprehensive reports.
"""

import pandas as pd
import sys
import os
from datetime import datetime


def load_csv(file_path):
    """Load CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def generate_report(df, output_file=None):
    """Generate a comprehensive report from the DataFrame."""
    report_lines = []
    
    # Header
    report_lines.append("=" * 70)
    report_lines.append("CSV DATA ANALYSIS REPORT")
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 70)
    report_lines.append("")
    
    # Basic Info
    report_lines.append("1. DATASET OVERVIEW")
    report_lines.append("-" * 40)
    report_lines.append(f"   Total Rows: {len(df)}")
    report_lines.append(f"   Total Columns: {len(df.columns)}")
    report_lines.append(f"   Memory Usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
    report_lines.append("")
    
    # Column Information
    report_lines.append("2. COLUMN DETAILS")
    report_lines.append("-" * 40)
    for col in df.columns:
        dtype = df[col].dtype
        non_null = df[col].count()
        null_count = df[col].isnull().sum()
        null_pct = (null_count / len(df)) * 100 if len(df) > 0 else 0
        report_lines.append(f"   • {col}")
        report_lines.append(f"     Type: {dtype}, Non-null: {non_null}, Missing: {null_count} ({null_pct:.1f}%)")
    report_lines.append("")
    
    # Statistical Summary for Numeric Columns
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if numeric_cols:
        report_lines.append("3. NUMERIC COLUMNS STATISTICS")
        report_lines.append("-" * 40)
        stats = df[numeric_cols].describe()
        report_lines.append(stats.to_string())
        report_lines.append("")
    
    # Categorical Columns Summary
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    if categorical_cols:
        report_lines.append("4. CATEGORICAL COLUMNS SUMMARY")
        report_lines.append("-" * 40)
        for col in categorical_cols:
            unique_count = df[col].nunique()
            top_value = df[col].mode().iloc[0] if not df[col].mode().empty else "N/A"
            top_freq = df[col].value_counts().iloc[0] if not df[col].value_counts().empty else 0
            report_lines.append(f"   • {col}")
            report_lines.append(f"     Unique values: {unique_count}")
            report_lines.append(f"     Most common: '{top_value}' (appears {top_freq} times)")
        report_lines.append("")
    
    # Missing Values Summary
    missing = df.isnull().sum()
    if missing.sum() > 0:
        report_lines.append("5. MISSING VALUES SUMMARY")
        report_lines.append("-" * 40)
        missing_cols = missing[missing > 0].sort_values(ascending=False)
        for col, count in missing_cols.items():
            pct = (count / len(df)) * 100
            report_lines.append(f"   • {col}: {count} missing ({pct:.1f}%)")
        report_lines.append("")
    else:
        report_lines.append("5. MISSING VALUES: None")
        report_lines.append("")
    
    # Sample Data
    report_lines.append("6. SAMPLE DATA (First 5 Rows)")
    report_lines.append("-" * 40)
    report_lines.append(df.head().to_string())
    report_lines.append("")
    
    # Footer
    report_lines.append("=" * 70)
    report_lines.append("END OF REPORT")
    report_lines.append("=" * 70)
    
    # Join all lines
    report = "\n".join(report_lines)
    
    # Print to console
    print(report)
    
    # Save to file if specified
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nReport saved to: {output_file}")
    
    return report


def main():
    """Main function to run the CSV report generator."""
    if len(sys.argv) < 2:
        print("Usage: python csv_report_generator.py <csv_file> [output_file]")
        print("\nArguments:")
        print("  csv_file     Path to the CSV file to analyze")
        print("  output_file  (Optional) Path to save the report")
        print("\nExample:")
        print("  python csv_report_generator.py data.csv report.txt")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Load and analyze
    print(f"Loading CSV file: {csv_file}\n")
    df = load_csv(csv_file)
    
    # Generate report
    generate_report(df, output_file)


if __name__ == "__main__":
    main()
