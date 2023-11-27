import random

COL = 3
ROW = 3
MATRIX = ROW * COL

VAR_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

VAR_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

MIN_BET_AMOUNT = 1
MAX_BET_AMOUNT = 100

def check_winner(bal, lines, amount, slot_mac_li):
	bet = lines * amount
	winning_line = 0
	winning_lines = []
	winning_amount = 0

	if bet > bal:
		print("### Bet amount is greater than your balance !")
	else:
		bal -= bet
		print(f"Your betting amount was ₹{bet} on {lines} lines")
		print_slot_machine(slot_mac_li)
		for sublist in slot_mac_li[0:lines]:
			if len(set(sublist)) == 1:
				winning_line = slot_mac_li.index(sublist) + 1
				winning_lines.append(winning_line)
				winning_letter = slot_mac_li[winning_line - 1][0]
				winning_amount += amount * VAR_VALUE[winning_letter]
				bal += winning_amount

		print("You won amount was ₹", winning_amount, "on", *winning_lines, "line")
	return bal

def slot_machine():
	final_list = []
	all_letters = []
	for i in VAR_COUNT.keys():
		for _ in range(0,VAR_COUNT[i]):
			all_letters.append(i)

	while len(final_list) < MATRIX:
		random_key = random.choice(all_letters)
		all_letters.remove(random_key)
		final_list.append(random_key)

	final_list = [final_list[i:i + COL] for i in range(0, len(final_list), COL)]
	return final_list

def print_slot_machine(li):
	print(" ___ " * COL)
	for i in range(len(li)):
		for j in range(len(li)):
			print("|_"+li[i][j]+"_|", end="")
		print()

def get_lines():
	while True:
		lines = input("Enter no.of lines to bet(1 - 3): ")
		if lines.isdigit():
			if int(lines) > 0 and int(lines) < ROW+1:
				break
			else:
				print("### Please enter the number within range !!!")
		else:
			print("### Please enter number !!!")
	return int(lines)

def get_bet_amount():
	while True:
		bet_amount = input("Enter amount to bet on each lines: ₹ ")
		if bet_amount.isdigit():
			if int(bet_amount) >= MIN_BET_AMOUNT and int(bet_amount) <= MAX_BET_AMOUNT:
				break
			else:
				print(f"### Please enter the bet amount within range({MIN_BET_AMOUNT} - {MAX_BET_AMOUNT}) !!!")
		else:
			print("### Please enter number !!!")
	return int(bet_amount)

def deposit():
	while True:
		amount = input("Enter your deposit amount: ₹ ")
		if amount.isdigit():
			if int(amount) > 0:
				break
			else:
				print("### Please enter number above zero !!!")
		else:
			print("### Please enter number !!!")
	return int(amount)

def execute(bal):
	nlines = get_lines()
	namount = get_bet_amount()
	slot_mac = slot_machine()
	bal = check_winner(bal, nlines, namount, slot_mac)
	return bal

def main():
	print("Welcome to Slot Machine Game:\n")
	balance = deposit()
	while True:
		print(f"~~Current balance is ₹ {balance}\n")
		start = input("Enter any key to start or [q to quit]. ").lower()
		if start == "q":
			break
		balance = execute(int(balance))		
	print(f"You finish with {balance}")
	
main()