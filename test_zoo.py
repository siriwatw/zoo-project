import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_invalid(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)

    def test_newborn(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    
    def test_teen(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
    
    def test_adult(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_elder(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)


if __name__ == '__main__':
    unittest.main()