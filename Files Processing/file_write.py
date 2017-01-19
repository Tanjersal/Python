__author__ = 'Fabien'

#writing names to a file

def main():

    #open or create file to be written

    outfile = open('names.txt', 'w')


    #write the names

    outfile.write('Fabien Lavenir\n')
    outfile.write('Arnaud LeBoss\n')
    outfile.write('Mami Foutou\n')

    #close the file

    outfile.close()

    print('Insertion to file has been successful!')



main()
