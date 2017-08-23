# N = int(input())

# for i in range(0, N):

# 	string = input()

# 	for j in range(0, len(string)):
# 		if j % 2 == 0:
# 			print(string[j], end='')
# 	print(" ", end='')

# S = str(len(input()))
# for i in S:
# 	for j in i:
# 		if j % 2 == 0:
# 			print([j], end ='')

for i in range (int(input())):
	S = input()
	print ('{} {}'.format(S[::2],S[1::2]))
	