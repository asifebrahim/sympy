from sympy import IndexedBase,pycode

p=IndexedBase('p')
print(pycode(p[1]),pycode(p[2]))

