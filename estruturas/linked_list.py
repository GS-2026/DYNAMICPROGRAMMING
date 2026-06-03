from typing import cast

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None 

class LinkedList:
    def __init__(self):
        self.head: Node | None = None 
    
    def is_empty(self) -> bool:
        return self.head is None
    
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node   
    
    def insert_at_end(self, data):
        new_node = Node(data) 
        if self.is_empty():
            self.head = new_node 
            return
        
        last = cast(Node, self.head)
        while last.next:        
            last = last.next
        last.next = new_node  
    
    def search(self, target):
        current = self.head 
        while current:   
            if current.data == target:
                return current.data
            current = current.next  
        return None   

    def remove(self, target):
        current = self.head       
        previous = None         
        while current:              
            if current.data == target:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next 
                return           
            previous = current 
            current = current.next
        print(f"Valor {target} não encontrado na lista.")
    
    def display(self):
        elementos = []
        current = self.head
        while current:
            elementos.append(current.data)
            current = current.next
        print("head -> " + " -> ".join(map(str, elementos)) + " -> None")
    
    def size(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def remove_first(self):
        if not self.is_empty():
            self.head = cast(Node, self.head).next
        else:
            print("A lista está vazia.")
    
    def remove_last(self):
        if self.is_empty():
            print("A lista está vazia.")
            return
        
        if cast(Node, self.head).next is None: 
            self.head = None 
            return
        
        current = cast(Node, self.head)
        while current.next and current.next.next: 
            current = current.next 
        current.next = None 