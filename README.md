# 🛠️ DevOps Technical Interview Challenge

## Welcome!
This repository contains a **Python data processing platform** that needs DevOps improvements. Your mission is to identify and fix infrastructure issues while implementing best practices for CI/CD, security, and deployment.

## 📋 Project Overview

You'll be working with:
- **Python Data Library** (`datalib`) for processing, validation, and formatting
- **Analysis Scripts** for customer data and sales reporting
- **CI/CD Pipeline** using GitHub Actions
- **Container Infrastructure** with Docker and Kubernetes
- **Configuration Management** system

## 🏗️ Project Structure

```
├── .github/workflows/    # CI/CD pipeline
├── src/datalib/          # Python library
│   ├── processor.py      # Data processing utilities  
│   ├── validator.py      # Data validation functions
│   ├── formatter.py      # Output formatting
│   └── config.py         # Configuration management
├── scripts/              # Analysis scripts
├── tests/                # Unit tests
├── data/                 # Sample JSON data files
├── k8s/                  # Kubernetes manifests
├── Dockerfile            # Container configuration
├── docker-compose.yml    # Development environment
└── requirements.txt      # Python dependencies
```

## 🚀 Getting Started

### 1. Explore the Application
```bash
# Clone the repository
git clone https://github.com/tuanatayman/sap-technical-interview-challenge.git
cd sap-technical-interview-challenge

# Test the application locally
python3 scripts/analyze_customers.py data/customers.json
python3 scripts/generate_report.py data/sales.json json
python3 -m pytest tests/ -v
```

### 2. Investigate the Infrastructure
```bash
# Check the CI/CD pipeline status
# Visit: https://github.com/tuanatayman/sap-technical-interview-challenge/actions

# Examine the infrastructure files
cat .github/workflows/pipeline.yml
cat Dockerfile
cat k8s/deployment.yaml
cat docker-compose.yml
```

## 🎯 Your Challenge

### The Situation
You're a **DevOps engineer** joining a team that has built a working Python data processing application. The code runs fine locally, but the team is struggling with their infrastructure and deployment pipeline. The application needs to be production-ready with proper CI/CD, security, and monitoring.

### Your Mission
1. **Diagnose** what's preventing successful deployments
2. **Fix** the infrastructure and pipeline issues
3. **Implement** DevOps best practices
4. **Document** your changes and decisions

### Success Criteria
- CI/CD pipeline runs successfully end-to-end
- Application deploys securely to containerized environments
- Proper monitoring and observability in place
- Security best practices implemented
- Clear documentation for future maintenance

## 🔍 What We're Evaluating

- **Problem-solving approach** - How you identify and prioritize issues
- **DevOps expertise** - Knowledge of CI/CD, containers, and orchestration
- **Awareness** - Implementation of best practices
- **Communication** - Clear documentation and explanation of changes

## 📝 Submission Guidelines

1. **Work in your own feature branch**: `devops/<name>/infrastructure-fixes`
2. **Document your process**: Commit messages explaining what you fixed and why
3. **Provide evidence**: Pipeline runs, test results, deployment proof
4. **Submit via Pull Request**: Include summary of changes and next steps

## 🆘 Getting Help

If you're stuck:
- Check **GitHub Issues** for clarification questions
- Review **Pipeline Logs** in GitHub Actions for error details
- Test changes **locally** before pushing

Ready to diagnose and fix the infrastructure? Good luck! 🚀

---

*This challenge contains intentional issues for assessment purposes.*