# Data Processing Library - Technical Interview Project

Welcome to the technical interview challenge! This repository contains a Python data processing library with scripts and a CI/CD pipeline that you'll be working with.

## 📋 Project Overview

This project simulates a real-world data processing application with:
- **Custom Python Library** (`datalib`) for data processing, validation, and formatting
- **Two Python Scripts** for data analysis and report generation
- **GitHub Actions Pipeline** for automated testing and simulated deployment
- **Unit Tests** ensuring code quality and reliability
- **Sample Data** for testing and demonstration

## 🏗️ Project Structure

```
ENTRETIEN/
├── .github/
│   └── workflows/
│       └── pipeline.yml         # CI/CD pipeline configuration
├── src/
│   └── datalib/                 # Core data processing library
│       ├── __init__.py
│       ├── processor.py         # Data loading and processing
│       ├── validator.py         # Data validation utilities
│       └── formatter.py         # Data formatting and export
├── scripts/
│   ├── analyze_customers.py     # Customer data analysis script
│   └── generate_report.py       # Sales report generation script
├── tests/
│   ├── test_processor.py        # Unit tests for processor
│   └── test_validator.py        # Unit tests for validator
├── data/
│   ├── customers.json           # Sample customer data
│   └── sales.json              # Sample sales data
├── requirements.txt             # Python dependencies
└── setup.cfg                    # Project configuration
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ENTRETIEN
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tests to verify setup:**
   ```bash
   python -m pytest tests/ -v
   ```

### Running the Scripts

**Customer Analysis:**
```bash
cd scripts
python analyze_customers.py ../data/customers.json
```

**Report Generation:**
```bash
cd scripts
python generate_report.py ../data/sales.json json
python generate_report.py ../data/sales.json csv
python generate_report.py ../data/sales.json txt
```

## 🎯 Interview Challenge

### Background
You are a new developer joining the team that maintains this data processing library. The business team has requested a new feature, and you need to understand the existing codebase and implement the requested functionality.

### Current System Capabilities

The `datalib` library currently provides:

1. **Data Processing** (`DataProcessor`):
   - Load JSON and CSV files
   - Filter data by field values
   - Aggregate data by counting field values
   - Track processing statistics

2. **Data Validation** (`DataValidator`):
   - Email format validation
   - Required field validation
   - Data type validation
   - Date format validation
   - Numeric range validation
   - Complete dataset validation

3. **Data Formatting** (`DataFormatter`):
   - Currency formatting
   - Percentage formatting
   - JSON/CSV export
   - Summary report generation
   - Text table formatting

### 🎯 Feature Request: Data Transformation Module

**Business Requirement:**
"We need to add data transformation capabilities to clean and standardize our data before analysis. Specifically, we need to be able to normalize text fields, handle missing values, and apply data transformations."

### Your Task

Implement a new `DataTransformer` class in the `datalib` library with the following functionality:

#### Required Methods:

1. **`normalize_text(text: str, options: dict = None) -> str`**
   - Convert text to lowercase
   - Remove extra whitespace
   - Remove special characters (configurable)
   - Handle None/empty values

2. **`handle_missing_values(data: List[Dict], strategy: str = 'remove', fill_value: Any = None) -> List[Dict]`**
   - Strategy options: 'remove', 'fill', 'skip'
   - Support different fill values for different data types

3. **`standardize_dates(data: List[Dict], date_fields: List[str], target_format: str = '%Y-%m-%d') -> List[Dict]`**
   - Convert various date formats to a standard format
   - Handle common date formats automatically

4. **`transform_dataset(data: List[Dict], transformations: List[Dict]) -> List[Dict]`**
   - Apply multiple transformations in sequence
   - Support transformation pipeline configuration

#### Implementation Requirements:

1. **Create the new file:** `src/datalib/transformer.py`
2. **Update the main module:** Add import to `src/datalib/__init__.py`
3. **Write comprehensive tests:** Create `tests/test_transformer.py`
4. **Update the analysis script:** Modify `scripts/analyze_customers.py` to use the new transformer
5. **Ensure CI/CD passes:** All existing tests should continue to pass

#### Example Usage:
```python
from datalib import DataTransformer

transformer = DataTransformer()

# Normalize text
clean_text = transformer.normalize_text("  Hello, World!  ")

# Handle missing values
clean_data = transformer.handle_missing_values(data, strategy='fill', fill_value='Unknown')

# Standardize dates
standardized_data = transformer.standardize_dates(data, ['created_date', 'updated_date'])

# Apply transformation pipeline
transformations = [
    {'type': 'normalize_text', 'fields': ['name', 'description']},
    {'type': 'handle_missing', 'strategy': 'fill', 'fill_value': 'N/A'}
]
transformed_data = transformer.transform_dataset(data, transformations)
```

## 📝 Evaluation Criteria

You will be evaluated on:

1. **Code Understanding** - How well you understand the existing codebase structure and patterns
2. **Implementation Quality** - Clean, readable, and maintainable code following project conventions
3. **Testing** - Comprehensive unit tests for the new functionality
4. **Integration** - Proper integration with existing codebase and updating relevant scripts
5. **Documentation** - Clear docstrings and comments
6. **Problem-Solving** - How you handle edge cases and error conditions

## 💡 Hints and Guidelines

1. **Study the existing code patterns** - Look at how other classes are implemented
2. **Follow the existing code style** - Match the docstring format and naming conventions
3. **Consider edge cases** - What happens with empty data, None values, invalid inputs?
4. **Test thoroughly** - Write tests for both success and failure cases
5. **Integration is key** - Make sure your changes work with the existing scripts
6. **Ask questions** - If something is unclear, don't hesitate to ask

## 🛠️ CI/CD Pipeline

The project includes a GitHub Actions pipeline that:
- Runs unit tests with coverage reporting
- Performs code quality checks (linting, formatting)
- Executes integration tests
- Runs security scans
- Simulates deployment to staging and production

Your implementation should not break the existing pipeline!

## 📊 Sample Data

The project includes sample data files for testing:
- `data/customers.json` - Customer information with some invalid records
- `data/sales.json` - Sales transaction data

Feel free to use this data for testing your implementation.

## 🎯 Bonus Challenges (Optional)

If you finish the main task quickly, consider these additional challenges:

1. **Add data export functionality** to save transformed data
2. **Implement data validation** for transformation configurations
3. **Add performance metrics** to track transformation execution time
4. **Create a command-line interface** for the transformation tool

## 📞 Questions?

If you have any questions about the requirements or need clarification, please ask! This is meant to be a collaborative discussion, not a silent test.

Good luck! 🚀