import game
hands = ["グー","チョキ","パー"]
count = 1
user_win = 0
computer_win = 0
draw = 0

print("じゃんけん5本勝負を始めます!")

while count < 6:
    print(f"{count}回目")
    user_hand = game.get_user_hand()
    computer_hand = game.get_computer_hand()

    print(f"あなた:{hands[user_hand]}")
    print(f"コンピューター:{hands[computer_hand]}")
   
    result = game.judge(user_hand,computer_hand)

    if result == "win":
        print("あなたの勝ちです！")
    elif result == "lose":
        print("あなたの負けです！")
    else:
        print("あいこです") 

    if result == "win":
        user_win += 1
    elif result == "lose":
        computer_win += 1 
    else:
        draw +=1

    print("------------------------------")
    print("現在の成績")
    print(f"あなた:{str(user_win)}勝") 
    print(f"コンピューター:{str(computer_win)}勝")
    print(f"あいこ:{str(draw)}回")  
    print("------------------------------")         

    count += 1

print("------------------------------")
print("最終結果")
print(f"あなた:{str(user_win)}勝") 
print(f"コンピューター:{str(computer_win)}勝")
print(f"あいこ:{str(draw)}回")  

if user_win > computer_win:
    print("おめでとう！あなたの勝ち！")
elif user_win == computer_win:
    print("どんまい！引き分け！")
else:
    print("残念！あなたの負け！！")      