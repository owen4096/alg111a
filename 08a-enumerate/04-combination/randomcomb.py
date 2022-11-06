import random

def randomCombination(A, k):
	chooses = []
	for _ in range(k):
		i = random.randrange(0, A[-1])
		if not A[i] in chooses:
			chooses.append(A[i])
		
	chooses.sort()
	if len(chooses)==k:
		print(chooses)
	return 

arr = [1,2,3,4,5]
for _ in range(30):
	randomCombination(arr, 3)