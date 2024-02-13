""" Configuration for the pytest tests."""

import pytest
import git
import os

@pytest.fixture(scope="session")
def get_data():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_data_dir = os.path.join(test_dir, "pytritech_testdata")
    
    if not os.path.exists(test_data_dir):
        # Download data to test_data_dir via git
        repo_clone_url = "https://github.com/OniDaito/pytritech_testdata.git"
        repo = git.Repo.clone_from(repo_clone_url, test_data_dir)
        repo.git.checkout("main")
  
    return test_data_dir
