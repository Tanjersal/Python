__author__ = 'Fabien'


#constants

NUM_DAYS = 7

def main():

    #create a list with to hold 5 days of sales

    sales = [0] * NUM_DAYS

    #variable to the index

    index = 0

    print('Please enter your sales for the week below : ')

    while index < NUM_DAYS:

        #print info for each entry

        print('Day #', index + 1, ': ', sep='', end='')

        #store the user entry into the list

        sales[index] = float(input())


        #update the index

        index += 1

    #display the values entered

    print('Your sales for the week: ')

    for sale in sales:

        print(sale)


main()