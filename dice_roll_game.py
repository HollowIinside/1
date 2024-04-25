import random
current_score = 50
current_bet = 5

print('Hi, this is dice game "Odd and Even"')
print('''To check your current score type "Score", to check current bet type "Bet"''')
print('Game starts with bet 5 and total score of 50, to win you must reach score of 100')
print('to bet on odd number type odd, to bet on even number type even')
def set_bet():
    global current_bet
    user_input_bet = int(input())
    if user_input_bet <= current_score:
        current_bet = user_input_bet
        return current_bet
    if user_input_bet > current_score:
        print(f'Try again, you set too high bet, your current score is {current_score}, you cant bet more than you have ')
    set_bet()

while True:
    dice_roll1 = random.randint(1, 6)
    dice_roll2 = random.randint(1, 6)
    total_roll_number = dice_roll1 + dice_roll2
    user_input = input()
    if current_bet > current_score:
        break
    elif user_input.lower() == 'bet':
        print (f'current bet is {current_bet}')
        continue
    elif user_input.lower() == 'score':
        print (f'current score is {current_score}')
        continue
    elif user_input.lower() == 'set bet':
        set_bet()
        continue
    elif user_input.lower() == 'odd' and total_roll_number %2==0:
        current_score = current_score - current_bet
        print(f'sorry, you lost the bet, rolled number is {total_roll_number}, you bet on odd current score is {current_score}')
        print('If you want to stop the game, type "n"')

    elif user_input.lower() == 'even' and total_roll_number %2==0:
        current_score = current_score + current_bet
        print(f'congratulations, you won the game, rolled number is {total_roll_number}, you bet on even, current score is {current_score}')
        print('If you want to stop the game, type "n"')

        
    elif user_input.lower() == 'odd' and total_roll_number %2!=0:
        current_score = current_score + current_bet
        print(f'congratulations, you won the game, rolled number is {total_roll_number}, you bet on odd, current score is {current_score}')
        print('If you want to stop the game, type "n"')
        
    elif user_input.lower() == 'even' and total_roll_number %2!=0:
        current_score = current_score - current_bet
        print(f'sorry, you lost the bet, rolled number is {total_roll_number}, you bet on even, current score is {current_score}')
        print('If you want to stop the game, type "n"')
    elif user_input.lower() == 'n':
        break
    else:
        print ('error, try again')
        continue
# if total_roll_number %2==0:
#     print('even')
# else:
#     print('odd')
