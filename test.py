import unittest
from app import *


class SimplisticTest(unittest.TestCase):
    
    def test_same(self):
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

    def test_estimated_days_diferent(self):
        data = [{"name":"Option 1","type":"Delivery","cost":10,"estimated_days":5},
                {"name":"Option 2","type":"Custom","cost":10,"estimated_days":2},
                {"name":"Option 3","type":"Pickup","cost":10,"estimated_days":3}]

        

        data_ord=[{"name":"Option 2","type":"Custom","cost":10,"estimated_days":2},
                    {"name":"Option 3","type":"Pickup","cost":10,"estimated_days":3},
                    {"name":"Option 1","type":"Delivery","cost":10,"estimated_days":5}
                ]

        #print('Esperada: ' , data_ord)

        response = order_best(data)

        #print('Procesada: ' , response)
        
        self.assertEqual(data_ord, response)
    

    def test_deferent_cost(self):
        data = [{"name":"Option 1","type":"Delivery","cost":6,"estimated_days":3},
                {"name":"Option 2","type":"Custom","cost":5,"estimated_days":3},
                {"name":"Option 3","type":"Pickup","cost":10,"estimated_days":3}]

        data_ord=[{"name":"Option 2","type":"Custom","cost":5,"estimated_days":3},
                {"name":"Option 1","type":"Delivery","cost":6,"estimated_days":3},
                {"name":"Option 3","type":"Pickup","cost":10,"estimated_days":3}]

        response = order_best(data)
        
        self.assertEqual(data_ord, response)

    
    def test_deferent_cost_estimated_days(self):
        data = [{"name":"Option 1","type":"Delivery","cost":10,"estimated_days":5},
                {"name":"Option 2","type":"Custom","cost":5,"estimated_days":3},
                {"name":"Option 3","type":"Pickup","cost":7,"estimated_days":2}]

        data_ord=[{"name":"Option 2","type":"Custom","cost":5,"estimated_days":3},
                {"name":"Option 3","type":"Pickup","cost":7,"estimated_days":2},
                {"name":"Option 1","type":"Delivery","cost":10,"estimated_days":5}]

        response = order_best(data)

        #print('Esperada: ' , data_ord)
        #print('Procesada: ' , response)
        
        self.assertEqual(data_ord, response)