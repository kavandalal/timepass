#1436
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
f=[paths[paths.index(i)][0] for i in paths]
#t=[paths[paths.index(i)][1] for i in paths]
for path in paths:
    if path[1] not in f:
        print(paths[paths.index(path)][1])      
    