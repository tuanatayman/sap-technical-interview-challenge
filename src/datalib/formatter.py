"""
Data formatting utilities for converting data between different formats
"""

import json
import csv
from typing import List, Dict, Any, Optional
from pathlib import Path


class DataFormatter:
    """
    A class for formatting and converting data between different formats
    """
    
    def __init__(self, output_dir: str = "output"):
        """Initialize the DataFormatter"""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def format_currency(self, amount: float, currency: str = "USD", decimal_places: int = 2) -> str:
        """
        Format a number as currency
        
        Args:
            amount (float): Amount to format
            currency (str): Currency symbol or code
            decimal_places (int): Number of decimal places
            
        Returns:
            str: Formatted currency string
        """
        return f"{currency} {amount:,.{decimal_places}f}"
    
    def format_percentage(self, value: float, decimal_places: int = 1) -> str:
        """
        Format a decimal value as percentage
        
        Args:
            value (float): Decimal value (e.g., 0.25 for 25%)
            decimal_places (int): Number of decimal places
            
        Returns:
            str: Formatted percentage string
        """
        percentage = value * 100
        return f"{percentage:.{decimal_places}f}%"
    
    def to_json(self, data: Any, file_path: Optional[str] = None, indent: int = 2) -> str:
        """
        Convert data to JSON format
        
        Args:
            data (Any): Data to convert
            file_path (Optional[str]): If provided, save to file
            indent (int): JSON indentation
            
        Returns:
            str: JSON string
        """
        json_string = json.dumps(data, indent=indent, ensure_ascii=False)
        
        if file_path:
            output_path = self.output_dir / file_path
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(json_string)
        
        return json_string
    
    def to_csv(self, data: List[Dict[str, Any]], file_path: str, 
              fieldnames: Optional[List[str]] = None) -> str:
        """
        Convert list of dictionaries to CSV format
        
        Args:
            data (List[Dict[str, Any]]): Data to convert
            file_path (str): Output file path
            fieldnames (Optional[List[str]]): CSV column names
            
        Returns:
            str: Path to the created CSV file
        """
        if not data:
            raise ValueError("Cannot create CSV from empty data")
        
        if fieldnames is None:
            fieldnames = list(data[0].keys())
        
        output_path = self.output_dir / file_path
        
        with open(output_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
        return str(output_path)
    
    def create_summary_report(self, data: List[Dict[str, Any]], 
                            title: str = "Data Summary") -> Dict[str, Any]:
        """
        Create a summary report from data
        
        Args:
            data (List[Dict[str, Any]]): Data to summarize
            title (str): Report title
            
        Returns:
            Dict[str, Any]: Summary report
        """
        if not data:
            return {
                'title': title,
                'total_records': 0,
                'fields': [],
                'summary': 'No data available'
            }
        
        fields = list(data[0].keys())
        field_stats = {}
        
        for field in fields:
            values = [record.get(field) for record in data if record.get(field) is not None]
            field_stats[field] = {
                'total_values': len(values),
                'missing_values': len(data) - len(values),
                'unique_values': len(set(str(v) for v in values))
            }
        
        return {
            'title': title,
            'total_records': len(data),
            'fields': fields,
            'field_statistics': field_stats,
            'summary': f"Dataset contains {len(data)} records with {len(fields)} fields"
        }
    
    def format_table(self, data: List[Dict[str, Any]], max_width: int = 80) -> str:
        """
        Format data as a simple text table
        
        Args:
            data (List[Dict[str, Any]]): Data to format
            max_width (int): Maximum table width
            
        Returns:
            str: Formatted table string
        """
        if not data:
            return "No data to display"
        
        headers = list(data[0].keys())
        
        # Calculate column widths
        col_widths = {}
        for header in headers:
            col_widths[header] = max(
                len(header),
                max(len(str(row.get(header, ''))) for row in data)
            )
        
        # Create header row
        header_row = " | ".join(header.ljust(col_widths[header]) for header in headers)
        separator = "-" * len(header_row)
        
        # Create data rows
        data_rows = []
        for row in data:
            formatted_row = " | ".join(
                str(row.get(header, '')).ljust(col_widths[header]) 
                for header in headers
            )
            data_rows.append(formatted_row)
        
        return "\n".join([header_row, separator] + data_rows)