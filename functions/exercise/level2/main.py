#1.OLD MACDONALD: 
# Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    if len(name)>=4:
       return name[0].upper()+name[1:3]+name[3].upper()+name[4:]
    else:
        return "name is too short"

print("Question 1")
print(old_macdonald('macdonald'))
print(old_macdonald("iroman"))


# 2.MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence


print("\nQuestion 2")
print(master_yoda('I am home'))

# 3.ALMOST THERE: Given an integer n, 
# return True if n is within 10 of either 100 or 200

def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

print("\nQuestion 3")
print(almost_there(90)) 
print(almost_there(104))