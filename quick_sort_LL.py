# class Node:
#     def __init__(self, data):
#         self.data=data
#         self.ref=None
# class Linked_List:
#     def __init__(self):
#         self.head=None
#     def Traversal(self):
#         if self.head==None:
#             print("the ll is empty !!!!!!")
#         else:
#             n=self.head
#             while n!=None:
#                 print(n.data,end="-->>")
#                 n=n.ref
#         print("\n")
#     def Adding_After(self,data):
#         newnode=Node(data)
#         if self.head==None:
#             self.head=newnode
#         else:
#             n=self.head
#             while n.ref!=None:
#                 n=n.ref
#             n.ref=newnode
#     def find_pivot(self,start,end):
#         if (start==end or start==None or end==None):
#             return start
#         pivot_prev=start
#         curr=start
#         pivot=end.data
#         while (start!=end):
#             if start.data<pivot:
#                 pivot_prev=curr
#                 temp=curr.data
#                 curr.data=start.data
#                 start.data=temp
#                 curr=curr.ref
#             start=start.ref
#         temp=curr.data
#         curr.data=pivot
#         end.data=temp

#         return pivot_prev
#     def QuickSort(self,start,end):
#         if (start==None or start==end):
#             return
#         pivot_prev=self.find_pivot(start,end)
#         self.QuickSort(start,pivot_prev)
#         if (pivot_prev!=None and pivot_prev==start):
#             self.QuickSort(pivot_prev.ref,end)
#         elif(pivot_prev!=None and pivot_prev.ref!=None):
#             self.QuickSort(pivot_prev.ref.ref,end)


# LL=Linked_List()
# num=int(input("enter hoe many nodes you want to insert :"))
# a=[]
# for i in range(num):
#     n=int(input("enter the number :"))
#     a.append(n)
# for i in a:
#     LL.Adding_After(i)
# dead=LL.head
# LL.Traversal()
# while dead!=None:
#     dead=dead.ref
# LL.QuickSort(LL.head,dead)
# LL.Traversal()






'''

sort a linked list using quick sort

'''

class Node:
	def __init__(self, val):
		self.data = val
		self.next = None

class Linked_List:

	def __init__(self):
		self.head=None

	def Adding_After(self,data):
		if (self.head == None):
			self.head = Node(data)
			return

		curr = self.head
		while (curr.next != None):
			curr = curr.next

		newNode = Node(data)
		curr.next = newNode

	def Traversal(self):
		while (self.head != None):
			print(self.head.data, end=" ")
			self.head = self.head.next

	''' takes first and last node,but do not
	break any links in the whole linked list'''
	def paritionLast(self,start, end):
		if (start == end or start == None or end == None):
			return start

		pivot_prev = start
		curr = start
		pivot = end.data

		'''iterate till one before the end,
		no need to iterate till the end because end is pivot'''

		while (start != end):
			if (start.data < pivot):
			
				# keep tracks of last modified item
				pivot_prev = curr
				temp = curr.data
				curr.data = start.data
				start.data = temp
				curr = curr.next
			start = start.next

		'''swap the position of curr i.e.
		next suitable index and pivot'''

		temp = curr.data
		curr.data = pivot
		end.data = temp

		''' return one previous to current because
		current is now pointing to pivot '''
		return pivot_prev

	def QuickSort(self, start, end):
		if(start == None or start == end or start == end.next):
			return

		# split list and partition recurse
		pivot_prev = self.paritionLast(start, end)
		self.sort(start, pivot_prev)

		'''
		if pivot is picked and moved to the start,
		that means start and pivot is same
		so pick from next of pivot
		'''
		if(pivot_prev != None and pivot_prev == start):
			self.sort(pivot_prev.next, end)

		# if pivot is in between of the list,start from next of pivot,
		# since we have pivot_prev, so we move two nodes
		elif (pivot_prev != None and pivot_prev.next != None):
			self.sort(pivot_prev.next.next, end)

if __name__ == "__main__":
	LL=Linked_List()
	num=int(input("enter hoe many nodes you want to insert :"))
	a=[]
	for i in range(num):
	    n=int(input("enter the number :"))
	    a.append(n)
	for i in a:
	    LL.Adding_After(i)
	dead=LL.head
	LL.Traversal()
	while dead!=None:
	    dead=dead.next
	LL.QuickSort(LL.head,dead)
	LL.Traversal()	
		# This code is contributed by humpheykibet.
