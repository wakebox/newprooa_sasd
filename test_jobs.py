#!/usr/bin/env python3
"""
Tests for the job management system.
"""

import os
import unittest
from datetime import datetime
from jobs import JobManager


class TestJobManager(unittest.TestCase):
    """Test cases for JobManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_file = "test_jobs.json"
        self.manager = JobManager(self.test_file)
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_job(self):
        """Test adding a job."""
        self.manager.add_job("Test Job", "2025-10-01", "Test description")
        self.assertEqual(len(self.manager.jobs), 1)
        self.assertEqual(self.manager.jobs[0]["title"], "Test Job")
        self.assertEqual(self.manager.jobs[0]["date"], "2025-10-01")
        self.assertEqual(self.manager.jobs[0]["description"], "Test description")
    
    def test_list_today_jobs(self):
        """Test listing today's jobs."""
        today = datetime.now().strftime("%Y-%m-%d")
        tomorrow = "2025-12-31"
        
        self.manager.add_job("Today's Job", today, "Should appear")
        self.manager.add_job("Future Job", tomorrow, "Should not appear")
        
        today_jobs = self.manager.list_today_jobs()
        self.assertEqual(len(today_jobs), 1)
        self.assertEqual(today_jobs[0]["title"], "Today's Job")
    
    def test_list_all_jobs(self):
        """Test listing all jobs."""
        self.manager.add_job("Job 1", "2025-10-01")
        self.manager.add_job("Job 2", "2025-10-02")
        
        all_jobs = self.manager.list_all_jobs()
        self.assertEqual(len(all_jobs), 2)
    
    def test_empty_jobs(self):
        """Test with no jobs."""
        today_jobs = self.manager.list_today_jobs()
        self.assertEqual(len(today_jobs), 0)
        
        all_jobs = self.manager.list_all_jobs()
        self.assertEqual(len(all_jobs), 0)
    
    def test_persistence(self):
        """Test that jobs are saved and loaded correctly."""
        self.manager.add_job("Persistent Job", "2025-10-01", "Test")
        
        # Create a new manager instance to test loading
        new_manager = JobManager(self.test_file)
        self.assertEqual(len(new_manager.jobs), 1)
        self.assertEqual(new_manager.jobs[0]["title"], "Persistent Job")


if __name__ == "__main__":
    unittest.main()
