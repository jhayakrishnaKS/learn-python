#1.Write a function that returns the lesser of two given numbers
# if both numbers are even, 
# but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a>b:
            print(b)
        else:
            print(a)
    else:
          if a>b:
            print(a)
          else:
            print(b)
            
print("Question 1:")        
lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)
lesser_of_two_evens(1,5)


# 2.ANIMAL CRACKERS: Write a function takes 
# a two-word string and returns True if both words begin with same letter

def animal_crackers(a):
    words=a.split()
    return words[0][0].lower()==words[1][0].lower()

print("\nQuestion 2:")        

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


#3.MAKES TWENTY: Given two integers, 
# return True if the sum of the integers is 20 or 
# if one of the integers is 20. If not, return False

def makes_twenty(a,b):
    return a==20 or b==20 or a+b==20
    
print("\nQuestion 3:")   
print(makes_twenty(20,10))
print(makes_twenty(2,3))
print(makes_twenty(12,8))