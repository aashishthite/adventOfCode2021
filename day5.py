
sign = lambda a: (a>0) - (a<0)

def sol1(data):
    minimap = [ [0]*1001 for i in range(1001)]
    for segment in data:
        x1 = segment[0][0]
        x2 = segment[1][0]
        y1 = segment[0][1]
        y2 = segment[1][1]
        if x1 == x2:
            for i in range(min(y1,y2), max(y1,y2)+1):
                minimap[x1][i] +=1
        if y1 == y2:
            for i in range(min(x1,x2), max(x1,x2)+1):
                minimap[i][y1] +=1
    #print('\n'.join([''.join([str(cell) for cell in row]) for row in minimap]))
    count = 0
    for i in range(len(minimap)):
        for j in range(len(minimap[0])):
            if minimap[i][j] > 1:
                count += 1
    return count

def sol2(data):
    minimap = [ [0]*1001 for i in range(1001)]
    for segment in data:
        x1 = segment[0][0]
        x2 = segment[1][0]
        y1 = segment[0][1]
        y2 = segment[1][1]
        if x1 == x2:
            for i in range(min(y1,y2), max(y1,y2)+1):
                minimap[x1][i] +=1
        if y1 == y2:
            for i in range(min(x1,x2), max(x1,x2)+1):
                minimap[i][y1] +=1
        dx = x1 - x2
        dy = y1 - y2

        if abs(dx) == abs(dy):
            for i in range(abs(dx)+1):
                minimap[x1 - i * sign(dx)][y1 - i * sign(dy)] += 1
    #print('\n'.join([''.join([str(cell) for cell in row]) for row in minimap]))

    count = 0
    for i in range(len(minimap)):
        for j in range(len(minimap[0])):
            if minimap[i][j] > 1:
                count += 1
    return count


if __name__ == '__main__':
    with open("./inputs/day5") as file:
        #data = [line.strip() for line in file]
        data = [[[int(x) for x in pos.split(",")] for pos in line.strip().split(" -> ")] for line in file]
    print(sol1(data))
    print(sol2(data))