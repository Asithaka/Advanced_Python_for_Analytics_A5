import numpy as np

arr01 = np.array([[1,2,3],[4,5,6]])

arr02 = np.array([0.0,0.1,0.2,0.3,0.4])

print(arr01)
print(arr02)

for row in arr01:
    #print(row)
    for col in row:
        print(col, end =' ') # we can print all digits in a same line


for i in arr01.flat: # print all values

    print(i)

arr03 = np.zeros(5)

arr04 = np.ones((2,4), dtype = int)

arr05 = np.full((3,5),13) # fill with 13

print(arr03)
print(arr04)
print(arr05)

# create a 2 dimentional arras of 5 integer elements each using the random Module
# and list compreshension print out list dimenstion, shape  and size

import random
import numpy as np

a = np.array([[random.randint(1,10) for i in range(5)],[random.randint(1,10) for i in range(5)]])

print(a)

b = np.array(np.random.randint(1,10, size =(2,5)))
print(b)

# create interger rangers using arange

arr06 = np.arange(5)

print(arr06)

arr07 = np.arange(5,10)

print(arr07)

arr08 = np.arange(10,1,-2) # upper limit exluded

print(arr08)

arr09 = np.linspace(0.0,1.0,num = 5) # lower limit and upper limint included
print(arr09)

arr10 = np.arange(1,21).reshape(4,5)
print(arr10)

arr11 = np.arange(1,100_001).reshape(100,1000)
print(arr11)

# element wise operation

arr11 = np.arange(1,6)

num02 = arr11 *2

num03 = arr11 *3

print(arr11)
print(num02)
print(num03)

arr11 +=10
print(arr11)

num04 = arr11 * num02
print(num04)

num05 =  arr11 > 6
num06 = num03 >arr11

print(num05)
print(num06)

# Numpy Calculation Methods

# Here we have an array of 4 students grades on 3 exams

# row = students
#col = exam

grades = np.array([[87,96,70], [100,87,90],[94,77,90],[100,81,82]])

print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())

# using axis =0 perform calculations on all row values withion each columns
grades_by_exam = grades.mean(axis = 0) # all row values in neach columns

print(grades_by_exam)

# using axis =1 perform calculations on all columns values withion each row

grades_by_exam = grades.mean(axis = 1) 

print(grades_by_exam)


# universal function 

num07 = np.array([1,4,9,16,25,36])
num08 = np.sqrt(num07)
print(num08)

num09 = np.array([10,20,30,40,50,60])

num10 = np.add(num07+num09)

num11 = np.multiply(num09,5)
print(num11)

num12 = num09.reshape(2,3)
num13 = np.array([2,4,6])

num14 = np.multiply(num12,num13)
print(num09)
print(num14)