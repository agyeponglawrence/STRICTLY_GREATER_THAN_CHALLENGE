def strictly_greater(list_):
    '''
    This function counts the number of integers strictly larger than all the integers to their right in a list.

    Parameter:
        list_ (list): A list of numbers
    
    '''

    result = []
    
    for j in range(len(list_)):
        if len(list_[j+1:]) >  0:
            if list_[j] > max(list_[j+1:]):
                result.append(list_[j])
            
    return print('The number of integers strictly larger than all the integers to their right is: {result}'.format(result = len(result)))
        

