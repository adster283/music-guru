import unittest
from server import searchSong

class TestSearchFunction(unittest.TestCase):

    
    def test_search1950(self):
        data = searchSong(1950, testing=True)
        self.assertEqual(str(data[0]), data[1].split(".")[0], data)
        
    def test_search1975(self):
        data = searchSong(1975, testing=True)
        self.assertEqual(str(data[0]), data[1].split(".")[0], data)
        
    def test_search1999(self):
        data = searchSong(1999, testing=True)
        self.assertEqual(str(data[0]), data[1].split(".")[0], data)
        
    def test_search2000(self):
        data = searchSong(2000, testing=True)
        self.assertEqual(str(data[0]), data[1].split(".")[0], data)
        
    def test_search2009(self):
        data = searchSong(2009, testing=True)
        self.assertEqual(str(data[0]), data[1].split(".")[0], data)
        

        
if __name__ == '__main__':
    unittest.main()
    