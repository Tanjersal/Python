__author__ = 'Fabien'


import random


class Name:

    #init method always call first to initialize attributes

    def __init__(self):

        #initialize attribute

         self.nameDisplay = 'Fabien'


    #method to set the name

    def set_name(self):

        if random.randint(0, 1) == 0:

            self.nameDisplay = 'Fabien'

        else:

            self.nameDisplay = 'Arnaud'


    #method to get the name


    def get_name(self):

        return self.nameDisplay


def main():

    # create an object

    myName = Name()

    # display the current toss

    print('Whose time is it? ', myName.get_name())


    # set the name

    myName.set_name()


    print('Lets try again..whose time is it? ', myName.get_name())


main()

