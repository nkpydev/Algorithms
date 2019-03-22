#-------------------------------------------------------------------------#
#!  Python3
#   Author          :   NK
#   Desc            :   Basic Bubble Sort Implementation
#   Info            :   Optimized version to check if swap not required.
#-------------------------------------------------------------------------#

def sort_bubble(user_input):
    l = len(user_input)
    for i in range(l-1,0,-1):
        swapped = False
        for j in range(i):
            if user_input[j] > user_input[j+1]: 
                user_input[j],user_input[j+1] = user_input[j+1],user_input[j]
                swapped = True
        if swapped == False:
            break
    return user_input


if __name__ == '__main__':
    final_sorted = []
    get_user_input = [int(x) for x in input('\nEnter numbers to be sorted [seperated by ","]:').split(',')] #int(x) is import as we are looking forward to integers and not string value
    print('\nUser Input before Sorting:\t',get_user_input)
    final_sorted = sort_bubble(get_user_input)
    print('\nUser Input after Bubble Sort:\t',get_user_input)