# 1. Write a Python program to sum all the items in a list.

L = [1, 2, 3, 4]

print sum(L)


# 2. Write a Python program to multiplies all the items in a list.


def all_mul(x):
    y = 1
    for i in x:
        y = y*i
    return y

print all_mul(L)


# 3. Write a Python program to get the largest number from a list.


def max_num_in_list( list ):  
    max = list[ 0 ]  
    for a in list:  
        if a > max:  
            max = a  
    return max  
print(max_num_in_list([1, 2, -8, 0]))


# 4. Write a Python program to get the smallest number from a list.

def smallest_num_in_list( list ):  
    min = list[ 0 ]  
    for a in list:  
        if a < min:  
            min = a  
    return min  
print(smallest_num_in_list([1, 2, -8, 0]))


        
