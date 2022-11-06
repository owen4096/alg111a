import random

def randomCombination(pA, k):
	A = pA.copy()
	chooses = []
	for _ in range(k):
		i = random.randrange(0, len(A))
		if not A[i] in chooses:
			chooses.append(A[i])
		
	chooses.sort()
	if len(chooses)==k:
		print(chooses)
	return 

A = [1,2,3,4,5]
for _ in range(30):
	randomCombination(A, 3)