class Node:
    """
    Node class initilizing
    """
    def __init__(self, value, next=None):
        """
        Init node instance with value and next element
        """
        self.value = value
        self.next = next

    def __str__(self):
        """ Return an object instance
        """
        return f'{self.value} -> {self.next}'

    def __repr__(self):
        """
        Return an object instance
        """
        return f'{self.value}'

class Queue:
    """class Queue"""

    def __init__(self):
        """Initiate class"""

        self.front = None
        self.rear = None
    

    def is_empty(self):
        """method to check if Queue is empty"""

        if self.front == None:
            return True
        return False


    def enqueue(self, val):
        """Method that adds an element to the end of the queue"""

        if self.is_empty():
            self.front = self.rear = Node(val)
        else:
            new_node = Node(val)
            self.rear.next, self.rear = new_node, new_node

    def dequeue(self):
        """Method that removes the node from the front of the queue, and returns it value."""

        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None

    def peek(self):
        """Method returns the value of the front node"""

        if not self.is_empty():
            return self.front.value
        return None

class Animal:
    """Class that creates animal imstance """
    def __init__(self, name):
        self.name = name
        self.next = None

class Cat(Animal):
    """Class that creates Cat imstance node and inherits it's properties from Animal class"""
    type = 'cat'

class Dog(Animal):
    """Class that creates Dog imstance node and inherits it's properties from Animal class"""
    type = 'dog'


class AnimalShelter:
    """Class  which holds only dogs and cats instances"""
    def __init__(self):
        """Method to initiate Animal shelter instance with creating two empty Queues"""
        self.cats = Queue()
        self.dogs = Queue()
        self.animals = Queue()
    
    def enqueue(self, animal):
        """Method to add animal to the shelter"""
        if animal.type == 'cat':
            self.cats.enqueue(animal)
            self.animals.enqueue(animal)
        elif animal.type == 'dog':
            self.dogs.enqueue(animal)
            self.animals.enqueue(animal)
        else:
            raise Exception('Must be a cat or a dog!')

    def dequeue(self, pref=None):
        """Returns either a dog or a cat. If pref is not "dog" or "cat" then return None"""
        if not pref:
            pet = self.animals.dequeue()
        elif pref.lower() == 'cat':
            pet = self.cats.dequeue()
        elif pref.lower() == 'dog':
            pet = self.dogs.dequeue()
        else:
            raise Exception('Must be a cat or a dog')
        return pet
