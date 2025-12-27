#!/usr/bin/env python3
"""
Data Analysis Script - Analyzes customer data and generates reports

This script demonstrates basic data processing using the datalib library.
It loads customer data, validates it, and generates summary reports.
"""

import sys
import os
from pathlib import Path

# Add src to Python path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from datalib import DataProcessor, DataValidator, DataFormatter


def analyze_customer_data(data_file: str) -> dict:
    """
    Analyze customer data and return summary statistics
    
    Args:
        data_file (str): Path to the customer data file
        
    Returns:
        dict: Analysis results
    """
    # Initialize components
    processor = DataProcessor()
    validator = DataValidator()
    formatter = DataFormatter()
    
    print(f"🔍 Loading data from {data_file}...")
    
    try:
        # Load data based on file extension
        if data_file.endswith('.json'):
            raw_data = processor.load_json_file(data_file)
            # Convert to list format for consistent processing
            data = raw_data if isinstance(raw_data, list) else [raw_data]
        elif data_file.endswith('.csv'):
            data = processor.load_csv_file(data_file)
        else:
            raise ValueError("Unsupported file format. Please use JSON or CSV.")
        
        print(f"✅ Loaded {len(data)} records")
        
        # Define validation schema
        schema = {
            'required_fields': ['name', 'email', 'age'],
            'types': {
                'name': str,
                'email': str,
                'age': int
            }
        }
        
        # Validate data
        print("🔎 Validating data quality...")
        validation_results = validator.validate_dataset(data, schema)
        
        print(f"📊 Validation complete:")
        print(f"   - Valid records: {validation_results['valid_records']}")
        print(f"   - Invalid records: {validation_results['invalid_records']}")
        
        # Filter out invalid records for analysis
        valid_data = []
        for i, record in enumerate(data):
            # Check if this record has errors
            has_errors = any(error['record_index'] == i for error in validation_results['errors'])
            if not has_errors:
                valid_data.append(record)
        
        # Perform analysis on valid data
        if valid_data:
            print("📈 Performing analysis...")
            
            # Age group analysis
            age_groups = {}
            for record in valid_data:
                age = int(record['age'])
                if age < 25:
                    group = "18-24"
                elif age < 35:
                    group = "25-34"
                elif age < 50:
                    group = "35-49"
                else:
                    group = "50+"
                
                age_groups[group] = age_groups.get(group, 0) + 1
            
            # Generate summary report
            summary_report = formatter.create_summary_report(valid_data, "Customer Analysis Report")
            
            # Create results dictionary
            results = {
                'total_customers': len(data),
                'valid_customers': len(valid_data),
                'age_distribution': age_groups,
                'validation_results': validation_results,
                'summary_report': summary_report
            }
            
            return results
        
        else:
            print("❌ No valid data found for analysis")
            return {'error': 'No valid data available'}
    
    except Exception as e:
        print(f"❌ Error during analysis: {str(e)}")
        return {'error': str(e)}


def main():
    """Main function to run the data analysis"""
    print("🚀 Customer Data Analysis Tool")
    print("=" * 50)
    
    # Default data file
    default_file = "data/customers.json"
    
    # Check if custom file provided
    if len(sys.argv) > 1:
        data_file = sys.argv[1]
    else:
        data_file = default_file
        print(f"📁 No file specified, using default: {data_file}")
    
    # Check if file exists
    if not Path(data_file).exists():
        print(f"❌ Error: File '{data_file}' not found")
        print("💡 Usage: python analyze_customers.py [data_file.json|data_file.csv]")
        sys.exit(1)
    
    # Run analysis
    results = analyze_customer_data(data_file)
    
    # Display results
    if 'error' in results:
        print(f"❌ Analysis failed: {results['error']}")
        sys.exit(1)
    
    print("\n📊 ANALYSIS RESULTS")
    print("=" * 50)
    print(f"Total customers: {results['total_customers']}")
    print(f"Valid customers: {results['valid_customers']}")
    print(f"Data quality: {(results['valid_customers'] / results['total_customers'] * 100):.1f}%")
    
    print("\n👥 Age Distribution:")
    for age_group, count in results['age_distribution'].items():
        percentage = (count / results['valid_customers'] * 100)
        print(f"   {age_group}: {count} customers ({percentage:.1f}%)")
    
    if results['validation_results']['errors']:
        print(f"\n⚠️  Found {len(results['validation_results']['errors'])} validation errors")
        print("   Run with verbose mode to see details")
    
    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    main()