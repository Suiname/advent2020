
def main():
	total = None
	with open('day1input') as f:
		read_data = f.read()
		expenses = read_data.splitlines()
	for expense in expenses:
		difference = 2020 - int(expense)
		match = str(difference)
		if expenses.count(match):
			total = int(expense) * difference
			break
	print(total)

if __name__ == '__main__':
	main()
