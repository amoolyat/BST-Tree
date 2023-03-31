import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BSTTester(unittest.TestCase):
    
    def setUp(self):
        self.__tree = Binary_Search_Tree()
    
    def test_insert(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.assertEqual('[ 10, 20, 30 ]', self.__tree.in_order())

    def test_mass_insert(self):
        self.__tree.insert_element(40)
        self.__tree.insert_element(65)
        self.__tree.insert_element(20)
        self.__tree.insert_element(90)
        self.__tree.insert_element(10)
        self.__tree.insert_element(3)
        self.__tree.insert_element(87)
        self.assertEqual([3, 10, 20, 40, 65, 87, 90], self.__tree.to_list())
   
    def test_heavy_left_insert_in_order(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.assertEqual('[ 1, 2, 3, 4, 5 ]', self.__tree.in_order())
    
    def test_heavy_left_insert_post_order(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.assertEqual('[ 1, 3, 2, 5, 4 ]', self.__tree.post_order())
    
    def test_heavy_right_insert_in_order(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(11)
        self.assertEqual('[ 5, 6, 8, 9, 11 ]', self.__tree.in_order())

    def test_heavy_right_insert_post_order(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(6)
        self.__tree.insert_element(8)
        self.__tree.insert_element(9)
        self.__tree.insert_element(11)
        self.assertEqual('[ 5, 8, 11, 9, 6 ]', self.__tree.post_order())
    
    def test_insert_duplicate(self):
        with self.assertRaises(ValueError):
            self.__tree.insert_element(30)
            self.__tree.insert_element(30)
        
    def test_remove_empty(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(10)
    
    def test_remove_leaf_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(17)
        self.__tree.insert_element(13)
        self.__tree.insert_element(44)
        self.__tree.insert_element(21)
        self.__tree.insert_element(1)
        self.__tree.insert_element(7)
        self.__tree.remove_element(1)
        self.assertEqual([2, 7, 13, 17, 21, 44], self.__tree.to_list())
        
    def test_remove_leaf_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(17)
        self.__tree.insert_element(13)
        self.__tree.insert_element(44)
        self.__tree.insert_element(21)
        self.__tree.insert_element(1)
        self.__tree.insert_element(7)
        self.__tree.remove_element(1)
        self.assertEqual('[ 13, 2, 7, 21, 17, 44 ]', self.__tree.pre_order())
        
    def test_remove_head_in_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(17)
        self.__tree.insert_element(13)
        self.__tree.insert_element(44)
        self.__tree.insert_element(21)
        self.__tree.insert_element(1)
        self.__tree.insert_element(7)
        self.__tree.remove_element(13)
        self.assertEqual([1, 2, 7, 17, 21, 44], self.__tree.to_list())
        
    def test_remove_head_pre_order(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(17)
        self.__tree.insert_element(13)
        self.__tree.insert_element(44)
        self.__tree.insert_element(21)
        self.__tree.insert_element(1)
        self.__tree.insert_element(7)
        self.__tree.remove_element(13)
        self.assertEqual('[ 17, 2, 1, 7, 21, 44 ]', self.__tree.pre_order())
    
    def test_remove_everything(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(6)
        self.__tree.insert_element(254)
        self.__tree.insert_element(22)
        self.__tree.remove_element(1)
        self.__tree.remove_element(3)
        self.__tree.remove_element(6)
        self.__tree.remove_element(254)
        self.__tree.remove_element(22)
        val = self.__tree.get_height()
        self.assertEqual(0, val)
        
    def test_height_empty(self):
        val = self.__tree.get_height()
        self.assertEqual(0, val)
    
    def test_height_remove(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(1)
        self.__tree.insert_element(6)
        self.__tree.remove_element(6)
        val = self.__tree.get_height()
        self.assertEqual(3, val)
    
    def test_height_insert(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.__tree.insert_element(1)
        self.__tree.insert_element(6)
        val = self.__tree.get_height()
        self.assertEqual(3, val)   

if __name__ == '__main__':
    unittest.main()        
    #res = unittest.main(argv=[''], verbosity=3, exit=False)
