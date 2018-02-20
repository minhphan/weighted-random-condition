import numpy as np
import sys
import ast
import csv
import utils

class RandomMessage:
    def __init__(self, w):
        '''
        Generates random messages

        # Parameter
        -------------
        w: np.array
            Weighted random condition.

        # Returns
        -------------
        sample: integer
            Single random message.
        '''

        self.w = w
        self.N = len(w)
        # We assign each message version with a unique ID from 0 to N-1
        self.setN = np.arange(self.N)
        self.M = sum(w)
        # w/self.M will generate an array of 0s, use numpy divide 
        self.norm_w = np.true_divide(w,self.M)
        # We randomize M message from N version for only 1 time
        if self.M < 6:
            self.shuffle = np.random.choice(self.setN, self.M, p=self.norm_w)
        else:
            # Use bcolz to store array > 1MB to speed up computation
            utils.save_array("shuffle.bc", np.random.choice(self.setN, self.M, p=self.norm_w))
            self.shuffle = utils.load_array("shuffle.bc")
        # Everytime we call the message function that take a random message, 
        # we increase current_id for the next message
        self.current_id = 0
    
    # Everytime we run this function, it will simply take the next sample
    # in our randomized messages.
    def message(self):
        sample = self.shuffle[self.current_id]
        self.current_id += 1
        return sample

def main():
    w = utils.csv_to_array(sys.argv[1])
    samples = RandomMessage(w)
    args = sys.argv[2:]
    randomized_msgs = samples.shuffle
    # Handle Command-Line Flags
    # -export random messages to csv file, each message is a row
    if '-export' in args:
        print("yes")
        utils.array_to_csv(randomized_msgs, "RandomMessage.csv")    
    # Pass object to any program to use it    
    return samples

if __name__ == "__main__":
    main()
