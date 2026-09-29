
#Linked List Creation
class Node:
  def __init__(self,data):
      self.data=data
      self.next=None

a=Node(5)
b=Node(10)
c=Node(15)

a.next=b
b.next=c

head=a

print(head.data)
print(head.next.data)
print(head.next.next.data)


#traverse Linked List

def printLinkedlist(head):
  curr = head

  while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next
printLinkedlist(head)


#insertion at the beginning

newnode=Node(2)

newnode.next=head
head=newnode
printLinkedlist(head)


#insertion at the end

endnewnode=Node(1561)
curr=head
while curr.next!=None:
  curr=curr.next
curr.next=endnewnode
printLinkedlist(head)



#insertion at kth Index

k=2
newnode=Node(1692)
curr=head
for i in range(k-1):
  curr=curr.next

newnode.next=curr.next
curr.next=newnode
printLinkedlist(head)


#delete first node

head=head.next
printLinkedlist(head)


#delete end node

curr=head
while curr.next.next!=None:
  curr=curr.next

curr.next=None
printLinkedlist(head)


#delete kth node

k=1

curr=head
for i in range(k-1):
  curr=curr.next

curr.next=curr.next.next
printLinkedlist(head)

