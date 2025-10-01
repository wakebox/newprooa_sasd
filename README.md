# newprooa_sasd

[![CI](https://github.com/wakebox/newprooa_sasd/actions/workflows/ci.yml/badge.svg)](https://github.com/wakebox/newprooa_sasd/actions/workflows/ci.yml)

## CI/CD Jobs

This repository includes the following automated jobs:

### Build Job
- Runs on every push and pull request
- Builds the project

### Test Job
- Runs on every push and pull request
- Executes the test suite

### Lint Job
- Runs on every push and pull request
- Checks code style and formatting

### Deploy Job
- Runs only on main branch after build, test, and lint pass
- Deploys the application

### Security Scan Job
- Runs on every push and pull request
- Performs security vulnerability scanning

### Code Quality Job
- Runs on every push and pull request
- Analyzes code quality metrics