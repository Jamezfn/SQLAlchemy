from modelY import Node
from appY import Session

session = Session()

n1 = Node(value="one")
n2 = Node(value="two")
n3 = Node(value="three")
n4 = Node(value="four")
n5 = Node(value="five")
n6 = Node(value="six")


session.add_all([n1, n2, n3, n4, n5, n6])
session.flush() 

n1.next_id = n2.id  
n2.next_id = n3.id  
n3.next_id = n4.id
n4.next_id = n5.id
n5.next_id = n6.id
n6.next_id = n1.id
session.commit()
