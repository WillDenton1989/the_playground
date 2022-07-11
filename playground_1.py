#the playground.

#functions

def is_multiple_of_five(n):
    if n % 5 == 0:
        return True
    return False

def is_multiple_of_three(n):
    if n % 3 == 0:
        return True
    return False

def is_multiple_of_3_and_5(n):
    if n % 3 == 0 and n % 5 == 0:
        return True
    return False

def new_count_up(n, x):
    while n <= x:
        if is_multiple_of_3_and_5(n):
            print(str(n) + " is divisible by both 3 and 5. wowzers!")
        else:
            if is_multiple_of_five(n):
                print(str(n) + " is divisible by 5! OwO")
            if is_multiple_of_three(n):
                print(str(n) + " is divisible by 3. weird")

        n = n + 1
#begin
new_count_up(1, 100)
