
def sol1(data, numBits):
	gamma=''
	eplison=''
	
	for k in range(0, numBits):
		count1s = 0
		for i in range(0, len(data)):
			count1s = count1s + getKthBit(data[i],k)
		if count1s > (len(data)/2):
			gamma = '1' + gamma 
			eplison = '0' + eplison 
		else:
			gamma =  '0' + gamma
			eplison = '1' + eplison 

	print(gamma)
	print(eplison)
	return int(gamma,2) * int(eplison,2) 

def sol2(data, numBits):
	return getO2(data, numBits) * getCO2(data, numBits)

def getO2(data, numBits):
	for k in reversed(range(0, numBits)):
		c = getMostCommonKthBit(data, numBits, k)
		newdata = []
		for i in range(0, len(data)):
			if getKthBit(data[i],k) == c :
				newdata.append(data[i])
		data = newdata
		if len(data) == 1:
			return data[0]


def getCO2(data, numBits):
	for k in reversed(range(0, numBits)):
		lc = getLeastCommonKthBit(data, numBits, k)
		newdata = []
		for i in range(0, len(data)):
			if getKthBit(data[i],k) == lc :
				newdata.append(data[i])
		data = newdata
		if len(data) == 1:
			return data[0]

def getMostCommonKthBit(data, numBits, k):
	count1s = 0
	for i in range(0, len(data)):
		count1s = count1s + getKthBit(data[i],k)
	if count1s >= (len(data)/2):
		return 1
	else: 
		return 0

def getLeastCommonKthBit(data, numBits, k):
	count1s = 0
	for i in range(0, len(data)):
		count1s = count1s + getKthBit(data[i],k)
	if count1s >= (len(data)/2):
		return 0
	else: 
		return 1



def getKthBit(n, k):
    return (n & (1 << k)) >> k

if __name__ == '__main__':
    with open("./inputs/day3") as file:
        data = [ line.strip() for line in file]
        intdata = [ int(line, 2)  for line in data ]
    print(sol1(intdata, len(data[0])))
    print(sol2(intdata, len(data[0])))
