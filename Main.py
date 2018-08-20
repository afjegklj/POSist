import csv
import sqlite3

db = sqlite3.connect(':memory:')
def init_db(cur):
cur (object) int= Reference_NodeID



create table node (
  Node_id int primary key, 
  TimeStamp varchar(13),
  Data varchar(),
  Mobile_Number int(),
  Phone int(),
  Value float(),
  Reference_NodeID int = null
  sort_order float
);



create table subnode(
	ChildNodeId int primary key,
	ReferenceCHildNodeId int = Reference_NodeID,

	)
// Option to create first Node
def add(self, newNode):
    node = self.firstNode
    while node.nextEl is not None:
        node = next.nextEl
    node.nextEl = newNode


// Update operations begin from here
db.node.Update(
	{Node_id:0},
	{ $set:
		{
			Node_id++
			Quantity=500 //Upper Limit
		}

	})

// Create multi set of first node according to row_number
def add_list_node(self, node):
        "add an nodeg at the end of the list"

        if not isinstance(node, ListNode):
            node = ListNode(node)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
			self.tail = node
		 return

//Add a new node to a particular set of node
def insert_Node( self, prev_node, new_data):
	if prev_nodeis None
	print "The given previous node must exist."
	return
	new_node = node(new_data)
	new_node = Node(new_data)
	new_node.next = prev_node.next
	prev_node.next = new_node
	 




insert into your_table values
(0, '', 2.0),
(1, '', 1.5),
(2, '', 0.0),
(3, '', 1.0);

-- This windowing function will "transform" the floats into sorted integers.
select id, title,
       row_number() over (order by sort_order)
from your_table