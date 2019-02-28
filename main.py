string = "TOURWTORTWRTZUPLEBEFADIEILOSUYSNIEAEAEACFMRVTRVTXRYUQSSPKNOLIOIGNIEADHDEAEACAEGDABEIGEHN…..????."

choice = input("R for rail fence or C for columnar: ")
if choice.lower == 'r':
	rows = int(input())
	pos = 0

	for i in range(rows):
		n = i - 1
		over = False
		over_goal = 2*(rows-i-1)-1
		under_goal = 2*i-1
		print()
		# print(over_goal, end=',')
		# print(under_goal, end='')
		for char in string:
			if over:
				if n == over_goal:
					print(string[pos], end='')
					pos += 1
					n = 0
					over = False
				elif over_goal < 0:
					over = False
					print(' ', end='')
					n += 1
				else:
					print(' ', end='')
					n += 1
			else:
				if n == under_goal:
					print(string[pos], end='')
					pos += 1
					n = 0
					over = True
				elif under_goal < 0:
					over = True
					print(' ', end='')
					n += 1
				else:
					print(' ', end='')
					n += 1
elif choice.lower() == 'c':
	cols = int(input())

	output = []
	for i in range(len(string)//cols):
		output.append('')

	for i, char in enumerate(string):
		output[i%len(output)] += char

	for out in output:
		print(out)

	print('\n')

	for out in output:
		print(out, end='')
