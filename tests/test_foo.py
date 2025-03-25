import unittest



class TestEntity(unittest.TestCase):
    """  Gerüst für Unit tests """
    def test_basix(self):
        self.assertTrue(2 == 1+1)

if __name__ == '__main__':
    unittest.main()
    
    
    
