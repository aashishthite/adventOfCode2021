
def sol1(data):
    result = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            result += 1
    print(result)


def sol2(data):
    result = 0
    for i in range(2, len(data)-1):
        if data[i-2] < data[i+1]:
            result += 1
    print(result) 

if __name__ == '__main__':
    with open("./inputs/day1") as file:
        data = [int(line.strip()) for line in file]
    sol1(data)
    sol2(data)