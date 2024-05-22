import copy

a = [2,3, [4,5]]
b = a
c = copy.copy(a)
c = [1,3,[4,5]]
d = copy.deepcopy(a)

a[0] = 6
a[-1][0] = 6

