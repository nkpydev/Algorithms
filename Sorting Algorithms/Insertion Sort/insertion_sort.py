
def sort_insertion(user_input):
    l = len(user_input)
    for i in range(1,l):
        current_value = user_input[i]
        index_position = i
        while index_position > 0 and user_input[index_position-1] > current_value:
            user_input[index_position] = user_input[index_position-1]
            index_position = index_position -1
        user_input[index_position] = current_value
    
    return user_input


if __name__ == '__main__':
    final_sorted = []
    get_user_input = [int(x) for x in input('\nEnter numbers to be sorted [seperated by ","]:').split(',')] #int(x) is import as we are looking forward to integers and not string value
    print('\nUser Input before Sorting:\t',get_user_input)
    final_sorted = sort_insertion(get_user_input)
    print('\nUser Input after Bubble Sort:\t',get_user_input)