"""
Unit tests for the DataProcessor class
"""

import unittest
import tempfile
import json
import csv
from pathlib import Path
import sys

# Add src to Python path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from datalib.processor import DataProcessor


class TestDataProcessor(unittest.TestCase):
    """Test cases for DataProcessor class"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.processor = DataProcessor()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)
    
    def tearDown(self):
        """Clean up after each test method"""
        self.temp_dir.cleanup()
    
    def test_initialization(self):
        """Test DataProcessor initialization"""
        processor = DataProcessor()
        self.assertEqual(processor.processed_count, 0)
        self.assertEqual(processor.config, {})
        
        config = {'setting1': 'value1'}
        processor_with_config = DataProcessor(config)
        self.assertEqual(processor_with_config.config, config)
    
    def test_load_json_file_success(self):
        """Test successful JSON file loading"""
        # Create test JSON file
        test_data = {'name': 'Test', 'value': 123}
        json_file = self.temp_path / 'test.json'
        
        with open(json_file, 'w') as f:
            json.dump(test_data, f)
        
        # Test loading
        result = self.processor.load_json_file(str(json_file))
        self.assertEqual(result, test_data)
        self.assertEqual(self.processor.processed_count, 1)
    
    def test_load_json_file_not_found(self):
        """Test JSON file loading with non-existent file"""
        with self.assertRaises(FileNotFoundError):
            self.processor.load_json_file('non_existent_file.json')
    
    def test_load_csv_file_success(self):
        """Test successful CSV file loading"""
        # Create test CSV file
        csv_file = self.temp_path / 'test.csv'
        test_data = [
            ['name', 'age', 'city'],
            ['Alice', '25', 'New York'],
            ['Bob', '30', 'Los Angeles']
        ]
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(test_data)
        
        # Test loading
        result = self.processor.load_csv_file(str(csv_file))
        expected = [
            {'name': 'Alice', 'age': '25', 'city': 'New York'},
            {'name': 'Bob', 'age': '30', 'city': 'Los Angeles'}
        ]
        self.assertEqual(result, expected)
        self.assertEqual(self.processor.processed_count, 1)
    
    def test_filter_data(self):
        """Test data filtering functionality"""
        test_data = [
            {'name': 'Alice', 'age': 25, 'city': 'New York'},
            {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
            {'name': 'Carol', 'age': 25, 'city': 'Chicago'}
        ]
        
        # Filter by age
        result = self.processor.filter_data(test_data, 'age', 25)
        expected = [
            {'name': 'Alice', 'age': 25, 'city': 'New York'},
            {'name': 'Carol', 'age': 25, 'city': 'Chicago'}
        ]
        self.assertEqual(result, expected)
        
        # Filter by city
        result = self.processor.filter_data(test_data, 'city', 'Los Angeles')
        expected = [{'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}]
        self.assertEqual(result, expected)
    
    def test_aggregate_by_field(self):
        """Test data aggregation functionality"""
        test_data = [
            {'name': 'Alice', 'department': 'Engineering'},
            {'name': 'Bob', 'department': 'Sales'},
            {'name': 'Carol', 'department': 'Engineering'},
            {'name': 'David', 'department': 'Sales'},
            {'name': 'Eva', 'department': 'Marketing'}
        ]
        
        result = self.processor.aggregate_by_field(test_data, 'department')
        expected = {
            'Engineering': 2,
            'Sales': 2,
            'Marketing': 1
        }
        self.assertEqual(result, expected)
    
    def test_get_processing_stats(self):
        """Test processing statistics"""
        # Initial stats
        stats = self.processor.get_processing_stats()
        self.assertEqual(stats['files_processed'], 0)
        self.assertEqual(stats['config_items'], 0)
        
        # Create and load a test file
        test_data = {'test': 'data'}
        json_file = self.temp_path / 'test.json'
        with open(json_file, 'w') as f:
            json.dump(test_data, f)
        
        self.processor.load_json_file(str(json_file))
        
        # Check updated stats
        stats = self.processor.get_processing_stats()
        self.assertEqual(stats['files_processed'], 1)


if __name__ == '__main__':
    unittest.main()