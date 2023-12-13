'''
Basic Loops

WHILE:

JS:
there are a few common approaches to control flow that will allow us to run the same lines of code over and 
over again. The most basic tool is the while loop, which works like this in JavaScript:

let i = 0;
while (i < 5) {
  console.log("Looping!");
  i++;
}

PY:
Python has a while construct too, which works in much the same way:

i = 0
while i < 5:
  print("Looping!")
  i += 1

FOR:

Looping with for

JS:
JavaScript has a for loop, which is commonly used to run some condition a set number of times:

for (let i = 0; i < 10; i++) {
  console.log(`Looping!`);
  console.log(`i is: ${i}`);
}

PY:
Python also has a for loop (with slightly simpler syntax!):

for i in range(10):
    print("Looping!")
    print(f"i is: {i}")

When writing a for loop in Python, the loop can proceed through any iterable object type. These include list, 
tuple, set, and dict objects, as well as str and range objects. range objects are especially useful in the for 
construct because they generate an ordered sequence of ints from 0 through a number of your choosing (like 10, above).

A for loop in Python automatically proceeds to the next element of the iterable object in its constructor; 
there is no need to specify that the loop is stopping at a certain point or increasing after each iteration.

player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

inch_heights = list()
for height in player_heights:
    inch_height = height * 7920
    inch_heights.append(inch_height)

inch_heights = list(): Here, we are initializing an empty list called inch_heights. This list will be used to store the converted heights in inches.

for height in player_heights:: This line starts a for loop that iterates over each element in the player_heights list. The variable height is used to represent each element in each iteration of the loop.

inch_height = height * 7920: Inside the loop, we have a line of code that calculates the height in inches. It takes the current height value and multiplies it by 7920 to convert it from a different unit to inches. The result is stored in the variable inch_height.

inch_heights.append(inch_height): This line appends the calculated inch_height value to the inch_heights list. It adds the converted height in inches to the list for each iteration of the loop.

So, overall, this code takes a list of player_heights, converts each height to inches using a conversion factor of 7920, and stores the converted heights in a new list called inch_heights.

update code using LIST COMPREHENSION:

inch_heights = [height * 7920 for height in player_heights]

This line of code is using a concept called list comprehension in Python. It creates a new list called inch_heights
based on the values in another list called player_heights.

Let's break it down:

height * 7920 is the expression that defines the elements of the new list. It takes each height value from player_heights and multiplies it by 7920.
for height in player_heights is the iteration part of the list comprehension. It means that for each height value in player_heights, the expression height * 7920 will be evaluated and added to the inch_heights list.
In simpler terms, this line of code is calculating the inch heights for each player in the player_heights list by multiplying their heights in another unit by 7920.