
def main():
	total = None
	with open('day1input') as f:
		read_data = f.read()
		expenses = read_data.splitlines()
	for i in range(len(expenses)):
		difference = 2020 - int(expenses[i])
		for j in range(len(expenses)):
			if i != j:
				second_diff = difference - int(expenses[j])
				match = str(second_diff)
				if expenses.count(match):
					total = second_diff * int(expenses[i]) * int(expenses[j])
					break
			
	print(total)

if __name__ == '__main__':
	main()
