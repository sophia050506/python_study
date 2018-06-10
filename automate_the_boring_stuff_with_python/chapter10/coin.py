import random
#生成0/1的随机数
answer = random.randint(0,1)
#正面对应1,反面为0
d = {'head': 1,"tail": 0}
#允许猜测2次
print(answer)
for i in range(2):
    guess = input("Enter your answer:")
    if d[guess] == answer:
        print("you are right")
        break
    else:
        print("Please try agin")
