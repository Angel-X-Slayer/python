class Node:
    def __init__(self,value):
        self.data=value
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def Traversal(self):
        if self.head==None:
            print("the ll is empty !!!!!!")
        else:
            n=self.head
            while n!=None:
                print(n.data,end="-->>")
                n=n.ref
        print("\n")
    def Adding_After(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            n=self.head
            while n.ref!=None:
                n=n.ref
            n.ref=newnode
    def Intersection(LL1,LL2):#this code will work fine for ll1=1 2 3 4 5 6 7
                              #                             ll2=8 10 9 5 12 14
                              #this code will work fine for ll1=1 2 3 4 5
                              #                             ll2=6 7 8 9 0
                              #this code will not work for ll1=1 2 3 4 5
                              #                            ll2=5 6 7 8 9
        ##keep that in mind and change the code after watching GfG##
        head1=LL1.head
        dead1=LL1.head
        head2=LL2.head
        dead2=LL2.head
        # print(head1.data)
        # print(head1.ref)
        count1=0
        count2=0
        while head1!=None:
            head1=head1.ref
            count1+=1
        while head2!=None:
            head2=head2.ref
            count2+=1
        if count1!=count2:
            if count1>count2:
                diff1=count1-count2
                while diff1!=0:
                    dead1=dead1.ref
                    diff1-=1
            elif count2>count1:
                diff2=count2-count1
                while diff2!=0:
                    dead2=dead2.ref
                    diff2-=1
        else:
            pass
        # print(count1, count2, dead1.data, dead2.data)
        while dead1.data!=dead2.data:
            dead1=dead1.ref
            dead2=dead2.ref
            if dead1==None or dead2==None:
                print("no match found")
                break
        if dead1==None or dead2==None:
            pass
        else:
            print(dead1.data)
    def Reversal(self):
        prev=None
        cur=self.head
        nxt=self.head.ref
        while cur!=None:
            nxt=cur.ref
            cur.ref=prev
            prev=cur
            cur=nxt
        self.head=prev
LL1=LinkedList()
LL2=LinkedList()
x1=int(input("enter the number of values want to insert in the LL :"))
x2=int(input("enter the number of values want to insert in the LL :"))
arr1=[]
arr2=[]
for i in range(x1):
    val=int(input("entr the number :"))
    arr1.append(val)
for i in arr1:
    LL1.Adding_After(i)
for j in range(x2):
    val=int(input("entr the number :"))
    arr2.append(val)
for j in arr2:
    LL2.Adding_After(j)
# LL1.Traversal()
# LL2.Traversal()
# LL1.Reversal()
# LL1.Traversal()
LL1.Intersection(LL2)




