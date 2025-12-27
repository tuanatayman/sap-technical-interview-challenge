#!/usr/bin/env python3
"""
Report Generator Script - Generates formatted reports from processed data

This script takes analysis results and generates various output formats
including JSON, CSV, and formatted text reports.
"""

import sys
import os
import json
from pathlib import Path
from datetime import datetime

# Add src to Python path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from datalib import DataProcessor, DataValidator, DataFormatter


def generate_sales_report(data_file: str, output_format: str = "json") -> str:
    """
    Generate a sales report from transaction data
    
    Args:
        data_file (str): Path to the sales data file
        output_format (str): Output format (json, csv, txt)
        
    Returns:
        str: Path to the generated report file
    """
    # Initialize components
    processor = DataProcessor()
    formatter = DataFormatter("reports")
    
    print(f"📋 Generating sales report from {data_file}...")
    
    try:
        # Load data
        if data_file.endswith('.json'):
            raw_data = processor.load_json_file(data_file)
            data = raw_data if isinstance(raw_data, list) else [raw_data]
        elif data_file.endswith('.csv'):
            data = processor.load_csv_file(data_file)
        else:
            raise ValueError("Unsupported file format. Please use JSON or CSV.")
        
        print(f"📊 Processing {len(data)} transactions...")
        
        # Calculate sales metrics
        total_sales = 0
        sales_by_category = {}
        sales_by_month = {}
        
        for record in data:
            # Parse sales amount
            amount = float(record.get('amount', 0))
            total_sales += amount
            
            # Group by category
            category = record.get('category', 'Unknown')
            sales_by_category[category] = sales_by_category.get(category, 0) + amount
            
            # Group by month (assuming date field exists)
            date_str = record.get('date', '2024-01-01')
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                month_key = date_obj.strftime('%Y-%m')
                sales_by_month[month_key] = sales_by_month.get(month_key, 0) + amount
            except ValueError:
                # If date parsing fails, skip monthly grouping for this record
                pass
        
        # Create report data
        report_data = {
            'report_generated': datetime.now().isoformat(),
            'summary': {
                'total_transactions': len(data),
                'total_sales': total_sales,
                'average_transaction': total_sales / len(data) if data else 0
            },
            'sales_by_category': sales_by_category,
            'sales_by_month': sales_by_month
        }
        
        # Format currency values
        report_data['summary']['total_sales_formatted'] = formatter.format_currency(total_sales)
        report_data['summary']['average_transaction_formatted'] = formatter.format_currency(
            report_data['summary']['average_transaction']
        )
        
        # Generate output based on format
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if output_format.lower() == "json":
            output_file = f"sales_report_{timestamp}.json"
            formatter.to_json(report_data, output_file)
            
        elif output_format.lower() == "csv":
            # Convert to tabular format for CSV
            csv_data = []
            for category, amount in sales_by_category.items():
                csv_data.append({
                    'category': category,
                    'total_sales': amount,
                    'formatted_amount': formatter.format_currency(amount)
                })
            
            output_file = f"sales_report_{timestamp}.csv"
            formatter.to_csv(csv_data, output_file)
            
        elif output_format.lower() == "txt":
            # Create formatted text report
            text_report = create_text_report(report_data, formatter)
            output_file = f"sales_report_{timestamp}.txt"
            output_path = Path("reports") / output_file
            output_path.parent.mkdir(exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text_report)
        
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
        
        print(f"✅ Report generated: reports/{output_file}")
        return f"reports/{output_file}"
        
    except Exception as e:
        print(f"❌ Error generating report: {str(e)}")
        raise


def create_text_report(report_data: dict, formatter: DataFormatter) -> str:
    """Create a formatted text report"""
    
    lines = []
    lines.append("SALES REPORT")
    lines.append("=" * 50)
    lines.append(f"Generated: {report_data['report_generated']}")
    lines.append("")
    
    # Summary section
    summary = report_data['summary']
    lines.append("SUMMARY")
    lines.append("-" * 20)
    lines.append(f"Total Transactions: {summary['total_transactions']:,}")
    lines.append(f"Total Sales: {summary['total_sales_formatted']}")
    lines.append(f"Average Transaction: {summary['average_transaction_formatted']}")
    lines.append("")
    
    # Sales by category
    lines.append("SALES BY CATEGORY")
    lines.append("-" * 20)
    for category, amount in report_data['sales_by_category'].items():
        percentage = (amount / summary['total_sales'] * 100) if summary['total_sales'] > 0 else 0
        lines.append(f"{category}: {formatter.format_currency(amount)} ({percentage:.1f}%)")
    lines.append("")
    
    # Monthly sales (if available)
    if report_data['sales_by_month']:
        lines.append("MONTHLY SALES")
        lines.append("-" * 20)
        for month, amount in sorted(report_data['sales_by_month'].items()):
            lines.append(f"{month}: {formatter.format_currency(amount)}")
    
    return "\n".join(lines)


def main():
    """Main function to run the report generator"""
    print("📈 Sales Report Generator")
    print("=" * 50)
    
    # Parse command line arguments
    if len(sys.argv) < 2:
        print("💡 Usage: python generate_report.py <data_file> [output_format]")
        print("   Output formats: json, csv, txt (default: json)")
        sys.exit(1)
    
    data_file = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else "json"
    
    # Validate inputs
    if not Path(data_file).exists():
        print(f"❌ Error: File '{data_file}' not found")
        sys.exit(1)
    
    if output_format.lower() not in ["json", "csv", "txt"]:
        print(f"❌ Error: Unsupported output format '{output_format}'")
        print("   Supported formats: json, csv, txt")
        sys.exit(1)
    
    try:
        # Generate report
        output_path = generate_sales_report(data_file, output_format)
        print(f"\n✅ Report successfully generated: {output_path}")
        
    except Exception as e:
        print(f"❌ Report generation failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()