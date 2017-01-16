__author__ = 'Fabien'


# program that construct login name with slicing


def main():

    #Get the user first and last name

    first = input('Enter your first name: ')

    last = input('Enter your last name: ')

    id = input('Enter your ID number: ')

    login_first, login_last, login_Id = get_login(first, last, id)

    #concat the login

    login_name = login_first + login_last + login_Id

    #get the login

    print('Your login name is: ', login_name)



def get_login(first, last, id):

    #  Get the first three letters of the first name.
    #  If the name is less than 3 characters, the
    #  slice will return the entire first name.

    real_first = first[0:3]

    # get first 3 letters of lastname

    real_last = last[0:3]

    # get the last 3 chars of id

    real_id = id[-3:]

    return real_first, real_last, real_id


main()
