__author__ = 'Fabien'

# using in operator for search in list

def main():

    #list of Names

    family = ['Fabien', 'Arnaud', 'Jerome', 'Nadia']

    #display list using in operator

    for name in family:

        print(name)




    #Search

    search_item = input('Enter the Name you are searching for: ')

    #using in to search in list

    if search_item in family:

        print(search_item, 'is in the list at position ', family.index(search_item))

    else:

        print(search_item, 'was not found')


main()


