# Authors: Roman Sydoruk

## Challenge
* Node class has properties for the value stored in the Node, and a pointer to the next Node. LinkedList class includes a head property. Upon instantiation, an empty Linked List creates.
* Method <b>.append(value)</b> which adds a new node with the given value to the end of the list
* Method <b> .includes(data)</b > returns True if data is in linked list or False if it is not
* Method <b>.insertBefore(value, newVal)</b> which add a new node with the given newValue immediately before the first value node
* Method <b>.insertAfter(value, newVal)</b> which add a new node with the given newValue immediately after the first value node
* Method <b>.remove_node(value)</b> which remove node with given value.
* Method <b>.get_at_end_index(n):</b> which return a node from the end at nth index.

## Approach & Efficiency
* For first part of the  challenge I inserted a data at the beginning of the linked list. In this case time O(1) and space O(n).
* For the second part (append, includes, insert_before, insert_after, remove_node, get_at_end_index) - time O(n), Space(n). 

# Solutions
<img src="https://github.com/sydoruk89/python-data-structures-and-algorithms/blob/master/assets/linked-list.png">
