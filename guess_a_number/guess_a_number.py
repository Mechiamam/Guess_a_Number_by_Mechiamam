from random import randint
computer_number = randint(1, 100)
play_again = False
game_lvl = 1
print(f"Welcome to the game, you are at lvl {game_lvl}!")
while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    player_number = int(player_input)

    if player_number > computer_number:
        print("Too High!")
    elif player_number < computer_number:
        print("Too Low!")
    elif player_number == computer_number:
        print("You guess it!")
        question = input("Do you want to play again? ")
        if question == "No":
            print("Thanks for playing, see you again!")
            break
        elif question == "Yes":
            play_again = True
            game_lvl += 1
            computer_number = randint(1, 500)
            print(f"You have advanced to lvl {game_lvl}!")
            while True:
                player_input = input("Guess the number (1-500): ")
                if not player_input.isdigit():
                    print("Invalid input. Try again...")
                    continue
                player_number = int(player_input)
                if player_number > computer_number:
                    print("Too High!")
                elif player_number < computer_number:
                    print("Too Low!")
                elif player_number == computer_number:
                    print("You guess it!")
                    question = input("Do you want to play again? ")
                    if question == "No":
                        print("Thanks for playing, see you again!")
                        play_again = False
                        break
                    elif question == "Yes":
                        play_again = True
                        game_lvl += 1
                        computer_number = randint(1, 1000)
                        print(f"You have advanced to lvl {game_lvl}!")
                        while True:
                            player_input = input("Guess the number (1-1000): ")
                            if not player_input.isdigit():
                                print("Invalid input. Try again...")
                                continue
                            player_number = int(player_input)
                            if player_number > computer_number:
                                print("Too High!")
                            elif player_number < computer_number:
                                print("Too Low!")
                            elif player_number == computer_number:
                                print("You guess it!")
                                if game_lvl == 3:
                                    print("Congratulations! You have successfully beaten the game!")
                                    quit()


