import logicold

digit_list = logic.create_number()
input_list = []
guesses = 0

while input_list != digit_list:
    if guesses >= 5:
        print("You used up all your guesses, sorry!")
        exit()
    print(f"You have {4-guesses} guesses remaining.")
    input_list = logic.input_number()
    guesses += 1
    logic.check_number(digit_list, input_list)


print(f"Congratulations, you guessed the number correctly in {guesses} guesses!\n")
