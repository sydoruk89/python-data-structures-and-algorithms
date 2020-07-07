class Node:
    """ Node class"""
    def __init__(self, value):
        self.value = value
        self.next = None

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


    def enqueue(self, new_node):
        """Method that adds an element to the end of the queue"""

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

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
        self.queue1 = Queue()
        self.queue2 = Queue()

    def enqueue(self, animal):
        """Method to add animal to the shelter"""
        if isinstance(animal, Cat) or isinstance(animal, Dog):
            self.queue1.enqueue(animal)
        else:
            return 'Animal must be cat or dog'

    def dequeue(self, pref):
        """Returns either a dog or a cat. If pref is not "dog" or "cat" then return None"""
        taken_animal = None

        while not self.queue1.is_empty():
            if self.queue1.front.type == pref.lower() and taken_animal == None:
                taken_animal = self.queue1.dequeue()
            else:
                self.queue2.enqueue(self.queue1.dequeue())

        while not self.queue2.is_empty():
            self.queue1.enqueue(self.queue2.dequeue())

        return taken_animal