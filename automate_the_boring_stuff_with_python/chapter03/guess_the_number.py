import random
def get_the_number(n):
    i = 0
    result = True
    while(result):
        if i == 0:
            num = int(input("Enter the number: "))
            i += 1
        else:
            num = int(input("Please Enter another number: "))
        if num > n:
            print("the number is too big")
        elif num < n:
            print("the number is too small")
        else:
            print("the number is ", num)
            result = False

get_the_number(random.randint(1,100))