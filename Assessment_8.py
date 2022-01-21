#!/usr/bin/env python
# coding: utf-8

# 1. Is the Python Standard Library included with PyInputPlus?
# Ans. PyInputPlus is not a part of the Python Standard Library, so you must install it separately using Pip
# 2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
# Ans. PyInputPlus contains functions similar to input() for several kinds of data: numbers, dates, email addresses, and more. If the user ever enters invalid input, such as a badly formatted date or a number that is outside of an intended range, PyInputPlus will reprompt them for input just like our code in the previous section did. PyInputPlus also has other useful features like a limit for the number of times it reprompts users and a timeout if users are required to respond within a time limit.
# 
# 3. How do you distinguish between inputInt() and inputFloat()?
# inputInt(), and inputFloat() functions, which accept int and float numbers, also have min, max, greaterThan, and lessThan keyword arguments for specifying a range of valid values.
# 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
# Ans. Accepts a single string argument of what the user entered
# Raises an exception if the string fails validation
# Returns None (or has no return statement) if inputCustom() should return the string unchanged
# Returns a non-None value if inputCustom() should return a different string from the one the user entered
# Is passed as the first argument to inputCustom().
# 5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
# Ans. You can also use regular expressions to specify whether an input is allowed or not. The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input. For example, enter the following code into the interactive shell so that inputNum() will accept Roman numerals in addition to the usual numbers.
# 6. If a blank input is entered three times, what does inputStr(limit=3) do?
# Ans.By default, blank input isn’t allowed unless the blank keyword argument is set to True:
#     Use blank=True if you’d like to make input optional so that the user doesn’t need to enter anything.
# 
# 7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
# Ans.
# When you use these keyword arguments and also pass a default keyword argument, the function returns the default value instead of raising an exception. Enter the following into the interactive shell:
# 
# 
# 
