__author__ = 'Fabien'

# demonstrates insert functions


def main():

    names = ['Fabien', 'Nadia', 'Arnaud', 'Lookman']

    print('List before insertion: ', names)

    #insertion at index 0

    names.insert(1, 'Jerome')

    print('List after insertion at position 0', names)

    # sort
    names.sort()

    print('Sorted list: ', names)

    
    item = input('Which item should i remove?: ')

    try:

        names.remove(item)

        print('List after item has been removed: ', names)

    except ValueError:

        print('Value to remove is not in the list')



    # append in the list

    print('Append a name to the list')

    again = 'y'

    while again == 'y' or again == 'Y':

        nameIn = input('Please enter a name you want to append: ')

        #append

        names.append(nameIn)

        print('Do you want to add another name?: ')

        again = input('y for yes, or n for no.')

        print()


    print('New List: ')

    print(names)




main()
