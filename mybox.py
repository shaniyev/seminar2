from myboxiterator import MyBoxIterator
from myclass import my_point

class MyBox():
    def __init__(self):
        self.items = list()
        self.point = my_point()

    def __len__(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        assert item in self.items
        ind = self.items.index(item)
        return self.items.pop(ind)

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return MyBoxIterator(self.items)


# Implement a container class MyBox in the mybox.py file that stores and operates with the objects of the class developed by you in the task 8 
# of the seminar tasks 1 (in the file myclass.py). Your container class needs to implement the following methods:
# - constructor method that initializes the container with some objects (more than one);
# - len() method that outputs the number of objects in the container ;
# - add(obj) method that adds a new object in the container;
# - remove(obj) method that removes the specified object from the container;
# - contains(obj) method that checks whether the specified object is in the container;
# - iterator() method that returns an iterator over the objects in the container;