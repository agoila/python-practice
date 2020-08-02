def probability_uniform(low_range, high_range, minimum, maximum):

    probability = (high_range - low_range) / (maximum - minimum) 
    
    return probability

# Test Your Results
assert "{0:.2f}".format(probability_uniform(15, 305, 0, 360)) == '0.81'
assert "{0:.2f}".format(probability_uniform(1, 5, 0, 10)) == '0.40'
assert "{0:.2f}".format(probability_uniform(55, 70, 20, 300)) == '0.05'
