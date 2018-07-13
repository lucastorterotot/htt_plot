import unittest

from task import Task

class TestTask(unittest.TestCase):
     
     def test_1_create(self):
          t1 = Task('t1', {'a': float, 'b': list}, {'c':int})
          with self.assertRaises(ValueError) as err:
               t2 = Task('t1', {}, {})
          print t1
          with self.assertRaises(ValueError) as err:
               t2 = Task('t1', 0, {})
          with self.assertRaises(ValueError) as err:
               t2 = Task('t1', {}, [])
          
               
          
if __name__ == '__main__':
     unittest.main()
