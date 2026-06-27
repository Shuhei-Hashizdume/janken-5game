import random

def get_user_hand():
    while True:
        try:
            print("0:グー 1:チョキ 2:パー")
            user_hand = int(input("数字を入力して下さい！："))
        except ValueError:
            print("＊警告＊ 数字を入力して下さい。")
            continue
        if not 0 <= user_hand < 3:
            print("*警告* 0~2の数字を入力して下さい")
            continue
        break
    return user_hand 

def get_computer_hand():
    return random.randint(0,2)

def judge(user_hand,computer_hand):
    if user_hand == computer_hand:
        return "draw"
    elif ((user_hand == 0 and computer_hand == 1 ) or
          (user_hand == 1 and computer_hand == 2) or
          (user_hand == 2 and computer_hand == 0)):
        return "win"
    else:
        return "lose"   


