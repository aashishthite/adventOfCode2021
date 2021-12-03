
def sol1(data):
	x = 0
	y = 0
	for i in range(0, len(data)):
		command = data[i].split()[0]
		val = int(data[i].split()[1])

		if command == 'forward':
			x = x + val
		if command == 'up':
			y = y - val
		if command == 'down':
			y = y + val
	return x * y

def sol2(data):
	x = 0
	y = 0
	aim = 0
	for i in range(0, len(data)):
		command = data[i].split()[0]
		val = int(data[i].split()[1])

		if command == 'forward':
			x = x + val
			y = y + aim*val
		if command == 'up':
			aim = aim - val
		if command == 'down':
			aim = aim + val
	return x * y


if __name__ == '__main__':
    with open("./inputs/day2") as file:
        data = [line.strip() for line in file]
    print(sol1(data))
    print(sol2(data))