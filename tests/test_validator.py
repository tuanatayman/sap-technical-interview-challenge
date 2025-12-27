"""
Unit tests for the DataValidator class
"""

import unittest
import sys
from pathlib import Path

# Add src to Python path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from datalib.validator import DataValidator


class TestDataValidator(unittest.TestCase):
    """Test cases for DataValidator class"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.validator = DataValidator()
    
    def test_validate_email_valid(self):
        """Test email validation with valid emails"""
        valid_emails = [
            'test@example.com',
            'user.name@domain.co.uk',
            'user+tag@example.org',
            'firstname.lastname@company.com'
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(self.validator.validate_email(email))
    
    def test_validate_email_invalid(self):
        """Test email validation with invalid emails"""
        invalid_emails = [
            'invalid-email',
            'user@',
            '@domain.com',
            'user.domain.com',
            'user@domain',
            'user space@domain.com'
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(self.validator.validate_email(email))
    
    def test_validate_required_fields_success(self):
        """Test required field validation with valid data"""
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'age': 30
        }
        required_fields = ['name', 'email', 'age']
        
        is_valid, missing_fields = self.validator.validate_required_fields(data, required_fields)
        self.assertTrue(is_valid)
        self.assertEqual(missing_fields, [])
    
    def test_validate_required_fields_missing(self):
        """Test required field validation with missing fields"""
        data = {
            'name': 'John Doe',
            'email': 'john@example.com'
            # age is missing
        }
        required_fields = ['name', 'email', 'age']
        
        is_valid, missing_fields = self.validator.validate_required_fields(data, required_fields)
        self.assertFalse(is_valid)
        self.assertEqual(missing_fields, ['age'])
    
    def test_validate_required_fields_empty_values(self):
        """Test required field validation with empty values"""
        data = {
            'name': '',
            'email': 'john@example.com',
            'age': None
        }
        required_fields = ['name', 'email', 'age']
        
        is_valid, missing_fields = self.validator.validate_required_fields(data, required_fields)
        self.assertFalse(is_valid)
        self.assertCountEqual(missing_fields, ['name', 'age'])
    
    def test_validate_data_types_success(self):
        """Test data type validation with correct types"""
        data = {
            'name': 'John Doe',
            'age': 30,
            'score': 95.5
        }
        type_schema = {
            'name': str,
            'age': int,
            'score': float
        }
        
        is_valid, type_errors = self.validator.validate_data_types(data, type_schema)
        self.assertTrue(is_valid)
        self.assertEqual(type_errors, [])
    
    def test_validate_data_types_failure(self):
        """Test data type validation with incorrect types"""
        data = {
            'name': 'John Doe',
            'age': '30',  # Should be int
            'score': 95   # Should be float
        }
        type_schema = {
            'name': str,
            'age': int,
            'score': float
        }
        
        is_valid, type_errors = self.validator.validate_data_types(data, type_schema)
        self.assertFalse(is_valid)
        self.assertEqual(len(type_errors), 2)
    
    def test_validate_date_format_valid(self):
        """Test date format validation with valid dates"""
        valid_dates = ['2024-01-01', '2023-12-31', '2024-02-29']  # 2024 is a leap year
        
        for date_str in valid_dates:
            with self.subTest(date=date_str):
                self.assertTrue(self.validator.validate_date_format(date_str))
    
    def test_validate_date_format_invalid(self):
        """Test date format validation with invalid dates"""
        invalid_dates = ['2024-13-01', '2024-02-30', '24-01-01', '2024/01/01']
        
        for date_str in invalid_dates:
            with self.subTest(date=date_str):
                self.assertFalse(self.validator.validate_date_format(date_str))
    
    def test_validate_range_success(self):
        """Test range validation with valid values"""
        self.assertTrue(self.validator.validate_range(50, 0, 100))
        self.assertTrue(self.validator.validate_range(0, 0, 100))
        self.assertTrue(self.validator.validate_range(100, 0, 100))
        self.assertTrue(self.validator.validate_range(50, min_value=0))
        self.assertTrue(self.validator.validate_range(50, max_value=100))
    
    def test_validate_range_failure(self):
        """Test range validation with invalid values"""
        self.assertFalse(self.validator.validate_range(-1, 0, 100))
        self.assertFalse(self.validator.validate_range(101, 0, 100))
        self.assertFalse(self.validator.validate_range(-1, min_value=0))
        self.assertFalse(self.validator.validate_range(101, max_value=100))
    
    def test_validate_dataset(self):
        """Test complete dataset validation"""
        dataset = [
            {'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
            {'name': 'Bob', 'email': 'bob@example.com', 'age': 30},
            {'name': '', 'email': 'invalid-email', 'age': 'thirty'},  # Invalid record
            {'email': 'carol@example.com', 'age': 35}  # Missing name
        ]
        
        schema = {
            'required_fields': ['name', 'email', 'age'],
            'types': {
                'name': str,
                'email': str,
                'age': int
            }
        }
        
        results = self.validator.validate_dataset(dataset, schema)
        
        self.assertEqual(results['total_records'], 4)
        self.assertEqual(results['valid_records'], 2)
        self.assertEqual(results['invalid_records'], 2)
        self.assertEqual(len(results['errors']), 2)


if __name__ == '__main__':
    unittest.main()