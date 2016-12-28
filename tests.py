import unittest
import main

class MyTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main.main(0), "Hello World")
        
    def test_main_two(self):
        self.assertEqual(main.main(1), "argument")
        
        
if __name__ == '__main__':
    unittest.main()
