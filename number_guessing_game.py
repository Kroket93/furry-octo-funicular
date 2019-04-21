
import random


game_won = False
the_number = random.randint(1, 10)
best_score = 0
tries = 0



while not game_won:

	if tries == 0:
		print("Guess the number!")

	user_number = int(input("Please enter a number between 1 and 10: "))
	tries = tries+1
	print("You entered: " + str(user_number))

	if user_number == the_number:
		print("You won! You guessed correctly in: " + str(tries) + " tries!")
		if best_score != 0:
			if tries < best_score:
				best_score = tries
		if best_score == 0:
			best_score = tries
		print("Best score this session: " + str(best_score))
		print("Do you want a rematch?")
		user_input = input("Enter Y for yes, or press any other button to exit: ")
		if str(user_input) == "y":
			tries = 0
			the_number = random.randint(1, 10)
		else:	
			game_won = True

	elif user_number < the_number:
		print("Nope! Guess higher!")

	elif user_number > the_number:
		print("Nope! Guess lower!")



