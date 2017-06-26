""" ASSIGNMENT 1- CSE 101 - INTRODUCTION TO PROGRAMMING
Task 1
Neelabhro Roy -2016171
Dewangee Agarwal-2016034"""

import unittest
from a1 import *

class testpoint(unittest.TestCase):
    def testresponse(self):
        self.assertEqual(currency_response('USD','INR',1),'{ "lhs" : "1 United States Dollar", "rhs" : "66.70947 Indian Rupees", "valid" : true, "error" : "" }')
        self.assertEqual(currency_response('LKR','TRY',10),'{ "lhs" : "10 Sri Lankan Rupees", "rhs" : "0.20327091612079 Turkish Liras", "valid" : true, "error" : "" }')
        self.assertEqual(currency_response('HWH','INR',60),'{ "lhs" : "", "rhs" : "", "valid" : false, "error" : "Source currency code is invalid." }')
        self.assertEqual(currency_response('AUD','IND',30),'{ "lhs" : "", "rhs" : "", "valid" : false, "error" : "Exchange currency code is invalid." }')
        self.assertEqual(currency_response('AUD','INR',-100),'{ "lhs" : "-100 Australian Dollars", "rhs" : "-5053.3151328712 Indian Rupees", "valid" : true, "error" : "" }')

        
    def testquery(self):
        self.assertEqual(has_error('{ "lhs" : "1 United States Dollar", "rhs" : "66.70947 Indian Rupees", "valid" : true, "error" : "" }'), False)
        self.assertEqual(has_error('{ "lhs" : "10 Sri Lankan Rupees", "rhs" : "0.20327091612079 Turkish Liras", "valid" : true, "error" : "" }'), False)
        self.assertEqual(has_error('{ "lhs" : "", "rhs" : "", "valid" : false, "error" : "Source currency code is invalid." }'), True)
        self.assertEqual(has_error('{ "lhs" : "", "rhs" : "", "valid" : false, "error" : "Exchange currency code is invalid." }'), True)
        self.assertEqual(has_error('{ "lhs" : "-100 Australian Dollars", "rhs" : "-5053.3151328712 Indian Rupees", "valid" : true, "error" : "" }'), False)
        
        
    def testexchange(self):
        self.assertEqual(exchange('USD','INR',1), 66.70947)
        self.assertEqual(exchange('LKR','TRY',10), 0.20327091612079)
        self.assertEqual(exchange('HWH','INR',60), -1)
        self.assertEqual(exchange('AUD','IND',30), -1)
        self.assertEqual(exchange('AUD','INR',-100), -5053.3151328712)
        
        



if __name__=='__main__':
    unittest.main()
