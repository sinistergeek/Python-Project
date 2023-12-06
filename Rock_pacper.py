import random
my_dict={'R':"Rock",'P':"Paper",'S':"Scissors"}
user_count = 0
comp_count = 0
games = int(input("Enter the the nume of game syou want ot play:"))

while(comp_count+user_count < games):
    flag =0
    user_input = input("\n User's Input:")[0]
    user_input = user_input.upper()

    for i in my_dict.keys():
        if(user_input==i):
            flag=1
            break
        if(flag!=1):
            print("Invalid input")
            continue
    comp_input = random.choice(list(my_dict.keys()))
    print("Computer's Input:",my_dict[comp_input])

    if(user_input=='R' and comp_input=='P') or (user_input=='P' and comp_input=='S') or (user_input=='S' and comp_input == 'R'):
        comp_count +=1
    elif(user_input=='P' and comp_input=='R') or (user_input=='S' and comp_input=='P') or (user_input=='R' and comp_input=='S'):
        user_count +=1
    else:
        print("TIE")
        print("\nSCORE:")
        print("UserScore",user_count,"\tComputer Score",comp_count,"\n")

print("\n\tFINAL SCORe:")



