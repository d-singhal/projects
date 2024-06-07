#Count the number of occurances in the given nested list

ls = [ 1,2,2,3,[2,3,1, [2,1,[4,5,2,3]]]]
newlist = []
def find_nest(ls):
    for i in ls:
        if isinstance(i , int):
            newlist.append(i)
        if isinstance(i , list):
            find_nest(i)
    el = set(newlist)
    temp_dict = {el:newlist.count(el) for el in newlist}
    return temp_dict

print(find_nest(ls))