def segregate(arr, size):
	j = 0
	for i in range(size):
		if (arr[i]<= 0):
			arr[i], arr[j] = arr[j], arr[i]
			j += 1
	print(arr)
	print(j)
arr=[0,10,2,-10,-20]
n=len(arr)
segregate(arr,n)
