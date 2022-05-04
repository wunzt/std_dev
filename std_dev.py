# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 5/3/2022
# Description:

class Person:
    """Represents a person with a name and age."""

    def __init__(self, name, age):
        """Creates a new Person with the specified name and age."""
        self._name = name
        self._age = age

    def get_age(self):
        """Returns the age of a Person."""
        return self._age

def std_dev(list):
    """Returns the standard deviation of a list of Persons."""
    sum = 0
    for person in list:
        sum += person.get_age()

    mean = sum/len(list)

    sigma = 0
    for person in list:
        sigma += (person.get_age() - mean) ** 2

    variance = sigma/len(list)

    deviation = variance ** 0.5

    return deviation