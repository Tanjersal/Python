__author__ = 'Fabien'

# demo how to write a list to a file


def main():

    #Open a file

    file = open('ListElements.txt', 'w')

    #create a list of cities

    cities = ['Raleigh', 'Minneapolis', 'Los Angeles']


    #loop through the list and write them

    for city in cities:

        file.write(city + '\n')


    #close the file

    file.close()


    print('List has been written to file')


main()
