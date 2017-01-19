__author__ = 'Fabien'


#dictionary to keep birthdays of friends


#constants

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():

    #empty dictionary

    birthdays = dict()

    # usr choice

    choice = 0

    while choice != QUIT:

        #get the user choice

        choice = get_menu_choice()


        #Process

        if choice == LOOK_UP:

            look_up(birthdays)

        elif choice == ADD:

            add(birthdays)

        elif choice == CHANGE:

            change(birthdays)

        elif choice == DELETE:

            delete(birthdays)


    print()


    print('Thank you for using our program!')



def get_menu_choice():

    print('Friends and their Birthdays')
    print('---------------------------')

    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit')

    print()

    #get user choice

    choice = int(input('Please make a choice: '))

    # validate the choice

    while choice < LOOK_UP or choice >QUIT:

        choice = int(input('Please make a valid choice: '))


    return choice


def look_up(dict):

    #take a name to look up

    name = input('Enter a name to look up: ')

    result = dict.get(name, 'This name was not found in the dictionary!')

    print(result)



def add(dict):

    #take a name and birthday to add

    name = input('Enter the name: ')
    birthday = input('Enter a birthday: ')


    #if the name does not exist add it - dictionary does not allow duplicates, overrides

    if name not in dict:

        #add in dictionary

        dict[name] = birthday

    else:

        print('Name already exist!')



def delete(dict):

    #get the name to delete

    name = input('Enter the name to delete: ')

    if name in dict:

        # call del to delete the name
        del dict[name]

        print('Name was deleted successfully!')

    else:

        print('Name was not found for deletion')



def change(dict):

    #get the name and birthday o change

    name = input('Enter name: ')
    birthday = input('Enter birthday: ')

    if name not in dict:

        print('Name not found for update')

    else:

        dict[name] = birthday



main()

