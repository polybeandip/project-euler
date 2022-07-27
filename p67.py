file = open("triangleforp67.txt","r")

triangle = file.readlines()
for (i,val) in enumerate(triangle):
    triangle[i] = val.split()

for (i,val) in enumerate(triangle):
    intline = []
    for j in val:
        intline.append(int(j))
    
    triangle[i] = intline

def bash(layers):
    newlist = []
    for (i,val) in enumerate(layers[len(layers)-2]):
        if layers[len(layers)-1][i] > layers[len(layers)-1][i+1]:
            newlist.append(val + layers[len(layers)-1][i])
        else: newlist.append(val + layers[len(layers)-1][i+1])

    layers.pop(len(layers)-1)
    layers[len(layers)-1] = newlist
    return layers

while len(triangle) > 1:
    triangle = bash(triangle)

print(triangle[0][0])

