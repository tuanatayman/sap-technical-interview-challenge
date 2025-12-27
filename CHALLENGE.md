# 🎯 Technical Interview Challenge - Feature Implementation

## What You Need to Do

**Main Task:** Implement a `DataTransformer` class in the `datalib` library.

### Implementation Steps:

1. **Create `src/datalib/transformer.py`** with these methods:
   - `normalize_text(text: str, options: dict = None) -> str`
   - `handle_missing_values(data: List[Dict], strategy: str = 'remove', fill_value: Any = None) -> List[Dict]`
   - `standardize_dates(data: List[Dict], date_fields: List[str], target_format: str = '%Y-%m-%d') -> List[Dict]`
   - `transform_dataset(data: List[Dict], transformations: List[Dict]) -> List[Dict]`

2. **Update `src/datalib/__init__.py`** to include the new `DataTransformer` class

3. **Create `tests/test_transformer.py`** with comprehensive unit tests

4. **Update `scripts/analyze_customers.py`** to use the new transformer

5. **Ensure all existing tests still pass**

### Available VS Code Tasks:
- **Run Customer Analysis** - Test the customer analysis script
- **Generate Sales Report (JSON)** - Create JSON sales report
- **Generate Sales Report (CSV)** - Create CSV sales report  
- **Run Unit Tests** - Execute the test suite
- **Run All Tests and Analysis** - Complete validation

### Getting Started:
1. Study the existing code in `src/datalib/` to understand patterns
2. Look at the sample data in `data/` to understand what you're working with
3. Run the existing scripts to see current functionality
4. Implement the new `DataTransformer` class
5. Test your implementation thoroughly

### Success Criteria:
- ✅ All existing functionality continues to work
- ✅ New `DataTransformer` class is properly implemented
- ✅ Unit tests provide good coverage
- ✅ Integration with existing scripts
- ✅ Code follows project conventions

Good luck! 🚀