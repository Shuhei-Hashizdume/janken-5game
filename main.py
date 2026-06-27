import game
hands = ["グー","チョキ","パー"]

print("じゃんけん5本勝負を始めます!")
user_hand = game.get_user_hand()
computer_hand = game.get_computer_hand()

result = game.judge(user_hand,computer_hand)
print(result)