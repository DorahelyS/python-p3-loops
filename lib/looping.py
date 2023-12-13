#!/usr/bin/env python3

'''
Write a function happy_new_year() using a while loop that outputs numbers starting at 10 and counting down to 1. 
After reaching 1, print out "Happy New Year!"

'''
def happy_new_year():
   i = 10 
   #while i <= 10:
   while  i > 0:
    print(i)
    i -= 1
    print("Happy New Year!")
#Printing i inside the while loop allows you to see the countdown from 10 to 1 as the loop iterates. 
#It gives you a visual representation the countdown process.

'''
The condition i <= 10 is used in the while loop, which means the loop will continue as long as i is less than or equal to 10. This version will also count down from 10 to 1 and print "Happy New Year!", but the loop will continue for an additional iteration where i becomes 0. However, since the print statement is outside the loop, "Happy New Year!" will only be printed once.

In practice, both versions will produce the same result of counting down from 10 to 1 and printing "Happy New Year!" at the end. However, the first version is more efficient because it stops the loop when i becomes 0, while the second version allows one extra iteration.

Let me know if you have any further questions or concerns!

'''
'''
i is greater than 1 and less than or equal to 10.
but since I have i set to 10 i will always be greater than one so don't need first statement

def happy_new_year():
    i = 10
    while i <= 10:
        i -= 1
        print("Happy New Year!")
'''
#Write a function square_integers() that takes one argument, a list of integers and returns the list of squared
#elements.
def square_integers(int_list):
    return [num ** 2 for num in int_list]
#return [i ** 2 for i in int_list]

'''
The new list is created using a list comprehension.

Here's how it works:

The expression [i ** 2 for i in int_list] is enclosed in square brackets [], which indicates that it will create a new list.
The for i in int_list part specifies that the list comprehension will iterate over each element i in the int_list.
The expression i ** 2 is the value that will be added to the new list for each iteration. It calculates the square of each element i.
The resulting squared numbers are added to the new list.
Finally, the return statement is used to return the new list containing the squared numbers.
So, when the square_integers function is called with a list of integers, the list comprehension will iterate over each number, calculate its square, and add it to a new list. This new list is then returned by the function.

The list comprehension is a concise way to create a new list based on an existing list or any iterable. It allows you to perform operations on each element of the iterable and generate a new list in a single line of

'''
'''
# how do I make this def work??
def square_integers(int_list):
    for num in int_list:
        return num ** 2



SOLUTION:

def square_integers(int_list):
    squared_list = []
    for num in int_list:
        squared_list.append(num ** 2)
    return squared_list

In this updated code, we initialize an empty list called squared_list. Then, we iterate over each number num in the
int_list using a for loop. Inside the loop, we calculate the square of each number num using the ** operator and 
append it to the squared_list using the append() method. Finally, we return the squared_list containing all the 
squared numbers.

By using a for loop and appending the squared numbers to a list, you can achieve the same functionality as the 
second code snippet and generate a list of squared numbers from the input list without using a list comprehension.

'''

#Write a function fizzbuzz() that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead 
#of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five,
#print "FizzBuzz".
def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)

'''
The range in the for loop uses the range function with arguments (1, 101), which means it will iterate from 1 to 100
(inclusive). The number 101 is used as the upper limit because the range function stops at the number before the 
upper limit. Therefore, using 101 ensures that the loop will iterate up to and include the number 100.

Yes, you can certainly use range(101) instead of range(1, 101) in the for loop. They both achieve the same result
of iterating from 1 to 100 (inclusive).

The reason for using range(1, 101) in the original code is to explicitly specify the starting point of the 
iteration as 1. By default, if you only provide one argument to the range() function, it assumes the starting point
is 0.

So, both range(1, 101) and range(101) will work in this case. It's a matter of personal preference and code 
readability.

Yes, the statement for i in range(1, 101) can be thought of as a loop that iterates over the numbers from 1 to 100, inclusive. It is equivalent to the following pseudo-code:

let i = 1
while i <= 100:
  # Loop body
  # ...
  i = i + 1
In each iteration, the value of i is incremented by 1 until it reaches 101, which is why the loop will iterate 
100 times.


USING LIST COMPREHENSION:
def fizzbuzz():
    result = ["FizzBuzz" if i % 15 == 0 else "Buzz" if i % 5 == 0 else "Fizz" if i % 3 == 0 else i for i in range(1, 101)]
    for item in result:
        print(item)
'''