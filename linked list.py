class Node:
 
    def __init__(self,data):
        self.data=data
        self.pointer=None
    
head= Node(1)
node2= Node(2)
node3= Node(3)

head.pointer= node2
node2.pointer= node3

cur= head

while(cur is not None):
    print(cur.data)
    cur = cur.pointer

print(head.data)
print(cur)
