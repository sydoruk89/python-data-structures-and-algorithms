# Stacks and Queues

## Authors: Roman Sydoruk

## Challenge
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
Should raise exception when called on empty stack
Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
Should raise exception when called on empty stack
Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
Should raise exception when called on empty queue
Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
Should raise exception when called on empty queue
Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.

## Approach & Efficiency
### Stack:
* pop() - space and time O(1);
* push(val) - space and time O(1);
* peek() - space and time O(1);
* is_empty() - space and time O(1);

### Queue:
* enqueue(value) - space and time O(1);
* dequeue() - space and time O(1);
* peek - space and time O(1);
* is_empty() - space and time O(1);

## API
* Node class that has properties for the value stored in the Node, and a pointer to the next node
* Stack class that has a top property. It creates an empty Stack when instantiated
- push - method which takes any value as an argument and adds a new node with that value to the top;
- pop - method that does not take any argument, removes the node from the top of the stack, and returns the node’s value;
- peek - method that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack;
- isEmpty - method that takes no argument, and returns a boolean indicating whether or not the stack is empty;

* Queue class that has a front property. It creates an empty Queue when instantiated;
- enqueue - method which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance;
- dequeue method -  that does not take any argument, removes the node from the front of the queue, and returns the node’s value;
- peek method that does not take an argument and returns the value of the node;
- isEmpty - method that takes no argument, and returns a boolean indicating whether or not the queue is empty.

### [Link to code]()