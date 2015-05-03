input = [["A",1],["B",1],["C",2],["D",1],["E",3],["F",4],["G",1],["H",2],["I",1],["J",3]]
ls = {i: map(lambda y: y[0],list(filter(lambda x: x[1]==i,input))) for i in set(map(lambda r: r[1],input))}
ld = [[i, map(lambda y: y[0],list(filter(lambda x: x[1]==i,input)))] for i in set(map(lambda r: r[1],input))]
print ls
print ld
