def probability_range_improved(low_range, high_range, minimum, maximum):
    
    inputs = [low_range, high_range, minimum, maximum]
    if (any(isinstance(i, str) for i in inputs)):
        # print a message to the user and return none
        print('Inputs should be numbers not string')
        return None
    
    if (low_range < minimum or low_range > maximum):
        # print a message to the user and return none
        print('Your low range value must be between minimum and maximum')
        return None
        
    if (high_range < minimum or high_range > maximum):
        # print a message to the user and return none
        print('The high range value must be between minimum and maximum')
        return None

    # TODO: calulate and return the probability 
    # even if low range is greater than high range
    probability = (abs(high_range - low_range)) / (maximum - minimum)
    return probability

assert probability_range_improved('a', 0, -100, 500) == None
assert probability_range_improved(0, 'b', -100, 500) == None
assert probability_range_improved(-100, 300, 100, 500) == None
assert probability_range_improved(105, 700, 100, 500) == None
assert "{0:.2f}".format(probability_range_improved(25, 700, 5, 800)) == '0.85'
assert "{0:.2f}".format(probability_range_improved(700, 25, 5, 800)) == '0.85'
