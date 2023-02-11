class Node:
    def __init__(self,sym,freq,left=None,right=None):
        self.left=left
        self.right=right
        self.sym=sym
        self.freq=freq
        self.huff=""
def printnodes(Nodek,val=""):
    newVal = val + str(Nodek.huff)
    if(Nodek.left):
        printnodes(Nodek.left, newVal)
    if(Nodek.right):
        printnodes(Nodek.right, newVal)
    if(not Nodek.left and not Nodek.right):
        print(f"{Nodek.sym} -> {newVal}")


# sym=list(map(int,input("enter symbols :").split(','))


sym=[]
freq=[]
nodes=[]
n=int(input("enter how many symbol u want to insert :"))
for i in range(n):
    k=input("enter the symbol :")
    sym.append(k)
for i in range(n):
    f=int(input(f"enter the freq of {sym[i]} :"))
    freq.append(f)




# sym= ['a', 'b', 'c', 'd', 'e', 'f']
# frequency of characters
# freq = [ 5, 9, 12, 13, 16, 45]
# print(sym)



zipped_p=zip(freq,sym)
z=[x for _, x in sorted(zipped_p)]

# print(z)

freq.sort()

# print(freq)

for i in range(len(sym)):
    nodes.append(Node(z[i],freq[i]))



# for i in range(len(nodes)):
#     print(nodes[i].sym)
#     print(nodes[i].freq)
#     print(nodes[i].huff)




while len(nodes)!=1:
    nodes = sorted(nodes, key=lambda x: x.freq)
    left=nodes[0]
    right=nodes[1]
    left.huff=0
    right.huff=1

    
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(Node(left.sym+right.sym, left.freq+right.freq,left,right))
printnodes(nodes[0])
 
# print(nodes)





#***************************************************************************************************************#






# A Huffman Tree Node
# class node:
# 	def __init__(self, freq, symbol, left=None, right=None):
# 		# frequency of symbol
# 		self.freq = freq

# 		# symbol name (character)
# 		self.symbol = symbol

# 		# node left of current node
# 		self.left = left

# 		# node right of current node
# 		self.right = right

# 		# tree direction (0/1)
# 		self.huff = ''

# # utility function to print huffman
# # codes for all symbols in the newly
# # created Huffman tree


# def printNodes(node, val=''):
# 	# huffman code for current node
# 	newVal = val + str(node.huff)

# 	# if node is not an edge node
# 	# then traverse inside it
# 	if(node.left):
# 		printNodes(node.left, newVal)
# 	if(node.right):
# 		printNodes(node.right, newVal)

# 		# if node is edge node then
# 		# display its huffman code
# 	if(not node.left and not node.right):
# 		print(f"{node.symbol} -> {newVal}")


# # characters for huffman tree
# chars = ['a', 'b', 'c', 'd', 'e', 'f']

# # frequency of characters
# freq = [ 5, 9, 12, 13, 16, 45]

# # list containing unused nodes
# nodes = []

# # converting characters and frequencies
# # into huffman tree nodes
# for x in range(len(chars)):
# 	nodes.append(node(freq[x], chars[x]))

# while len(nodes) > 1:
# 	# sort all the nodes in ascending order
# 	# based on theri frequency
# 	nodes = sorted(nodes, key=lambda x: x.freq)

# 	# pick 2 smallest nodes
# 	left = nodes[0]
# 	right = nodes[1]

# 	# assign directional value to these nodes
# 	left.huff = 0
# 	right.huff = 1

# 	# combine the 2 smallest nodes to create
# 	# new node as their parent
# 	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

# 	# remove the 2 nodes and add their
# 	# parent as new node among others
# 	nodes.remove(left)
# 	nodes.remove(right)
# 	nodes.append(newNode)

# # Huffman Tree is ready!
# printNodes(nodes[0])

