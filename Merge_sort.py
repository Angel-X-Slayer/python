# # def merge_func(arr,left,mid,right):
# #     b=[]
# #     if right>1:
# #         i=left
# #         j=mid+1
# #         k=1
        
# #         while i<=mid and j<=right:
# #             if arr[i]<=arr[j]:
# #                 b[k]=arr[i]
            
# #                 i+=1
# #             elif arr[i]>arr[j]:
# #                 b[k]=arr[j]
            
# #                 j+=1
# #             k+=1
# #         if i>mid:
# #             while j<=right:
# #                 b[k]=arr[j]
# #                 k+=1
# #                 j+=1
# #         if j>right:
# #             while i<=mid:
# #                 b[k]=arr[i]
# #                 k+=1
# #                 i+=1
# #     return(b)


# # def merge_sort(arr,left,right):
# #     if left < right:
# #         mid=(left+right)//2
# #         merge_sort(arr,left,mid)
# #         merge_sort(arr,mid+1,right)
# #         merge_func(arr,left,mid,right)
# #         print(arr)


# # arr=[5,3,4,1,8,7]
# # merge_sort(arr,0,len(arr)-1)

# # Python program for implementation of MergeSort
# def mergeSort(arr):
# 	if len(arr) > 1:

# 		# Finding the mid of the array
# 		mid = len(arr)//2

# 		# Dividing the array elements
# 		L = arr[:mid]

# 		# into 2 halves
# 		R = arr[mid:]

# 		# Sorting the first half
# 		mergeSort(L)

# 		# Sorting the second half
# 		mergeSort(R)

# 		i = j = k = 0

# 		# Copy data to temp arrays L[] and R[]
# 		while i < len(L) and j < len(R):
# 			if L[i] < R[j]:
# 				arr[k] = L[i]
# 				i += 1
# 			else:
# 				arr[k] = R[j]
# 				j += 1
# 			k += 1

# 		# Checking if any element was left
# 		while i < len(L):
# 			arr[k] = L[i]
# 			i += 1
# 			k += 1

# 		while j < len(R):
# 			arr[k] = R[j]
# 			j += 1
# 			k += 1

# # Code to print the list


# def printList(arr):
# 	for i in range(len(arr)):
# 		print(arr[i], end=" ")
# 	print()


# # Driver Code
# if __name__ == '__main__':
# 	arr = [12, 11, 13, 5, 6, 7]
# 	print("Given array is", end="\n")
# 	printList(arr)
# 	mergeSort(arr)
# 	print("Sorted array is: ", end="\n")
# 	printList(arr)

# # This code is contributed by Mayank Khanna
def MS(arr):
	if len(arr)>1:
		mid=len(arr)//2
		# l=[]
		# r=[]
		l=arr[ :mid]
		r=arr[mid: ]
		MS(l)
		MS(r)
		i=j=k=0
		while i<len(l) and j<len(r):
			if l[i]<r[j]:
				arr[k]=l[i]
				i+=1
			else:
				arr[k]=r[j]
				j+=1
			k+=1
		while i<len(l):
			arr[k]=l[i]
			i+=1
			k+=1
		while j<len(r):
			arr[k]=r[j]
			k+=1
			j+=1
		return(arr)
		
# arr=[5,3,1,4,8,7]
# arr=[2,1,2,1,2,1,21,2,1]
arr=[1,3,5,4,2,34,87,12,66,22]
print(MS(arr))






















