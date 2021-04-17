import random

def play():
    user =input("what's your choice 'r' for rock ,'p' for paper , 's' for scissors  ::")
    computer = random.choice(['r','p','s'])


    if user == computer:
        return "its a tie"

    if instruction(user,computer):
        return 'you won'
    return 'you lost'



def instruction(player,opponenet):
    if(player =='r' and opponenet =='s') or (player =='s' and opponenet =='p') \
        or (player =='p' and opponenet =='r'):
        return True

print(play())