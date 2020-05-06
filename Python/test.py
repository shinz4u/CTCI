# import sys
# print(sys.path)


def function(a):
    print(a())

a = function(lambda x:"hi")

a = 10
b = 20
a = function(lambda x: a + b)



