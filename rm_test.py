import numpy as np
import math
import random_message
import sys

def weights_versions_test(log_max_weight = 9, 
                               log_max_N = 3):
    '''
    Test with different weights and versions
    '''
    esp = 10**(-log_max_weight) # Our criteria
    
    # Try different weights and versions
    test_weights = [int(n) for n in 10**np.linspace(0,log_max_weight,10)]
    test_Ns = [int(n) for n in 10**np.linspace(0,log_max_N,10)] 
    
    # Result of each test case
    ret_T = []

    for tw in test_weights:
        for N in test_Ns:
            # Init random weights
            w = np.random.randint(0,tw,N)
            samples = RandomMessage(w)
            # A counting dict with default value of 0 
            # for all message version in setN
            count_setN_randomized = dict.fromkeys(samples.setN,0)
            # Go through the entire sampled messages
            # Count how many each version appears 
            for message in samples.shuffle:
                if message in samples.setN:
                    count_setN_randomized[message] += 1
            # Normalize our weight so that \sum^N_{i=1}w_i = 1
            norm_w_sample = [v / samples.M for k, v in count_setN_randomized.items()]
            # Measure the difference between our posterior weight and the prior weight
            t = sum(norm_w_sample - samples.norm_w)/samples.N
            ret_T.append(t)
            if not math.isnan(float(t)):
                # If our criteria is violated, stop the test and see where the problem is
                assert esp>=abs(t), "weight= %s" % w

    print("%s test cases passed" % len(ret_T))            
    
if __name__ == "__main__":
    action = sys.argv[1:]
    # The program will get killed if weight $\geq 10^7$
    if "-full" in action:
        weights_versions_test()
    # The default test will only run with max weight 10^6 and 100 versions    
    else:
        weights_versions_test(6,2)
    