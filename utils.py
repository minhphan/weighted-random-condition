import csv
import numpy as np
import bcolz

# Create an on-disk carray container
def save_array(path, arr): 
    c=bcolz.carray(arr, rootdir=path, mode='w') 
    c.flush()

def load_array(path): 
    return bcolz.open(path)[:]

def csv_to_array(csv_path):
    '''
    The csv file must has each weight in a row
    50
    30
    50
    '''
    csvfile = open(csv_path, 'r')
    reader = csv.reader(csvfile, delimiter='\t')
    my_list = list(reader)
    w = []
    for i in range(len(my_list)):
        if not str.isdigit(*my_list[i]):
            raise ValueError('Value %s at row %s in the csv file is not an positive integer. \
                Change the weight to an integer.' 
                % (my_list[i][0], i+1))
        elif int(*my_list[i]) > 10**9:
            raise ValueError('Weight %s at row %s in the csv file should be less than 10^9' 
                % (my_list[i][0], i+1))
        else:
            w.append(int(*my_list[i]))

    return w       

def array_to_csv(w, name):
    w = [[i] for i in w]
    with open(name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(w)

# Generate a csv with random weights
def create_test_csv(name="_test_weight.csv",
                    max_weight=10**3,
                    max_version=10):
    w = np.random.randint(0, max_weight, max_version)
    array_to_csv(w, name)
