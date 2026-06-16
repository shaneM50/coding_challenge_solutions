import unittest
from src.container_of_integers import Container

class ContainerTestCase(unittest.TestCase):

    def setUp(self):
        self.container = Container()
        
    def test_internal_order_after_random_adds(self):
        values = [5, 1, 4, 2, 3]
        for v in values:
            self.container.add(v)

        self.assertEqual(self.container.data, [1, 2, 3, 4, 5])

    def test_delete_removes_only_one_occurrence(self):
        self.container.add(5)
        self.container.add(5)
        self.container.add(5)

        self.assertEqual(self.container.delete(5), True)
        # should still have two 5s left
        self.assertEqual(self.container.data, [5, 5])

    def test_median_after_deletes_around_middle(self):
        for v in [1, 2, 3, 4, 5, 6]:
            self.container.add(v)
        # data: [1, 2, 3, 4, 5, 6], median index (even) -> 2 => value 3
        self.assertEqual(self.container.get_median(), 3)

        self.assertTrue(self.container.delete(3))
        # now [1, 2, 4, 5, 6], len=5, median index 2 => 4
        self.assertEqual(self.container.get_median(), 4)


    def test_singleElementMedian(self):
        self.container.add(1)
        self.assertEqual(self.container.get_median(), 1)
    
    def test_emptyListMedian(self):
        self.assertRaises(RuntimeError, self.container.get_median)
    
    def test_twoElementsAddedInOrderMedian(self):
        self.container.add(2)
        self.container.add(3)
        self.assertEqual(self.container.get_median(), 2)
    
    def test_twoElementsAddedReverseOrderMedian(self):
        self.container.add(3)
        self.container.add(2)
        self.assertEqual(self.container.get_median(), 2)
    
    def test_multipleOddElementsMedian(self):
        self.container.add(2)
        self.container.add(1)
        self.container.add(3)
        self.assertEqual(self.container.get_median(), 2)
    
    def test_multipleEvenElementsMedian(self):
        self.container.add(2)
        self.container.add(1)
        self.container.add(3)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 2)

    
    def test_singleElementDelete(self):
        self.container.add(1)
        self.assertEqual(self.container.delete(1), True)
    
    def test_singleElementNoDelete(self):
        self.container.add(1)
        self.assertEqual(self.container.delete(2), False)
        
    def test_emptyDelete(self):
        self.assertEqual(self.container.delete(2), False)
    
    def test_twoElementDelete(self):
        self.container.add(1)
        self.container.add(2)
        self.assertEqual(self.container.delete(1), True)

    def test_basic1(self):
        self.container.add(1)
        self.container.add(2)
        self.container.add(5)
        self.container.add(4)
        self.assertEqual(self.container.get_median(), 2)
        self.assertEqual(self.container.delete(1), True)
        self.assertEqual(self.container.get_median(), 4)

   
    def test_basic2(self):
        self.container.add(5)
        self.container.add(3)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 5)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.delete(5), False)
        self.assertEqual(self.container.get_median(), 3)
        self.assertEqual(self.container.delete(2), False)
        self.assertEqual(self.container.delete(3), True)
        self.assertRaises(Exception, self.container.get_median)
        self.container.add(1)
        self.container.add(1)
        self.container.add(2)
        self.container.add(2)
        self.container.add(2)
        self.assertEqual(self.container.get_median(), 2)
        self.assertEqual(self.container.delete(2), True)
        self.assertEqual(self.container.get_median(), 1)
        self.assertEqual(self.container.delete(1), True)
        self.assertEqual(self.container.get_median(), 2)

    def test_basic3(self):
        self.assertEqual(self.container.delete(4), False)
        self.assertRaises(Exception, self.container.get_median)
        for i in range(10, 0, -1):
            self.container.add(i)
        self.assertEqual(self.container.get_median(), 5)
        for i in range(4, 7):
            self.assertEqual(self.container.delete(i), True)
        self.assertEqual(self.container.get_median(), 7)
    

    def test_01_simpleGetOddLength(self):
        self.container.add(1)
        self.container.add(2)
        self.container.add(5)
        self.container.add(7)
        self.container.add(9)
        self.assertEqual(self.container.get_median(), 5)
        self.container.add(3)
        self.container.add(4)
        self.assertEqual(self.container.get_median(), 4)


    def test_02_simpleGetEvenLength(self):
        self.container.add(30)
        self.container.add(10)
        self.assertEqual(self.container.get_median(), 10)
        self.container.add(12)
        self.container.add(35)
        self.assertEqual(self.container.get_median(), 12)
        self.assertEqual(self.container.get_median(), 12)
        self.container.add(11)
        self.container.add(40)
        self.container.add(100)
        self.container.add(90)
        self.assertEqual(self.container.get_median(), 30)


    def test_03_simpleMixedAddAndGet(self):
        self.assertRaises(Exception, self.container.get_median)
        self.assertRaises(Exception, self.container.get_median)
        self.container.add(1)
        self.assertEqual(self.container.get_median(), 1)
        self.container.add(3)
        self.container.add(4)
        self.container.add(2)
        self.container.add(10)
        self.container.add(30)
        self.assertEqual(self.container.get_median(), 3)
        self.container.add(52)
        self.container.add(53)
        self.container.add(54)
        self.container.add(55)
        self.assertEqual(self.container.get_median(), 10)
        self.container.add(6)
        self.container.add(7)
        self.container.add(8)
        self.container.add(9)
        self.assertEqual(self.container.get_median(), 8)
        self.container.add(11)
        self.assertEqual(self.container.get_median(), 9)


    def test_04_repetitions1(self):
        self.container.add(1)
        self.container.add(2)
        self.container.add(3)
        self.container.add(4)
        self.container.add(5)
        self.container.add(5)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 4)
        self.container.add(2)
        self.assertEqual(self.container.get_median(), 3)
        self.container.add(3)
        self.assertEqual(self.container.get_median(), 3)
        self.container.add(5)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 4)


    def test_05_repetitions2(self):
        for _ in range(20):
            self.container.add(42)
        self.assertEqual(self.container.get_median(), 42)
        for i in range(30):
            self.container.add(i)
        self.assertEqual(self.container.get_median(), 24)
        for _ in range(50):
            self.container.add(130)
        self.assertEqual(self.container.get_median(), 42)
        for _ in range(50):
            self.container.add(170)
        self.assertEqual(self.container.get_median(), 130)

 
    def test_06_simpleDeletes1(self):
        self.container.add(10)
        self.container.add(20)
        self.container.add(30)
        self.assertEqual(self.container.delete(20), True)
        self.assertEqual(self.container.get_median(), 10)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 10)
        self.assertEqual(self.container.delete(30), True)
        self.assertEqual(self.container.get_median(), 5)

  
    def test_07_simpleDeletes2(self):
        self.assertRaises(Exception, self.container.get_median)
        self.assertEqual(self.container.delete(5), False)
        self.assertRaises(Exception, self.container.get_median)
        self.assertEqual(self.container.delete(5), False)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 5)
        self.assertEqual(self.container.delete(5), True)
        self.assertRaises(Exception, self.container.get_median)
        self.assertEqual(self.container.delete(5), False)
        self.container.add(5)
        self.container.add(4)
        self.container.add(3)
        self.assertEqual(self.container.get_median(), 4)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.get_median(), 3)
        self.assertEqual(self.container.delete(5), False)
        self.assertEqual(self.container.delete(3), True)
        self.assertEqual(self.container.get_median(), 4)

  
    def test_08_repetitionsAndDeletes(self):
        self.container.add(3)
        self.container.add(30)
        self.container.add(30)
        self.container.add(15)
        self.assertEqual(self.container.get_median(), 15)
        self.assertEqual(self.container.delete(30), True)
        self.assertEqual(self.container.get_median(), 15)
        self.assertEqual(self.container.delete(30), True)
        self.assertEqual(self.container.get_median(), 3)
        self.container.add(30)
        self.container.add(30)
        self.container.add(30)
        self.assertEqual(self.container.get_median(), 30)
        self.container.add(15)
        self.assertEqual(self.container.get_median(), 15)
        self.assertEqual(self.container.delete(20), False)
        self.assertEqual(self.container.delete(3), True)
        self.assertEqual(self.container.get_median(), 30)

   
    def test_09_mixedOperations1(self):
        self.container.add(5)
        self.container.add(3)
        self.container.add(5)
        self.container.add(7)
        self.container.add(8)
        self.container.add(9)
        self.assertEqual(self.container.get_median(), 5)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.delete(8), True)
        self.assertEqual(self.container.get_median(), 5)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.delete(5), False)
        self.assertEqual(self.container.get_median(), 7)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 5)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.delete(5), False)
        self.assertEqual(self.container.delete(7), True)
        self.assertEqual(self.container.delete(3), True)
        self.assertEqual(self.container.get_median(), 9)
        self.assertEqual(self.container.delete(9), True)
        self.assertRaises(Exception, self.container.get_median)
        self.assertEqual(self.container.delete(9), False)
        self.assertRaises(Exception, self.container.get_median)


    def test_10_mixedOperations2(self):
        for i in range(100):
            self.container.add(i)
            self.container.add(i)
        self.assertEqual(self.container.get_median(), 49)
        answers = [
            50, 50, 51, 51, 52, 52, 53, 53, 54, 54, 55, 55, 56,
            56, 57, 57, 58, 58, 59, 59, 60, 60, 61, 61, 62, 62,
            63, 63, 64, 64, 65, 65, 66, 66, 67, 67, 68, 68, 69,
            69, 70, 70, 71, 71, 72, 72, 73, 73, 74, 74
        ]
        for i in range(50):
            self.assertEqual(self.container.delete(i), True)
            self.assertEqual(self.container.delete(i), True)
            self.assertEqual(self.container.delete(i), False)
            self.assertEqual(self.container.get_median(), answers[i])

        for i in range(100):
            self.assertEqual(
                self.container.delete(i),
                False if i < 50 else True
            )
        self.assertEqual(self.container.get_median(), 74)

if __name__ == '__main__':
	unittest.main()