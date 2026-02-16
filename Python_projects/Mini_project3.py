import random



a = '1 is for rock'
b = '0 is for paper'
c = '-1 is for scissor'

print("")
print(a)
print(b)
print(c)
print("")


comp = random.randint(-1,1)
user = int(input("Enter your choice: "))

dict={
    1 : "Rock",
    0 : "Paper",
    -1 : "Scissor"}

print("")
print("Computer choose", dict[comp])
print("Your choose", dict[user])


if(comp==user):
    print("This game is Draw!Play again")
else:
    if(comp==1 and user==0):
        print("****YOU WIN!****")
    elif(comp==1 and user==-1):
        print("----YOU LOSE!----")
    elif(comp==0 and user==1):
        print("----YOU LOSE!----")
    elif(comp==0 and user==-1):
        print("****YOU WIN!****")
    elif(comp==-1 and user==0):
        print("----YOU LOSE!----")
    elif(comp==-1 and user==1):
        print("****YOU WIN!****")
    else:
        print("Something went wrong!")