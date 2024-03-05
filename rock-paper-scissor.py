import random

gameInput = ('','rock','paper', 'scissor')


cScore = 0
pScore = 0

while True:
	print("Starting game...")
	print()
	print("""Enter 1 for Rock
Enter 2 for Paper
Enter 3 for Scissor""")
	playerInput = int(input("Enter your choice: "))

	if playerInput == 1 or playerInput == 2 or playerInput == 3:
		print()
		print(f"You choice: {gameInput[playerInput]}")
		computerInput = random.randint(1,3)
		print(f"Computer choice: {gameInput[computerInput]}")
		print()
		if playerInput == computerInput:
			print("Draw")
			cScore += 1
			pScore += 1
		elif (playerInput == 3 and computerInput == 2) or (playerInput == 2 and computerInput == 1) or (playerInput == 1 and computerInput == 3):
			print("You Win!!!!")
			pScore += 1
		else:
			print("You Lose!!!!")
			cScore += 1

		print()
		print(f"Your Score: {pScore}")
		print(f"Computer Score: {cScore}")

		print()

		choice = input("Do you want to continue playin? Y/n: ").lower()

		if choice == 'n':
			break

	else:
		print("Wrong Input...")
		continue

print()
print("Final Score: ")
print(f"Your Score: {pScore}")
print(f"Computer Score: {cScore}")
print()
if cScore == pScore:
	print("Draw!!!")
elif cScore > pScore:
	print("Computer Win!!!")
else:
	print("You WIn!!!")


