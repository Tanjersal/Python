__author__ = 'Fabien'

# program to demonstrate the set operations


def main():

    #two sets

    computerScience = set(['Fabien', 'Arnaud', 'Philip', 'Daddy','Sylvain'])
    electricalEng = set(['Fabien', 'Philip', 'Arnaud', 'Yosh'])

    #display number of baseball set

    print('Computer Science Students: ')

    for student in computerScience:

        print(student)

    print()

    print('Electrical Engineering Students: ')

    for student in electricalEng:

        print(student)

    #intersection

    print()

    intersection = computerScience.intersection(electricalEng)

    print('Students with majors in Computer Science and Electrical Engineering: ')

    for student in intersection:

        print(student)

    print()

    # union

    union = computerScience.union(electricalEng)

    print('Students with majors in Computer Science or in Electrical Engineering:')

    for student in union:

        print(student)

    print()

    # difference
    difference = computerScience.difference(electricalEng)

    print('Students with major in Computer Science but not in Electrical Engineering:')

    for student in difference:

        print(student)

    print()


    #symmetric difference
    symetric_difference = computerScience.symmetric_difference(electricalEng)

    print('List of students that major in one major:')

    for student in symetric_difference:

        print(student)

    print()




main()
