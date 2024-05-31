# 1.Write a function that computes the volume of a sphere given its radius.
import math
import string

def volume(r):
    return(4/3)*math.pi*(r**3)

print(volume(2))

# 2.Write a function that checks whether 
# a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    return num>=low and num<=high

print(ran_check(3,1,10))
        

#3. Write a Python function that accepts a string 
# and calculates the number of upper case letters and lower case letters.

def up_low(s):
    upperCount=0
    lowerCount=0
    for i in s:
       if i.isupper():
           upperCount+=1
       else:
           lowerCount+=1
    return upperCount,lowerCount

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))
        
#4. Write a Python function that takes a list 
# and returns a new list with unique elements of the first list.


def unique_list(input_list):
    return list(set(input_list))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

#5. Write a Python function to multiply all the numbers in a list.

def multiply(num):  
    for i in range(1,len(num)):
        num[i]*=num[i-1] 
    return num[len(num)-1]
        
print(multiply([1,2,3,-4]))

#6. Write a Python function that
# checks whether a word or phrase is palindrome or not.

def palindrome(s):
    s=s.replace(" ","")
    return s==s[::-1]
print(palindrome('abcba'))

#Write a Python function to 
# check whether a string is pangram or not

def is_pangram(s):
    alphabet=set(string.ascii_lowercase)
    letters=set(s.lower())
    return alphabet<=letters

print(is_pangram("The quick brown fox jumps over the lazy dog"))