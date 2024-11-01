## Numpy Exercise
import numpy as np 

## Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")

mt1 = np.ones((4,3) , dtype = int)
mt1 = mt1 *2
print(mt1)


## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")

mt3 = np.arange(0,120,10)
mt4 = mt3.reshape(3,4)
print(mt4)

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")

mt5 = mt4.reshape(4,3)
print(mt5)


## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")

mt6 = mt5 *3

print(mt6)

## Step 5: Multiply your array from step one by your array from step 2
print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")


# mt6 = mt1 * mt4

## This errored out... why?
# Because this is an element wise multiplication, not matrix multiplication. 
# In element wise multiplication, the dimensions of the array from step 1 should exactly match the dimensions of the array from step 2

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")

mt7 = mt1 * mt5

## this worked! why?
# Both matrix have same dimention
print(mt7)



