from files.text import ReadTextFile
import unittest


class TestReadFile(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_readcsvfile(self):
        csv_file = ReadTextFile('iris.csv')
        self.assertEqual(csv_file.read_first_two(), '\n'.join(['"sepal.length","sepal.width","petal.length","petal.width","variety"\n',
                         '5.1,3.5,1.4,.2,"Setosa"\n']))


    def test_readtextfile(self):
        text_file = ReadTextFile('numbers.txt')
        self.assertEqual(text_file.read_last_two(), '\n'.join(['44\n', '31']))


if __name__ == "__main__":
    unittest.main()

# print('a')
