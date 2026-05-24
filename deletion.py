class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class singlyLL():
    def __init__(self):
        self.head = None

    def delete_beg(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None
    def delete_end(self):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next:
                    temp = temp.next
                temp.next = None
    def display(self):
        if self.head == None:
            print('List is empty')
        else:
            temp = self.head
            while temp:
                print(temp.data,'-->',end=' ')
                temp = temp.next 
l =singlyLL()
n = node(10)
l.head =n 
n1 = node(20)
n.next = n1
n2 = node(30)
n1.next = n2 

l.display()
print(end='\n')

l.delete_beg()
print(end='\n')
l.display()

l.delete_end()
print(end='\n')
l.display()

