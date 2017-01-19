__author__ = 'Fabien'

#writing to a file using a loop for large amount of data

def main():

    print('How many students name you want to write to file?: ')
    students = int(input('Students: '))

    #open the file to write

    outfile = open('students.txt', 'w')

    for student in range(1, students+1):

        #get the students

        student = input('Student #' + str(student) + ':')


        outfile.write(student + '\n')

    outfile.close()

    print('Finish writing to file!')


main()