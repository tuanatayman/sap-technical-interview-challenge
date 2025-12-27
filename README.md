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
└── docker-compose.yml   # Development environment
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

## 🎯 DevOps Interview Challenge

### Background
You are a **DevOps engineer** joining the team that maintains this Python data processing platform. The application works locally, but the infrastructure and CI/CD pipeline have critical issues that need immediate attention. Your mission is to diagnose and fix these DevOps problems while implementing best practices.

### Current System State

The platform currently has:

1. **Working Application Code**:
   - Python data processing library with unit tests
   - Customer analysis and report generation scripts
   - Sample data for testing and validation

2. **Broken DevOps Infrastructure**:
   - GitHub Actions pipeline with dependency and path issues
   - Insecure Docker container running as root
   - Kubernetes manifests missing security contexts
   - Hardcoded configuration values
   - No security scanning or monitoring
   - Complete dataset validation

3. **Data Formatting** (`DataFormatter`):
   - Currency formatting
   - Percentage formatting
   - JSON/CSV export
   - Summary report generation
   - Text table formatting

## 🚀 The Challenge: Fix the Infrastructure

### What's Currently Broken?

The DevOps infrastructure has several issues that need fixing:

#### 1. CI/CD Pipeline Issues (.github/workflows/pipeline.yml)
- ❌ Missing dependency installation step
- ❌ Incorrect coverage report paths
- ❌ No security vulnerability scanning
- ❌ Integration tests not properly configured
- ❌ No deployment automation

#### 2. Docker Security Problems (Dockerfile)
- ❌ Container running as root user
- ❌ No multi-stage build optimization
- ❌ Unnecessary packages installed
- ❌ No health checks configured
- ❌ Insecure base image practices

#### 3. Kubernetes Configuration Gaps (k8s/deployment.yaml)
- ❌ Missing security contexts
- ❌ No resource limits or requests
- ❌ Missing readiness/liveness probes
- ❌ No pod security policies
- ❌ Insecure service configuration

### Your Mission

Fix these infrastructure issues to create a production-ready deployment pipeline with proper security and monitoring.

## 📋 Challenge Tasks

### 1. 🔧 Fix the CI/CD Pipeline
**File:** `.github/workflows/pipeline.yml`

**Required fixes:**
- Install Python dependencies properly
- Fix test coverage reporting paths
- Add security vulnerability scanning
- Configure integration test environment
- Implement proper deployment stages

### 2. 🐳 Secure the Docker Container
**File:** `Dockerfile`

**Security improvements needed:**
- Implement non-root user
- Add multi-stage build
- Remove unnecessary packages
- Add health checks
- Use secure base images

### 3. ☸️ Harden Kubernetes Deployment
**File:** `k8s/deployment.yaml`

**Security enhancements required:**
- Add security contexts
- Configure resource limits
- Implement health checks
- Add pod security policies
- Secure service configuration

### 4. 📊 Verify Everything Works
**Validation requirements:**
- All pipeline stages pass ✅
- Container security scan passes ✅
- Application runs correctly ✅
- Kubernetes deployment succeeds ✅

## 🔍 Assessment Areas

### DevOps Skills Being Evaluated:

1. **CI/CD Pipeline Design** - Understanding of automated testing and deployment
2. **Container Security** - Knowledge of Docker security best practices
3. **Kubernetes Operations** - Understanding of K8s security and resource management
4. **Problem-Solving** - Systematic approach to identifying and fixing issues
5. **Security Awareness** - Implementation of security best practices
6. **Documentation** - Clear explanation of changes and decisions

## 💡 Getting Started

1. **Clone the repository** and examine the current state
2. **Run the pipeline** to see what fails
3. **Analyze the errors** systematically
4. **Fix issues one by one** and test locally
5. **Document your changes** and reasoning

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

Ready to start fixing? Begin by examining the current pipeline failures and work through each issue systematically!

Good luck! 🚀

---

*This is a technical interview challenge. The codebase contains intentional issues for assessment purposes.*