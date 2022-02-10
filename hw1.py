def swap_num(a,b):
    a = a + b
    b = a - b
    a = a - b


def remove_vowel(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)


def sort_list(list):
    list.sort()
    return list


def fibo():
    fib1 = fib2 = 1
    print('Insert fibo num: ')
    n = int(input())
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

