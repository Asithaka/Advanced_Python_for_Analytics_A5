import numpy as np

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

# all rows and consecutive or sequential columns

all_students_test1_2 = grades[:,1:3]

print(all_students_test1_2)

# all rows and non-consecutive or non -sequential columns

all_students_test0_and_2 = grades[:,[0,2]]

print(all_students_test0_and_2)

# Use Numpy random-number generation to crete an array of twelve andom grades in the range 60 throught  100, then reshape
# the result into a 3-by-4 array. Calculate the average of all grades, the verages of the grades for each test and the 
# averages of the grades for each student.

grades = np.random.randint(60, 101,12).reshape(3,4)

print(grades)

print(grades.mean())

print(grades.mean(axis = 0))

print(grades.mean(axis = 1))

# shalow copy of array
# origanl change effect the view however, it doesn't work vise versa

numbers = np.arange(1,6)

print(numbers)

number_view = numbers.view()

print(number_view)

numbers[1] *= 10
print(numbers)
print(number_view)

number_view[1] /= 10
print(numbers)
print(number_view)

number_slice_viev = numbers[0:3]
print(number_slice_viev)

numbers[1] *= 20

print(number_slice_viev)

numbers_copy = numbers.copy()

print(numbers_copy)

numbers[1] *= 10
print(numbers)
print(numbers_copy)


grades = np.array([[87,96,70], [100,87,90]])

grades_reshaped = grades.reshape(1,6)

print(grades_reshaped)

grades.resize(1,6)
print(grades)


# flatten creates a deep copy
flattened = grades.flatten()

print(flattened)

# ravel create  a shallow copy
raveled = grades.ravel()

print(raveled)

# transpose

print(grades.T)


grades2 = np.array([[94,77,90],[100,81,82]])

#HSTACK adding more cols to each row

print(grades2)

h_grades = np.hstack((grades,grades2))
print(h_grades)
print(grades)

#VSTACK - adding more rows

v_grades = np.vstack((grades,grades2))
print(h_grades)
print(grades)