import game
hands = ["グー","チョキ","パー"]
count = 1

print("じゃんけん5本勝負を始めます!")

while count < 6:
    print(f"{count}回目")
    user_hand = game.get_user_hand()
    computer_hand = game.get_computer_hand()

    result = game.judge(user_hand,computer_hand)

    print(result)
    print(f"あなた:{hands[user_hand]}")
    print(f"コンピューター:{hands[computer_hand]}")
    count += 1