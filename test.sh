#!/bin/bash
# Test with different weights and number of versions
python rm_test.py 

# Generate _test_weight.csv with random weights
python -c 'from utils import create_test_csv; create_test_csv("_test_weight.csv",10**3,50)' 
# Test csv input function, export result to a file
python random_message.py _test_weight.csv -export
