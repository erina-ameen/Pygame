import random
num=random.randint(1,20)
print(num)
for i in range(3):
    ans=int(input("Pick a number between 1-20"))
    if ans<num:
        print("Your guess is too low!")
    elif ans>num:
        print("Your guess is too high!")
    elif ans==num:
        print("Your guess is correct!")
        break
