# 1.SPY GAME: Write a function that 
# takes in a list of integers and returns True if it contains 007 in order

def spy_game(arr):
    for i in range(len(arr)-2):  
        if arr[i]==0 and arr[i+1]==0 and arr[i+2]==7:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


# 3.COUNT PRIMES: Write a function that returns
# the number of prime numbers that exist up to and including a given number

def count_primes(n):
    if n < 2:
        return 0
    count = 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    
    return count


print(count_primes(10))  
print(count_primes(20)) 
print(count_primes(1))   
