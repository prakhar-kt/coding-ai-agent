# from subdirectory.filename import function_name
import unittest
    
from functions.run_file import run_python_file

class TestGetFilesInfo(unittest.TestCase):

    def test_get_files_info(self):

        print(run_python_file("calculator", "main.py"))
        print(run_python_file("calculator", "tests.py"))
        print(run_python_file("calculator", "../main.py"))
        print(run_python_file("calculator", "nonexistent.py"))


if __name__ == '__main__':
    unittest.main()