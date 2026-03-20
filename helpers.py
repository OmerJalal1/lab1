def is_even(n):
    
    return n % 2 == 0

def factorial(n):
   
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def celsius_to_fahrenheit(c):
   
    return (c * 9 / 5) + 32

def count_vowels(s):
  
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)