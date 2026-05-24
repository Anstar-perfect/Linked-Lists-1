class node:
    def __init__(self,data):
        self.data = data
        self.next =None
class singlyLL():
    def __init__(self):
        self.head = None
    def insert_beg(self,data):
        nb = node(data)
        nb.next = self.head
        self.head = nb
    def insert_end(self,data):
        ne = node(data)
        temp = self.head 
        while temp.next:
            temp = temp.next
        temp.next = ne
    def display(self):
        if self.head == None:
            print('List is empty')
        else:
            temp = self.head
            while temp:
                print(temp.data,'-->',end=' ')
                temp = temp.next

l =  singlyLL()
n = node(10)
l.head = n
n1 = node(20)
n.next = n1
n2 = node(30)
n1.next = n2
n3 = node(40)
n2.next = n3

l.display()
print(end='\n')

l.insert_beg(100)
l.display()
print(end='\n')
l.insert_end(100)
l.display()
print(end='\n')

