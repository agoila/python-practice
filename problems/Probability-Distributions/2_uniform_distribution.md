
# Uniform Probability Distribution

### Your Task

Let's get started! In this exercise, you'll write a function for calculating continuous uniform probability distributions.

### Continuous Uniform Distribution

From the lesson videos, the wheel of fortune and spinning bottle examples both had continuous uniform distributions. You spin, and the arrow or bottle had an equal chance of stopping anywhere between 0 and 360 degrees. 

### Instructions
For this first programming exercise, write a function that calculates the probability that the arrow will stop between two angles. You'll want this function to work with any continuous uniform distribution not just a wheel or bottle. 

As an example: the probability that the bottle stops between 20 and 30 degrees is P = (30 - 20) / (360 - 0).

The function has four inputs:
* `low_range` representing the first angle of interest
* `high_range` representing the second angle
* `minimum` representing the minimum value of the distribution (0 for the spinning example)
* `maximum` representing the maximum value of the distribution (360 for the spinning example)

The output should be the probability that the arrow stops between low_range and high_range.

Assume low_range < high_range.


```python
def probability_uniform(low_range, high_range, minimum, maximum):
    
    ## TODO: Calculate the probability of an event occurring 
    ## between low_range and high_range.
    ## Assume the user has given valid inputs such that low_range < high_range.
    ##   minimum < maximum
    ##

    probability = (high_range - low_range) / (maximum - minimum) 
    
    return probability
```

# Test Your Results

Run the code cell below to test your results. If you get an assertion error, that means your answer was not what we expected.


```python
## TODO: Test your results by running this cell.
## If the cell produces no output, your answer was as expected

assert "{0:.2f}".format(probability_uniform(15, 305, 0, 360)) == '0.81'
assert "{0:.2f}".format(probability_uniform(1, 5, 0, 10)) == '0.40'
assert "{0:.2f}".format(probability_uniform(55, 70, 20, 300)) == '0.05'
print('Great work! Your code outputs the expected results.')
```

    Great work! Your code outputs the expected results.

