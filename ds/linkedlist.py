class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None
        
    def make_new_list(self):
        nums = int(input("How many nodes you need to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_at_end(value)
    
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref
    
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node
    
    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return
        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def get_count(self):
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return count
    
    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False
    
    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        self.start_node = self.start_node.ref
    
    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
    
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

new_linked_list = LinkedList()
while(True):
    print('''1:Make New List\n2:Insert value at end\n3:Traverse List\n4:Insert at Start\n5:Insert after item\n6:Insert before item\n7:Insert at index\n8:Search Item in List\n9:Delete at start\n10:Delete at end\n11:Delete element by value\n12:Get total node count\n13:Exit''')
    n=int(input('Enter any option:'))
    
    if (n==1):
        new_linked_list.make_new_list()
    elif (n==2):
        new_linked_list.insert_at_end(int(input('Enter value to add at end:')))
    elif (n==3):
        new_linked_list.traverse_list()
    elif (n==4):
        new_linked_list.insert_at_start(int(input('Enter value to add at end:')))
    elif (n==5):
        new_linked_list.insert_after_item(int(input('Enter item')), int(input('Enter value')))
    elif (n==6):
        new_linked_list.insert_before_item(int(input('Enter item')), int(input('Enter value')))
    elif (n==7):
        new_linked_list.insert_at_index(int(input('Enter index')),int(input('Enter value')))
    elif (n==8):
        new_linked_list.search_item(int(input('Enter value')))
    elif (n==9):
        new_linked_list.delete_at_start()
    elif (n==10):
        new_linked_list.delete_at_end()
    elif (n==11):
        new_linked_list.delete_element_by_value()
    elif (n==12):
        c=new_linked_list.get_count()
        print('Count:',c)
    elif (n==13):
        print('Thank You')
        exit()
