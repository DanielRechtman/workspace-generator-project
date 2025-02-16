import os
import tempfile
import shutil
import unittest
from create_workspace.workspace_creator import WorkspaceCreator

class TestWorkspaceCreator(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.base_folder = os.path.join(self.test_dir, "test_workspace")

    def tearDown(self):
        # Remove the temporary directory after test
        shutil.rmtree(self.test_dir)

    def test_workspace_creation(self):
        creator = WorkspaceCreator(self.base_folder)
        creator.create_workspace()
        # Check that directories and files have been created
        expected_dirs = [
            os.path.join(self.base_folder, "app", "templates"),
            os.path.join(self.base_folder, "app", "static"),
        ]
        for d in expected_dirs:
            self.assertTrue(os.path.isdir(d))
        expected_files = [
            os.path.join(self.base_folder, "app", "__init__.py"),
            os.path.join(self.base_folder, "app", "main.py"),
            os.path.join(self.base_folder, "app", "templates", "index.html"),
            os.path.join(self.base_folder, "app", "static", "style.css"),
            os.path.join(self.base_folder, "requirements.txt"),
            os.path.join(self.base_folder, "Dockerfile"),
            os.path.join(self.base_folder, "docker-compose.yml"),
            os.path.join(self.base_folder, "README.md"),
        ]
        for f in expected_files:
            self.assertTrue(os.path.isfile(f))

if __name__ == "__main__":
    unittest.main()
