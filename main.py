import random
n= random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    guesses+=1
    a =int(input("enter your number :"))
    if(a>n):
        print(F"enter lower no  ")
    elif(a==n):
        print("the number is correct")
    else:
        print("enter higher no ")
print(f"you have guessed the number {n} correctly in {guesses } attempt")
