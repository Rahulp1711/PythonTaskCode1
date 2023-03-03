
def rotate_clockwise(lst):
    last_element = lst[-1]      # Here we store last elements in variable
    for i in range(len(lst) - 1, 0, -1):  #Here  we have to shift all elements to the right side by one position
        lst[i] = lst[i - 1]
    lst[0] = last_element         #Here we put last element at the beginning of the list.

#my_list = [1, 2, 3, 4, 5]        #List input   output[5, 1, 2, 3, 4]
#my_list = [6, 5, 8, 9, 7]          #List input   output[7, 6, 5, 8, 9]
my_list = [20, 15, 26, 8, 4]      #List input     output[4, 20, 15, 26, 8]

rotate_clockwise(my_list)
print(my_list)
