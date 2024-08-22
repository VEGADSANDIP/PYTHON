import cProfile

def sum():
    return 1+3
print(cProfile.run("sum()"))