import pandas as pd

grades_dict = {'Wally' : [87,96,70],
               'Eva' : [100,87,90],
               'Sam' : [94,77,90],
               'Katie' : [100,81,82],
               'Bob' : [83,65,85]}

print(grades_dict)

grades = pd.DataFrame(grades_dict)


grades.index =['Test1', 'Test2', 'Test3']
print(grades)

print(grades['Eva'])

# Every column pandas series

print(grades.Sam)

print(grades.loc['Test2'])

print(grades.iloc[1])

# for consecative rows

print(grades.loc['Test1':'Test3'])

# exclude the last index
print(grades.iloc[0:2])

# for non consecative rows

print(grades.loc[['Test1','Test3']])

# exclude the last index
print(grades.iloc[[0,2]])

# View only Eva's and Katie's grades for Test1 and Test2

print(grades.loc[:'Test2', ['Eva','Katie']])

# View only Sam's TRUE Bob's grades for Test1 and Test3

print(grades.loc[['Test1','Test2'], 'Sam':'Bob'])

# Boolean Indexing

grades_A = grades[grades >= 90]

print(grades_A)

# create a dataframe of everyone with a B grade

grades_B = grades[(grades >= 80) & (grades < 90)]

print(grades_B)

# create a dataframe of everyone with an A or B grade

grades_A_or_B = grades[(grades >= 90) | (grades  >= 80)]

print(grades_A_or_B)

print(grades.describe())

# by test

print(grades.T.describe())


# Average of student grades for each test

print(grades.T.mean())


# SORTING
# sort rows by their indices (Test name)

r_sorted_grades = grades.sort_index(ascending= False)

print(r_sorted_grades)

# Sort columns by their column names (student names)
# axis =1 indicates to sort by column indices
# axis =0 indicates to sort by row indices

c_sorted_grades = grades.sort_index(axis= 1)

print(c_sorted_grades)

rc_sorted_grades = grades.sort_index(axis= 1, ascending= False)

print(rc_sorted_grades)


c_sorted_grades = grades.sort_index(axis= 1)

print(c_sorted_grades)

# sort by column values (showing grades for test 1 with student name highest to lowest)

c_sorted_grades_v = grades.sort_values(by = 'Test1', axis= 1, ascending= False)
print(c_sorted_grades_v)