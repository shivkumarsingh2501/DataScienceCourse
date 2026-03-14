Python Loops — Interview Ready Notes
1️⃣ What are Loops?

Loops allow a program to execute a block of code multiple times.

Instead of writing repetitive code, loops automate repetition.

Example problem:

Print numbers from 1 to 10

Without loop → 10 print statements
With loop → 1 loop

2️⃣ Types of Loops in Python

Python mainly has:

Loop Type	Purpose
For Loop	Iterate over sequence
While Loop	Run until condition becomes false

Loop control statements:

break
continue
pass
3️⃣ For Loop
Definition

A for loop is used to iterate over a sequence such as:

list

string

range

dictionary

tuple

Syntax
for variable in sequence:
    statement
4️⃣ Using range() Function

range() generates a sequence of numbers.

Syntax
range(start, stop, step)
Parameter	Meaning
start	starting number
stop	ending number (excluded)
step	increment value
Example
for i in range(5):
    print(i)

Output

0
1
2
3
4

Note: 5 is not included

5️⃣ Range with Start and Stop
for i in range(1,6):
    print(i)

Output

1
2
3
4
5
6️⃣ Range with Step
for i in range(1,10,2):
    print(i)

Output

1
3
5
7
9

Step = 2

7️⃣ Reverse Loop
for i in range(10,0,-1):
    print(i)

Output

10
9
8
7
6
5
4
3
2
1
8️⃣ Loop Through String

Strings are collections of characters.

Example:

name = "Krish"

for char in name:
    print(char)

Output

K
r
i
s
h
9️⃣ While Loop
Definition

A while loop runs until the condition becomes false.

Syntax
while condition:
    statement
Example
count = 0

while count < 5:
    print(count)
    count = count + 1

Output

0
1
2
3
4
Important Rule

Always update the variable inside the loop.

Otherwise:

Infinite loop

Example

while True:
    print("Hello")

Runs forever.

🔟 Break Statement

break stops the loop immediately.

Example
for i in range(10):

    if i == 5:
        break

    print(i)

Output

0
1
2
3
4

Loop stops when i = 5.

1️⃣1️⃣ Continue Statement

continue skips the current iteration.

Example

Print only odd numbers.

for i in range(10):

    if i % 2 == 0:
        continue

    print(i)

Output

1
3
5
7
9

Even numbers skipped.

1️⃣2️⃣ Pass Statement

pass does nothing.

Used as a placeholder.

Example
for i in range(5):

    if i == 3:
        pass

    print(i)

Output

0
1
2
3
4

pass simply ignores the condition.

1️⃣3️⃣ Nested Loops

Nested loop = loop inside another loop.

Example
for i in range(3):

    for j in range(2):

        print("i =", i, "j =", j)

Output

i = 0 j = 0
i = 0 j = 1
i = 1 j = 0
i = 1 j = 1
i = 2 j = 0
i = 2 j = 1
1️⃣4️⃣ Example — Sum of Natural Numbers
Using While Loop
n = 10
sum = 0
count = 1

while count <= n:
    sum = sum + count
    count += 1

print(sum)

Output

55
Using For Loop
sum = 0

for i in range(1,11):
    sum = sum + i

print(sum)

Output

55
1️⃣5️⃣ Example — Prime Numbers

Print prime numbers between 1–100.

for num in range(1,101):

    if num > 1:

        for i in range(2,num):

            if num % i == 0:
                break

        else:
            print(num)

Output

2 3 5 7 11 13 ...
Most Common Python Loop Interview Questions
Q1 What is a loop?

A loop executes a block of code repeatedly.

Q2 Difference between for loop and while loop?
For Loop	While Loop
Used for sequences	Used for conditions
Fixed iterations	Unknown iterations
Q3 What does break do?

Stops loop immediately.

Q4 What does continue do?

Skips current iteration.

Q5 What does pass do?

Null operation (does nothing).

Data Science Use of Loops

Loops are used in:

data cleaning
model training
feature engineering
data processing

Example:

for column in dataframe.columns:
    print(column)

Used frequently in Pandas and ML pipelines.

Quick Revision Sheet
Loop Types
for loop
while loop
Loop Control
break
continue
pass
Range
range(start, stop, step)
Important Next Topic in Your Course

The next Python topics will become extremely important for Data Science:

Strings
Lists
Tuples
Sets
Dictionaries
Functions

Especially:

Lists
Dictionaries

These are used heavily in NumPy and Pandas.