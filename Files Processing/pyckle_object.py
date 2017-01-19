__author__ = 'Fabien'

# serialize data in a bin file using pickle.dump

import pickle


def main():

    #open file for output

    outfile = open('pickle.dat', 'wb')

    again = 'y'


    while again.lower() == 'y':

        #get data and save it

        getAndSave(outfile)


        #ask user again

        again = input('Do you want to enter more data? Type y to continue: ')


    print('Thank you!')

    outfile.close()




def getAndSave(file):

    #create a dictionary

    person = dict()

    # get data about a person and store it
    print("Please enter below the person's details to be recorded")

    print()

    person['name'] = input('Enter Name: ')
    person['age'] = int(input('Enter age: '))
    person['sex'] = input('Enter sex: ')


    #write the person dict to the binary file

    pickle.dump(person, file)

    print('File was saved successfully!')


main()



