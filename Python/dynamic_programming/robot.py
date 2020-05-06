def robot(r, c, no_entry, path):
    if [r, c] in already_seen:
        return False
    if r < 0 or c < 0:
        return False
    if [r, c] in no_entry:
        return False

    isDestination = (r == 0 and c == 0)
    if (isDestination or robot(r-1, c, no_entry, path) or robot(r, c-1, no_entry, path)):
        path.append([r, c])
        return True
    already_seen.append([r, c])
    return False

"""

1 1 1 1 
0 1 0 1
1 0 1 1 
1 1 1 1
"""


no_entry = [[1,2],[2,1],[1,0]]
# grid = [[i, j] for i,j in range(0,11)]
r = 4
c = 4
path = []
already_seen = []
robot(r, c, no_entry, path)
print(path)

# Left top is 0,0
# Right bottom is 10,10
#
