# Ćwiczenie 1/ zwracanie napisu
def check_range(x, y, z):
    if x in range(y, z):
        print("x jest między y a z")
    else:
        print("x NIE jest między y a z")
check_range(10, 7, 18)


# Ćwiczenie 1/ zwracanie booleana
def bool_range(x, y, z):
    if x in range(y, z):
        return True
    else:
        return False
bool_range(10, 7, 18)


# Ćwiczenie 2/ zwracanie unikatów - funkcja
def unique_list(my_list):
    return list(set(my_list))
unique_list([1,2,2,2,2,3,3,4,4,5,6,6,6,7,7,7,8,9])


# Ćwiczenie 2/ zwracanie unikatów - nie funkcja
my_list = [1,3,5,6,4,3,2,3,3,4,3,4,5,6,6,4,3,2,12,3,5,63,4,5,3,3,2]
list(set(my_list))


# Ćwiczenie 3/ objętość kuli
def volume_of_sphere(radius):
    return round(4/3*3.14*radius**3, 2)
volume_of_sphere(2)


# Ćwiczenie 4/ rekurencja
def num_fact(x):
    if x > 1:
        return x*num_fact(x-1)
    return 1
num_fact(10)
