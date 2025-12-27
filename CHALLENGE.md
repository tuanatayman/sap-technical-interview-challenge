# 🛠️ DevOps Technical Interview Challenge

## Scenario
You're joining a team that maintains a Python data processing platform. The CI/CD pipeline has several issues and needs DevOps improvements. Your task is to diagnose and fix these problems while implementing best practices.

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

## 🔧 Getting Started

### 1. Analyze Current Issues
```bash
# Check pipeline status
gh workflow list
gh run list --workflow=pipeline.yml

# Review current pipeline configuration
cat .github/workflows/pipeline.yml

# Test locally
python -m pytest tests/ -v
python scripts/analyze_customers.py data/customers.json
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

## 📊 Success Criteria

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

Good luck! This challenge tests real-world DevOps scenarios you'll encounter on the team. 🛠️