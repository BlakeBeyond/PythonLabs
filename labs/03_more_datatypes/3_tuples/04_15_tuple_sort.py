'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

list_t = [("one_gekko", 3), ("two_gekkos", 6), ("three_gekkos", 1)]
def takeSecond(elem):
    return elem[1]
sorted_gekkos = sorted(list_t, key=takeSecond)
print(sorted_gekkos)
