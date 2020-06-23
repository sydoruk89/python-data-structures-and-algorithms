# Merging 2 linked lists

## Authors: Roman Sydoruk

## Challenge
Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
* For this algorithm space Big O(1) and time O(n). To solve this problem I used if statements to check if any of the lists are empty. Then if lists are equal I used while loop (while next element of each lists) and swaped elements. Before that I created a new variable temp to protect elements from being lost elements from the second array. Furthermore, I used if statements in case if one of lists is shorter.

# Solutions
