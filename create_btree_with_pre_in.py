class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def solution(inodr,preodr):
    if not inodr or not preodr:
        return None
    node=Node(preodr[0])
    mi=inodr.index(preodr[0])
    node.left=solution(inodr[:mi],preodr[1:mi+1])
    node.right=solution(inodr[mi+1:],preodr[mi+1:])
    return node
def printTree(node):
    if node.left:
        printTree(node.left)
    print(node.data,end=" ")
    if node.right:
        printTree(node.right)





inord=[40,20,50,10,60,30]
preord=[10,20,40,50,30,60]
km=solution(inord,preord)
printTree(km)

# inord=['D','B','E','A','F','C']
# preord=['A','B','D','E','C','F']