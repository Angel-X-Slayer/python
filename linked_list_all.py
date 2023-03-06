

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class linkedlist:
    def __init__(self):
        self.head = None

    def travarsal(self):
        if self.head == None:
            print("the linkedlist is empty")
        else:
            n = self.head
            while n != None:
                print(n.data, end=" -> ")
                n = n.ref

    def adding_to_ll_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

    def adding_to_ll_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref != None:
                n = n.ref
            n.ref = new_node

    def searching(self, data):
        flag = 0
        n = self.head
        while n != None:
            if n.data == data:
                # print("element found")   if this is not used in adding_any_after then print the statement
                flag += 1
                break
            else:
                n = n.ref
                flag += 1
        if flag == 0:
            print("element not in the linked list")
            # return(0)  #only for adding_any_after,otherwise go with the previous print statement
        else:
            # pass
            # only for adding_any_after,otherwise go with the previous print statement
            print(f"the element is in {flag}th place")

    def adding_any_after(self, data, spot):
        new_node = Node(data)
        k = ll1.searching(data)
        if k == 0:
            print("no such element........")
        else:
            y = k.ref
            y.ref = new_node
            new_node.ref = y
        ll1.travarsal()

    def reversal(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.ref
            current.ref = prev
            prev = current
            current = next
        self.head = prev


ll1 = linkedlist()
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]
# for i in a:
#     ll1.adding_to_ll_front(i)
for i in a:
    ll1.adding_to_ll_end(i)
ll1.travarsal()
print()
ll1.reversal()
# print()
# ll1.searching(6)
# ll1.adding_any_after(8,16)
ll1.travarsal()
