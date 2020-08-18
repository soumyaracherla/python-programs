import unittest
import logging
def modthree(x):                             #defining the function
      return x%3

class Tests(unittest.TestCase):
      def test(self):                                  #test method
          self.assertEqual(modthree(5),2)

if __name__=='__main__':
          unittest.main()
