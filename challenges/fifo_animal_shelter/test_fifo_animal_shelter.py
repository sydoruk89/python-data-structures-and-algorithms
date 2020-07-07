from fifo_animal_shelter import Node, Queue, Animal, Cat, Dog, AnimalShelter
import pytest

def test_cat():
    cat = Cat("Tangerin")
    assert cat.name == 'Tangerin'
    assert cat.type == 'cat'
    assert cat.next == None

def test_dog():
    dog = Dog("Rex")
    assert dog.name == 'Rex'
    assert dog.type == 'dog'
    assert dog.next == None

def test_shelter_enqueue():
    shelter = AnimalShelter()

    shelter.enqueue(Cat('1'))
    assert shelter.queue1.front.name == '1'
    assert shelter.queue1.rear.name == '1'
    shelter.enqueue(Dog('2'))
    assert shelter.queue1.rear.name == '2'
    shelter.enqueue(Cat('3'))
    assert shelter.queue1.rear.name == '3'
    assert shelter.queue1.front.name == '1'

def test_shelter_enqueue_not_cat_or_dog():
    shelter = AnimalShelter()
    assert shelter.enqueue(Node('1')) == "Animal must be cat or dog"

def test_shelter_dequeue():
    shelter = AnimalShelter()

    shelter.enqueue(Cat('1'))
    shelter.enqueue(Dog('2'))
    shelter.enqueue(Cat('3'))
    shelter.enqueue(Cat('4'))
    shelter.enqueue(Dog('5'))

    taken = shelter.dequeue('cat')
    assert taken.type == 'cat'
    assert taken.name == '1'

    taken = shelter.dequeue('cat')
    assert taken.type == 'cat'
    assert taken.name == '3'

    taken = shelter.dequeue('dog')
    assert shelter.queue1.front.name == '2'
    assert taken.type == 'dog'
    assert taken.name == '2'