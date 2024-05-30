# 1.FIND 33:
# Given a list of ints, return True if the array contains a 3 
# next to a 3 somewhere.
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
    
print("Question 1")    
print( has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))



#2.BLACKJACK: Given three integers between 1 and 
# 11, if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and 
# there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'


def blackjack(a,b,c):
    if a+b+c<=21:
        print(a+b+c)
    elif a+b+c>21 and (a==11 or b==11 or c==11):
        print((a+b+c)-10)
    else:
        print("BUST")
      
print("\nQuestion 2")   
blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)


# 3.SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and 
# extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.

def summer_69(arr):
    total = 0
    skip_section = False 

    for num in arr:
        if num == 6:
            skip_section = True
        elif num == 9 and skip_section:
            skip_section = False
        elif not skip_section:
            total += num
    
    return total

print("\nQuestion 3")
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
print(summer_69([1, 3, 5]))



# 4.PAPER DOLL: Given a string, return a string where for 
# every character in the original there are three characters

def paper_doll(text):
    result = ""
    for char in text:
        result += char * 3
    return result

print("\nQuestion 4")
print(paper_doll("Hello"))
print(paper_doll("Python"))  
