__author__ = 'Fabien'

# demonstrate how to read a list from a file


def main():

    #open a file for read

    file = open('ListElements.txt', 'r')

    #read the contents of file into list

    cities = file.readlines() #readline vs readlines

    #close

    file.close()

    #strip the end of line

    index = 0

    while index < len(cities):

        cities[index] = cities[index].rstrip('\n')

        index+=1


    print('List read from file', cities)


main()


