def separator(x):
    """ This function returns separated characters """
    new_str = ''
    for element in x[1:]:
        new_str += ',' + element
    return x[0] + new_str


v = '12333'
x = separator(v)
print(type(x))
