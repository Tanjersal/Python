__author__ = 'Fabien'

#reading from the file

def main():

    #open file for reading

    infile = open('names.txt', 'r')

    #read the data from file

    file_contents = infile.read() # read() - puts the entire file into memory different than readline - reads per line


    print('Contents from the file read is below \n', file_contents)

    #close the buffer

    infile.close()


main()