# from subdirectory.filename import function_name
import unittest

from functions.files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):

    def test_get_files_info(self):

        print(get_files_info("calculator", "."))
        print(get_files_info("calculator", "pkg"))
        print(get_files_info("calculator", ":/bin"))
        print(get_files_info("calculator", "../"))


if __name__ == '__main__':
    unittest.main()