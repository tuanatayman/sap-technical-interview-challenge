"""
Data processing utilities for handling various data formats
"""

import json
import csv
from typing import List, Dict, Any, Optional
from pathlib import Path


class DataProcessor:
    """
    A class for processing different types of data files and structures
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """Initialize the DataProcessor with optional configuration"""
        self.config = config or {}
        self.processed_count = 0
    
    def load_json_file(self, file_path: str) -> Dict[str, Any]:
        """
        Load and parse a JSON file
        
        Args:
            file_path (str): Path to the JSON file
            
        Returns:
            Dict[str, Any]: Parsed JSON data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file is not valid JSON
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        self.processed_count += 1
        return data
    
    def load_csv_file(self, file_path: str, delimiter: str = ',') -> List[Dict[str, str]]:
        """
        Load and parse a CSV file
        
        Args:
            file_path (str): Path to the CSV file
            delimiter (str): CSV delimiter character
            
        Returns:
            List[Dict[str, str]]: List of dictionaries representing CSV rows
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        data = []
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            data = list(reader)
        
        self.processed_count += 1
        return data
    
    def filter_data(self, data: List[Dict], field: str, value: Any) -> List[Dict]:
        """
        Filter a list of dictionaries by a specific field value
        
        Args:
            data (List[Dict]): List of dictionaries to filter
            field (str): Field name to filter by
            value (Any): Value to match
            
        Returns:
            List[Dict]: Filtered data
        """
        return [item for item in data if item.get(field) == value]
    
    def aggregate_by_field(self, data: List[Dict], field: str) -> Dict[str, int]:
        """
        Aggregate data by counting occurrences of field values
        
        Args:
            data (List[Dict]): List of dictionaries to aggregate
            field (str): Field name to aggregate by
            
        Returns:
            Dict[str, int]: Dictionary with field values as keys and counts as values
        """
        aggregation = {}
        for item in data:
            key = item.get(field, 'Unknown')
            aggregation[key] = aggregation.get(key, 0) + 1
        
        return aggregation
    
    def get_processing_stats(self) -> Dict[str, int]:
        """
        Get processing statistics
        
        Returns:
            Dict[str, int]: Processing statistics
        """
        return {
            'files_processed': self.processed_count,
            'config_items': len(self.config)
        }