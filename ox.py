theboard = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}

board_key = list(theboard.keys())

def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printboard(theboard)
        print(f"It is your turn, {turn}. Move to which place?")

        move = input()

        
        if move not in theboard:
            print("Invalid move. Please choose a valid position.")
            continue

        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1
        else:
            print("That place is already filled. Try again.")
            continue

        
        if count >= 5:
            if (theboard['7'] == theboard['8'] == theboard['9'] != ' ') or \
               (theboard['4'] == theboard['5'] == theboard['6'] != ' ') or \
               (theboard['1'] == theboard['2'] == theboard['3'] != ' ') or \
               (theboard['7'] == theboard['4'] == theboard['1'] != ' ') or \
               (theboard['8'] == theboard['5'] == theboard['2'] != ' ') or \
               (theboard['9'] == theboard['6'] == theboard['3'] != ' ') or \
               (theboard['7'] == theboard['5'] == theboard['3'] != ' ') or \
               (theboard['9'] == theboard['5'] == theboard['1'] != ' '):
                printboard(theboard)
                print("\nGame Over")
                print(f"**** {turn} won! ****")
                break

        
        if count == 9:
            print("\nGame Over")
            print("It's a Tie!")
            break

        
        turn = 'O' if turn == 'X' else 'X'

    
    restart = input("Do you want to play again? (y/n): ").lower()
    if restart == 'y':
        for key in board_key:
            theboard[key] = ' '
        game()

if __name__ == "__main__":
    game()
