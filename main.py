import math


def hello():
    print('Привет, мир!')

def sum_two_numbers(a, b):
    return a + b

def is_even(num):
    if num % 2 == 0:
        return True
    return False

def calculate_area(radius):
    return math.pi * (radius ** 2)

def count_vowels(string: str):
    vowels = 'уеэоаыяиюeyuioa'
    lower_string = string.lower()

    return sum(1 for char in lower_string if char in vowels)
print(count_vowels('АхахXDYes'))    # 4

def is_prime(num):
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num
print(is_prime(15), is_prime(13))

def reverse_string(string: str):
    return string[::-1]
print(reverse_string('Hello, world!'))

def calculate_factorial(num):
    if num == 1:
        return 1
    return calculate_factorial(num - 1) * num
print(calculate_factorial(5), calculate_factorial(1))

def get_average(numbers: list):
    return sum(numbers) / len(numbers)
print(get_average([1, 2, 3, 4, 5]))

def is_palindrome(string: str):
    return string == string[::-1]
print(is_palindrome('ABA'), is_palindrome('AKAL'))

def calculate_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)
print(calculate_hypotenuse(3, 4))

def remove_duplicates(elements: list):
    return list(set(elements))
print(remove_duplicates([1, 2, 2, 'ahhahha', 'g', 'g', 5, 5]))

def capitalize_words(string: str):
    return ' '.join([word.capitalize() for word in string.split(' ')])
print(capitalize_words('hello world'))

def check_anagrams(string1: str, string2: str):
    return sorted(string1) == sorted(string2)
print(check_anagrams('listen', 'silent'), check_anagrams('ggg', 'jjssss'))


###################################################################

sum_lambda = lambda a, b: a + b
print(sum_lambda(1, 3), sum_lambda(5, 6))

cap_str = lambda s: s.capitalize()
print(cap_str('hello'), cap_str('hi'))

is_even_lambda = lambda n: n % 2 == 0
print(is_even_lambda(15), is_even_lambda(4))

square_list = lambda l: [i ** 2 for i in l]
print(square_list([1, 2, 3, 4, 5]))

is_palindrome_lambda = lambda s: s[::-1] == s
print(is_palindrome_lambda('ABA'), is_palindrome_lambda('AJODAJJJ'))

sum_if_cond = lambda a, b: a + b if a + b > 10 else a * b
print(sum_if_cond(1, 11), sum_if_cond(2, 3))

first_letter_cap = lambda s: [i for i in s if i.isupper()][0]
print(first_letter_cap('ahahahGwfwodKKKWDDSdsdsd'))

lens_of_words = lambda l: [len(i) for i in l]
print(lens_of_words(['Hello', 'World','How']))