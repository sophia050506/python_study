def collazt(num):
    result = True
    while(result):
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        print(num)
        result = False if num == 1 else True

try:
    num = int(input("Enter the number:"))
    collazt(num)
except ValueError:
    print("Please enter an Integer")

