# Tree

## Authors: Roman Sydoruk

## Challenge
- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
- Create a BinaryTree class
    - Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
    - Write an instance method called find-maximum-value
    - Write an instance method called find-maximum-value
    - Write a breadth first traversal method which takes a Binary Tree as its unique input.
## Approach & Efficiency
* In this challenge I used recursion;
* The Big O time complexity of a Binary Search Tree is O(h), or O(height);
* The Big O space complexity of a BST search would be O(1).
* The Big O space complexity of a BST breadth_first would be O(n) and time O(h)


## API 
* class Node
* class BinaryTree
    - pre_order method
    - in_order method
    - post_order method
    - find-maximum-value method
    - breadth_first method
* class BST(BinaryTree)
    - add method
    - contains method
    
## Solution for find max value
<img src="https://github.com/sydoruk89/python-data-structures-and-algorithms/blob/master/assets/bt_max_val.png">

## Solution for Breadth First method
<img src="https://github.com/sydoruk89/python-data-structures-and-algorithms/blob/master/assets/breadth_first.png">
