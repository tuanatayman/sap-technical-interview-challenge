# 🛠️ DevOps Technical Interview Challenge

## Welcome!
This repository contains a **Python data processing platform** with intentional DevOps issues that need to be resolved. Your mission is to identify, diagnose, and fix these problems while implementing DevOps best practices.

## 📋 Project Overview

This project simulates a real-world data processing application that **needs DevOps fixes**:
- **Python Data Library** (`datalib`) with processing, validation, and formatting (working)
- **Analysis Scripts** for customer data and sales reporting (working locally)  
- **Broken CI/CD Pipeline** with multiple issues requiring DevOps expertise
- **Insecure Infrastructure** (Dockerfile, Kubernetes) needing security hardening
- **Missing DevOps Tools** (monitoring, logging, proper configuration management)

## 🏗️ Project Structure

```
├── .github/workflows/    # CI/CD pipeline (HAS BUGS - missing deps, wrong paths)
├── src/datalib/          # Python library (working)
│   ├── processor.py      # Data processing utilities  
│   ├── validator.py      # Data validation functions
│   ├── formatter.py      # Output formatting
│   └── config.py         # Configuration management (INCOMPLETE)
├── scripts/              # Analysis scripts (working locally)
├── tests/                # Unit tests (working)
├── data/                 # Sample JSON data files
├── k8s/                  # Kubernetes manifests (MISSING SECURITY)
├── Dockerfile            # Container config (INSECURE - root user)  
├── docker-compose.yml    # Development stack (INCOMPLETE)
├── requirements.txt      # Basic dependencies
├── CHALLENGE.md          # Detailed implementation tasks
└── DEVOPS_INTERVIEW_GUIDE.md  # Interviewer reference
```
├── tests/
│   ├── test_processor.py        # Unit tests for processor
│   └── test_validator.py        # Unit tests for validator
├── data/
│   ├── customers.json           # Sample customer data
│   └── sales.json              # Sample sales data
├── requirements.txt             # Python dependencies
└── setup.cfg                    # Project configuration
```

## 🚀 Quick Start - Investigate the Issues

### 1. Test Current Functionality
```bash
# Clone and explore
git clone https://github.com/tuanatayman/sap-technical-interview-challenge.git
cd sap-technical-interview-challenge

# These should work locally
python3 scripts/analyze_customers.py data/customers.json
python3 scripts/generate_report.py data/sales.json json
```

### 2. Discover the Problems  
```bash
# Check GitHub Actions (will be failing)
# Go to: https://github.com/tuanatayman/sap-technical-interview-challenge/actions

# Examine the broken pipeline
cat .github/workflows/pipeline.yml

# Review insecure infrastructure  
cat Dockerfile                    # Runs as root!
cat k8s/deployment.yaml          # Missing security contexts!
cat src/config.py                # Hardcoded values!
```

### 3. Your DevOps Mission

## 🎯 Challenge Tasks

### Task 1: Fix the Failing CI/CD Pipeline (Priority: High)
**Problem:** The GitHub Actions pipeline is currently failing. 
- Analyze the pipeline logs in `.github/workflows/pipeline.yml`
- Fix dependency installation issues
- Ensure tests run properly in the containerized environment
- Add proper error handling and retry mechanisms

### Task 2: Implement Multi-Environment Support
**Requirements:**
- Add environment-specific configuration (dev, staging, prod)
- Create environment variable management
- Implement different deployment strategies per environment
- Add environment health checks

### Task 3: Add Security and Quality Gates
**Implement these CI/CD improvements:**
- Add SAST (Static Application Security Testing)
- Implement code coverage thresholds (minimum 80%)
- Add dependency vulnerability scanning
- Create PR quality gates that block merging on failures

### Task 4: Infrastructure as Code
**Create deployment configurations:**
- Add `Dockerfile` for containerization
- Create `docker-compose.yml` for local development
- Add Kubernetes manifests (`k8s/` directory)
- Include monitoring and logging setup

### Task 5: Pipeline Optimization
**Performance improvements:**
- Implement build caching strategies
- Add parallel job execution where possible
- Create pipeline status notifications (Slack/email)
- Add deployment rollback capabilities

## 📋 Technical Requirements

### Expected Deliverables:
1. **Fixed CI/CD pipeline** with all tests passing
2. **Environment configuration** system
3. **Security scanning** integrated into pipeline  
4. **Containerization** setup with multi-stage builds
5. **Monitoring/logging** configuration
6. **Documentation** for deployment procedures

### Skills Demonstrated:
- ✅ **CI/CD Pipeline Design** - GitHub Actions, multi-stage workflows
- ✅ **Infrastructure as Code** - Docker, Kubernetes, configuration management
- ✅ **Security Best Practices** - SAST, dependency scanning, secrets management
- ✅ **Monitoring & Observability** - Health checks, logging, alerting
- ✅ **Python Ecosystem** - Understanding package management, testing frameworks
- ✅ **Problem Solving** - Debugging failed pipelines, performance optimization

## 🔧 Implementation Guide

### 1. Analyze Current Issues
```bash
# Check GitHub Actions failures
# Go to: https://github.com/tuanatayman/sap-technical-interview-challenge/actions

# Review current pipeline configuration
cat .github/workflows/pipeline.yml

# Test locally (should work)
python3 -m pytest tests/ -v
python3 scripts/analyze_customers.py data/customers.json

# Try Docker build (will reveal issues)
docker build -t datalib .
```

### 2. Investigate the Environment
- Study the existing `src/datalib/` structure
- Understand the data processing workflows
- Review current testing approach
- Identify deployment gaps

### 3. Common Issues to Fix
- Missing or incorrect dependency declarations
- Environment-specific configuration handling
- Test execution in CI environment
- Security vulnerabilities in dependencies
- No containerization strategy
- Missing monitoring/observability

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

## 🎉 Success Criteria

### Minimum Requirements (Must Have):
- ✅ CI/CD pipeline executes successfully end-to-end
- ✅ All existing functionality continues to work
- ✅ Security scanning passes without critical vulnerabilities
- ✅ Code coverage meets threshold requirements
- ✅ Docker container builds and runs successfully

### Bonus Points (Nice to Have):
- ✅ Kubernetes deployment manifests
- ✅ Pipeline optimization (caching, parallelization)
- ✅ Comprehensive monitoring setup
- ✅ Automated rollback capabilities
- ✅ Infrastructure automation scripts

## 🚀 Submission Guidelines

1. **Create a feature branch** following naming convention: `devops/pipeline-fixes`
2. **Document your changes** in commit messages and PR description
3. **Include testing evidence** - pipeline runs, local testing results
4. **Provide deployment guide** - how to deploy and monitor the solution
5. **Submit via Pull Request** with detailed explanation of fixes  

## 🔧 What We're Looking For

- **Problem-solving approach** - How you identify and prioritize issues
- **DevOps knowledge** - Understanding of CI/CD, containers, K8s security
- **Security awareness** - Implementation of security best practices  
- **Documentation** - Clear explanations of changes and decisions
- **Testing** - Validation that fixes actually work

## 💡 Getting Help

- **GitHub Issues** - Ask questions about requirements
- **Pipeline Logs** - Check GitHub Actions for specific error details
- **Local Testing** - Always verify fixes work in your environment first

Ready to dive in? Check out **[CHALLENGE.md](./CHALLENGE.md)** for detailed instructions!

Good luck! 🚀

---

*This is a technical interview challenge. The codebase contains intentional issues for assessment purposes.*