# s=input("enter the string:")
# l=len(s)
# k=0
# for i in range(l):
#     k=k+((ord(s[i])-64)*26**i)
# print(k) 

# import bisect
# import math
# def minSum(num, k):
#     num.sort()
#     lastIndex = len(num)-1
#     for i in range(k):
#         if num[lastIndex]==1:
#             return sum(num)

#         num[lastIndex]= math.ceil(num[lastIndex]/2)
#         lastNumber = num[len(num)-1]
#         num.pop()
#         bisect.insort(num, lastNumber)

#     return sum(num)
# import math
# import heapq

# def minSum(num, k):
#     heap = [-n for n in num]  # negate values for max-heap
#     heapq.heapify(heap)

#     for i in range(k):
#         # Find max value
#         max_value = heapq.heappop(heap)
#         # Change max value to rounded half
#         # use floor since we've negated the values
#         heapq.heappush(heap, math.floor(max_value/2))

#     # Calculate minimum sum
#     return -sum(heap)
# import heapq
# import math
# def minSum(num, k):
#     heap = [-n for n in num]  # negate values for max-heap
#     heapq.heapify(heap)

#     for i in range(k):
#         max_value = heap[0]
#         heapq.heapreplace(heap, math.floor(max_value/2))

#     # Calculate minimum sum
#     return -sum(heap)  # reverse polarity again
# import math
# import heapq
# def heapreplace_max(heap, item):
#     "We need to implement this ourselves from primitives."
#     returnitem = heap[0]
#     heap[0] = item
#     heapq._siftup_max(heap, 0)
#     return returnitem


# def minSum(num, k):
#     heap = num   # alias for consistency with other samples
#     heapq._heapify_max(heap)  # make it a max heap (no negation hack)

#     for i in range(k):
#         max_value = heap[0]
#         heapreplace_max(heap, math.ceil(max_value/2))

#     return sum(heap)
num=[2,16]
k=3
p=minSum(num,k)
print(p)
