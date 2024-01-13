import random as rd

while True:

    choice=['rock', 'paper', 'scissor']

    user_choice=input('User: Please enter rock, paper or scissor: ')

    computer_choice=rd.choice(choice)
    computer_choice

    if computer_choice==user_choice:
        print('its a tie, computer entered ' + computer_choice)

    elif computer_choice=='rock' and user_choice=='paper':
        print('user won, computer entered ' + computer_choice)

    elif computer_choice=='scissor' and user_choice=='paper':
        print('computer won, computer entered ' + computer_choice)

    elif computer_choice=='paper' and user_choice=='scissor':
        print('user won, computer entered ' + computer_choice)

    elif user_choice=='rock' and computer_choice=='paper':
        print('computer won, computer entered ' + computer_choice)

    elif user_choice=='rock' and computer_choice=='scissor':
        print('user won, computer entered ' + computer_choice)

    elif user_choice=='scissor' and computer_choice=='rock':
        print('computer won, computer entered ' + computer_choice)
    
    end_program=input('Do you wish to terminate yes/no: ')
    
    if end_program=='yes':
        #print('the end')
        break
    else:
        pass
    