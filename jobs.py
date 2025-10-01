#!/usr/bin/env python3
"""
Job management system for tracking and listing jobs.
"""

import json
import os
from datetime import datetime
from typing import List, Dict


class JobManager:
    """Manages jobs with dates."""
    
    def __init__(self, data_file: str = "jobs.json"):
        """Initialize the job manager.
        
        Args:
            data_file: Path to the JSON file storing jobs.
        """
        self.data_file = data_file
        self.jobs = self._load_jobs()
    
    def _load_jobs(self) -> List[Dict]:
        """Load jobs from the data file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def _save_jobs(self):
        """Save jobs to the data file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.jobs, f, indent=2)
    
    def add_job(self, title: str, date: str, description: str = ""):
        """Add a new job.
        
        Args:
            title: Job title.
            date: Job date in YYYY-MM-DD format.
            description: Optional job description.
        """
        job = {
            "title": title,
            "date": date,
            "description": description,
            "created_at": datetime.now().isoformat()
        }
        self.jobs.append(job)
        self._save_jobs()
    
    def list_today_jobs(self) -> List[Dict]:
        """List all jobs scheduled for today.
        
        Returns:
            List of jobs scheduled for today.
        """
        today = datetime.now().strftime("%Y-%m-%d")
        return [job for job in self.jobs if job.get("date") == today]
    
    def list_all_jobs(self) -> List[Dict]:
        """List all jobs.
        
        Returns:
            List of all jobs.
        """
        return self.jobs


def main():
    """Main CLI interface."""
    import sys
    
    manager = JobManager()
    
    if len(sys.argv) < 2:
        print("Usage: python jobs.py [command] [args...]")
        print("Commands:")
        print("  add <title> <date> [description]  - Add a new job")
        print("  today                              - List today's jobs")
        print("  all                                - List all jobs")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 4:
            print("Error: add requires title and date")
            print("Usage: python jobs.py add <title> <date> [description]")
            sys.exit(1)
        title = sys.argv[2]
        date = sys.argv[3]
        description = sys.argv[4] if len(sys.argv) > 4 else ""
        manager.add_job(title, date, description)
        print(f"Job added: {title} on {date}")
    
    elif command == "today":
        jobs = manager.list_today_jobs()
        if not jobs:
            print("No jobs scheduled for today.")
        else:
            print(f"Jobs for today ({datetime.now().strftime('%Y-%m-%d')}):")
            for i, job in enumerate(jobs, 1):
                print(f"{i}. {job['title']}")
                if job.get('description'):
                    print(f"   Description: {job['description']}")
    
    elif command == "all":
        jobs = manager.list_all_jobs()
        if not jobs:
            print("No jobs found.")
        else:
            print("All jobs:")
            for i, job in enumerate(jobs, 1):
                print(f"{i}. {job['title']} - {job['date']}")
                if job.get('description'):
                    print(f"   Description: {job['description']}")
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
