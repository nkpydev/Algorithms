#-------------------------------------------------------------------------#
#!  Python3
#   Author          :   NK
#   Desc            :   Insertion Sort Implementation
#   Info            :   Find largest value and move it to the last position.
#-------------------------------------------------------------------------#

def sort_selection(user_input):
    l = len(user_input)
    for i in range(l-1,0,-1):
        max = 0
        for j in range(1,i+1):
            if user_input[j]>user_input[max]:
                max = j
        user_input[max],user_input[i] = user_input[i],user_input[max]
    
    return user_input



if __name__ == '__main__':
    final_sorted = []
    get_user_input = [int(x) for x in input('\nEnter numbers to be sorted [seperated by ","]:').split(',')] #int(x) is import as we are looking forward to integers and not string value
    print('\nUser Input before Sorting:\t',get_user_input)
    final_sorted = sort_selection(get_user_input)
    print('\nUser Input after Bubble Sort:\t',get_user_input)