"""
Data validation utilities for ensuring data quality and correctness
"""

import re
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime


class DataValidator:
    """
    A class for validating data structures and values
    """
    
    def __init__(self, strict_mode: bool = False):
        """Initialize the DataValidator"""
        self.strict_mode = strict_mode
        self.validation_errors = []
    
    def validate_email(self, email: str) -> bool:
        """
        Validate email address format
        
        Args:
            email (str): Email address to validate
            
        Returns:
            bool: True if email is valid, False otherwise
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_required_fields(self, data: Dict[str, Any], required_fields: List[str]) -> Tuple[bool, List[str]]:
        """
        Validate that required fields are present and not empty
        
        Args:
            data (Dict[str, Any]): Data dictionary to validate
            required_fields (List[str]): List of required field names
            
        Returns:
            Tuple[bool, List[str]]: (is_valid, missing_fields)
        """
        missing_fields = []
        
        for field in required_fields:
            if field not in data:
                missing_fields.append(field)
            elif data[field] is None or data[field] == "":
                missing_fields.append(field)
        
        return len(missing_fields) == 0, missing_fields
    
    def validate_data_types(self, data: Dict[str, Any], type_schema: Dict[str, type]) -> Tuple[bool, List[str]]:
        """
        Validate data types against a schema
        
        Args:
            data (Dict[str, Any]): Data to validate
            type_schema (Dict[str, type]): Schema defining expected types
            
        Returns:
            Tuple[bool, List[str]]: (is_valid, type_errors)
        """
        type_errors = []
        
        for field, expected_type in type_schema.items():
            if field in data:
                if not isinstance(data[field], expected_type):
                    error_msg = f"Field '{field}' should be {expected_type.__name__}, got {type(data[field]).__name__}"
                    type_errors.append(error_msg)
        
        return len(type_errors) == 0, type_errors
    
    def validate_date_format(self, date_string: str, date_format: str = "%Y-%m-%d") -> bool:
        """
        Validate date string format
        
        Args:
            date_string (str): Date string to validate
            date_format (str): Expected date format
            
        Returns:
            bool: True if date format is valid, False otherwise
        """
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False
    
    def validate_range(self, value: float, min_value: Optional[float] = None, 
                      max_value: Optional[float] = None) -> bool:
        """
        Validate that a numeric value is within a specified range
        
        Args:
            value (float): Value to validate
            min_value (Optional[float]): Minimum allowed value
            max_value (Optional[float]): Maximum allowed value
            
        Returns:
            bool: True if value is within range, False otherwise
        """
        if min_value is not None and value < min_value:
            return False
        if max_value is not None and value > max_value:
            return False
        return True
    
    def validate_dataset(self, dataset: List[Dict[str, Any]], 
                        schema: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate an entire dataset against a schema
        
        Args:
            dataset (List[Dict[str, Any]]): Dataset to validate
            schema (Dict[str, Any]): Validation schema
            
        Returns:
            Dict[str, Any]: Validation results
        """
        results = {
            'total_records': len(dataset),
            'valid_records': 0,
            'invalid_records': 0,
            'errors': []
        }
        
        required_fields = schema.get('required_fields', [])
        type_schema = schema.get('types', {})
        
        for i, record in enumerate(dataset):
            record_valid = True
            record_errors = []
            
            # Check required fields
            is_valid, missing_fields = self.validate_required_fields(record, required_fields)
            if not is_valid:
                record_valid = False
                record_errors.extend([f"Missing field: {field}" for field in missing_fields])
            
            # Check data types
            is_valid, type_errors = self.validate_data_types(record, type_schema)
            if not is_valid:
                record_valid = False
                record_errors.extend(type_errors)
            
            if record_valid:
                results['valid_records'] += 1
            else:
                results['invalid_records'] += 1
                results['errors'].append({
                    'record_index': i,
                    'errors': record_errors
                })
        
        return results