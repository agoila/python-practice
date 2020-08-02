
# Problems with your probability_uniform Function

Your `probability_uniform` function should work at this point. But, you might run into a couple of problems. 

1. What happens if you call your function like this: `probability_range(35, 20, 0, 360)` ?
2. What happens if you input an angle that is outside the possibilities of the bottle's possible outcomes like probability_range(-25, 390, 0, 360)?
3. What if you call your function like this: probability_range('a', 'b', 0, 360)?

When writing functions, it's important to think of edge cases or incorrect user input. 

# Your Task

Your task is to improve your function. Let's make these changes one step at a time. 

# Task One

Make sure the function outputs a valid probability when low_range is greater than high_range.

There is more than one way to go about this. You could:
1. Calculate the absolute value of high_range - low_range 
2. Use if statements to compare low_range and high_range to see which one is greater

Here is a [link](https://docs.python.org/2/library/functions.html#abs) to using Python's absolute value function.

Fill out the TODOs below.


```python
def probability_range_improved(low_range, high_range, minimum, maximum):

    # TODO: calulate and return the probability 
    # even if low range is greater than high range.
    # Use the abs() function or if statements
    probability = (abs(high_range - low_range)) / (maximum - minimum)
    return probability
```

Run the cell below to see if your function works as expected.


```python
assert "{0:.2f}".format(probability_range_improved(25, 700, 5, 800)) == '0.85'
assert "{0:.2f}".format(probability_range_improved(700, 25, 5, 800)) == '0.85'
print('Nice work!')
```

    Nice work!


# Task Two

Check the inputs to the function to make sure they are not strings. If the user inputted a string, the function should return None. 

This exercise might seem trivial, but if you try to do something like `'my_string'/2` in Python, you will get an error. Debugging the errors and avoiding them is a key programming skill. 

Hint: Use the Python isinstance() function. If you're not sure how to use this function, search for it online.

Hint: Use your code from Task One to calculate the probability


```python
def probability_range_improved(low_range, high_range, minimum, maximum):

    # TODO: check if any of the inputs are strings.
    # hint: the python function isinstance() will be useful
    inputs = [low_range, high_range, minimum, maximum]
    if (any(isinstance(i, str) for i in inputs)):
        # print a message to the user and return none
        print('Inputs should be numbers not string')
        return None
    probability = (abs(high_range - low_range)) / (maximum - minimum)
    return probability
```

Run the next cell to check your results.


```python
assert probability_range_improved('a', 0, -100, 500) == None
assert probability_range_improved(5, 'b', -100, 500) == None

assert "{0:.2f}".format(probability_range_improved(25, 700, 5, 800)) == '0.85'
assert "{0:.2f}".format(probability_range_improved(700, 25, 5, 800)) == '0.85'

print('Well done!')
```

    Inputs should be numbers not string
    Inputs should be numbers not string
    Well done!


# Task Three

Check that the user has only inputted low_range and high_range values that are in between the allowed minimum and maximum. If an input is out of the allowed range, return None. 

Hint: Use your code from Task One to calculate the probability


```python
def probability_range_improved(low_range, high_range, minimum, maximum):
    
    # TODO check that low_range is between minimum and maximum
    if (low_range < minimum or low_range > maximum):
        # print a message to the user and return none
        print('Your low range value must be between minimum and maximum')
        return None
        
    # TODO check that high_range is between min and max
    if (high_range < minimum or high_range > maximum):
        # print a message to the user and return none
        print('The high range value must be between minimum and maximum')
        return None

    probability = (abs(high_range - low_range)) / (maximum - minimum)
    return probability

```

Run the next code cell to check your results.


```python
assert probability_range_improved(-100, 300, 100, 500) == None
assert probability_range_improved(105, 700, 100, 500) == None

assert "{0:.2f}".format(probability_range_improved(25, 700, 5, 800)) == '0.85'
assert "{0:.2f}".format(probability_range_improved(700, 25, 5, 800)) == '0.85'

print('Awesome!')
```

    Your low range value must be between minimum and maximum
    The high range value must be between minimum and maximum
    Awesome!


# Task Four

Take all of your work from task one, two and three. Put them into one final function.


```python
def probability_range_improved(low_range, high_range, minimum, maximum):

    # TODO: check if any of the inputs are strings.
    # hint: the python function isinstance() will be useful
    inputs = [low_range, high_range, minimum, maximum]
    if (any(isinstance(i, str) for i in inputs)):
        # print a message to the user and return none
        print('Inputs should be numbers not string')
        return None
    
    # TODO check that low_range is between minimum and maximum
    if (low_range < minimum or low_range > maximum):
        # print a message to the user and return none
        print('Your low range value must be between minimum and maximum')
        return None
        
    # TODO check that high_range is between min and max
    if (high_range < minimum or high_range > maximum):
        # print a message to the user and return none
        print('The high range value must be between minimum and maximum')
        return None

    # TODO: calulate and return the probability 
    # even if low range is greater than high range
    probability = (abs(high_range - low_range)) / (maximum - minimum)
    return probability

```

Run the cell below. If there are no AssertionErrors, then your code runs as expected. In Python, assert checks whether a statement
resolves to True or False


```python
assert probability_range_improved('a', 0, -100, 500) == None
assert probability_range_improved(0, 'b', -100, 500) == None
assert probability_range_improved(-100, 300, 100, 500) == None
assert probability_range_improved(105, 700, 100, 500) == None
assert "{0:.2f}".format(probability_range_improved(25, 700, 5, 800)) == '0.85'
assert "{0:.2f}".format(probability_range_improved(700, 25, 5, 800)) == '0.85'
print('You got the results we were looking for!')
```

    Inputs should be numbers not string
    Inputs should be numbers not string
    Your low range value must be between minimum and maximum
    The high range value must be between minimum and maximum
    You got the results we were looking for!

