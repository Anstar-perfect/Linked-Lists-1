class node():
    def __init__(self,data):
        self.data =data
        self.next = None

class singlyLL():
    def __init__(self):
        self.head = None

    def search(self,key):
        if self.head != None:
            temp = self.head
            while temp:
                if temp.data == key:
                    return True
                temp = temp.next
            return False   
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

print(l.search(20))
