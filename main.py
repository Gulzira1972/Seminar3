from linked_list import MyList, ListNode
from myclass import Tortbyrish 
lst = MyList()

nd = ListNode('class')
lst.add(nd)
nd = ListNode('name')
lst.add(nd)
nd = ListNode('My')
lst.add(nd)
lst.remove('my') #lst.remove(1)

for data in lst:
   print(data)
