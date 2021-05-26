import unittest
from app import *


class SimplisticTest(unittest.TestCase):
    
    def test(self):
        data = [{'name': 'Option 1', 'type': 'Delivery', 'cost': 10, 'estimated_days': 3}, 
                {'name': 'Option 2', 'type': 'Custom', 'cost': 10, 'estimated_days': 3}, 
                {'name': 'Option 3', 'type': 'Pickup', 'cost': 10, 'estimated_days': 3}]

        data_ord=[{'name': 'Option 1', 'type': 'Delivery', 'cost': 10, 'estimated_days': 3}, 
                {'name': 'Option 2', 'type': 'Custom', 'cost': 10, 'estimated_days': 3}, 
                {'name': 'Option 3', 'type': 'Pickup', 'cost': 10, 'estimated_days': 3}] 

        response = order_best(data)
        
        self.assertEqual(data_ord, response)

    def test_vacio(self):
        data = []

        data_ord=[] 

        response = order_best(data)
        
        self.assertEqual(data_ord, response)