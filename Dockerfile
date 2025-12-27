# TODO: DevOps should create proper Dockerfile
# Current state: INCOMPLETE - needs multi-stage build, security hardening

FROM python:3.11-slim

# BUG: Running as root - security risk
# BUG: No build optimization
# BUG: Missing health checks
# BUG: No proper logging setup

WORKDIR /app

# TODO: Add proper build stages (build, runtime)
# TODO: Add non-root user
# TODO: Add security scanning
# TODO: Optimize layer caching

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# BUG: Exposing port but not configurable
EXPOSE 8000

# TODO: Add health check endpoint
# TODO: Add proper startup scripts
# TODO: Add monitoring setup

CMD ["python", "scripts/analyze_customers.py", "data/customers.json"]