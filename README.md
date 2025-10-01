# newprooa_sasd

A simple job management system for tracking and listing jobs.

## Features

- Add jobs with dates and descriptions
- List jobs scheduled for today
- List all jobs
- Persistent storage using JSON

## Usage

### List Today's Jobs

To list all jobs scheduled for today:

```bash
python3 jobs.py today
```

### Add a Job

To add a new job:

```bash
python3 jobs.py add "Job Title" "YYYY-MM-DD" "Optional description"
```

Example:
```bash
python3 jobs.py add "Team meeting" "2025-10-01" "Discuss Q4 roadmap"
```

### List All Jobs

To list all jobs:

```bash
python3 jobs.py all
```

## Running Tests

To run the test suite:

```bash
python3 test_jobs.py
```

## Requirements

- Python 3.6 or higher