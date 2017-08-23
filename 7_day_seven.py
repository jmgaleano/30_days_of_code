# N = int(input())

# L=[str(input())]
# #L.reverse()
# for i in range(L):
# 	print (i + ' ', end=' ')
# 	l = [1,2,3,4,5]
# print (l[::-1])

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
rarr = map(str, arr[::-1])
print(" ".join(rarr))