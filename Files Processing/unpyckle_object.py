__author__ = 'Fabien'

# read from binary file again

import pickle

def main():

    #open file

    infile = open('pickle.dat', 'rb')

    #read until EOF

    EOF= False



    while not EOF:


        try:

             #unpickle object using load to load the records into person dict

            person = pickle.load(infile)

             #read until eof

            #display objects in file

            print('Here below is the list of records')

            print()

            print('Name: ', person['name'])
            print('Age: ', person['age'])
            print('Sex: ', person['sex'])

            print()

        except EOFError:


            EOF = True


    infile.close()


main()