import unittest
def add(a,b):
    return a + b

class test(unittest.TestCase):
    def testpositive(self):
        self.assertEqual(add(9,5),14)

    def testnegative(self):
        self.assertEqual(add(-1,-2),-3)

if __name__=="__main__":
    unittest.main()