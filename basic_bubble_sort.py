#-------------------------------------------------------------------------#
#!  Python3
#   Author          :   NK
#   Desc            :   Basic Bubble Sort Implementation
#   Info            :   Not efficient enough, as both the for loops will run even if the user_input is almost sorted
#-------------------------------------------------------------------------#

def sort_bubble(user_input):
    l = len(user_input)
    for i in range(l):
        for j in range(0,l-i-1):
            if user_input[j] > user_input[j+1]: 
                user_input[j],user_input[j+1] = user_input[j+1],user_input[j]
    return user_input


if __name__ == '__main__':
    final_sorted = []
    get_user_input = [int(x) for x in input('\nEnter numbers to be sorted [seperated by ","]:').split(',')] #int(x) is import as we are looking forward to integers and not string value
    print('\nUser Input before Sorting:\t',get_user_input)
    final_sorted = sort_bubble(get_user_input)
    print('\nUser Input after Bubble Sort:\t',get_user_input)