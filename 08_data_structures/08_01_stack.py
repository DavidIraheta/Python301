# Build a custom `Stack` similar to the `Queue` you built

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
        self.min = None

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.min = value
        else:
            new_node.next = self.top
            self.top = new_node
            if value < self.min:
                self.min = value
        self.length += 1
        return self
    
    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        self.length -= 1
        return popped_node.value
    
    def empty(self):
        return self.length == 0
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.value
    

end_of_night__checklist = Stack()

end_of_night__checklist.push("Brush teeth")
end_of_night__checklist.push("Wash face")
end_of_night__checklist.push("Read")
end_of_night__checklist.push("Drink water")

print(end_of_night__checklist.peek())  
print(end_of_night__checklist.pop())  





