def type_logger(func):
    def tag_wrapper(*args):
        result = {i: type(i) for i in args}
        return result
    return tag_wrapper


@type_logger
def calc_cube(x):
   return x ** 3


a = calc_cube(5, 1.6, 'abc')
print(a)
b = calc_cube(15)
print(b)
