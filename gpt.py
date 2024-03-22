rows=11
columns=21
result=list()
copy=[]
iteration=[0,]

def parent_chain_name_giver(n):
    one_to_ten=["","Meth","Eth","Prop","But","Pent","Hex","Hept","Oct","Non","Dec"]
    one_to_ten_counters=["","Un","Do","Tri","Tetra","Penta","Hexa","Hepta","Octa","Nona"]
    times_ten=["","Dec","Eicos","Triacont","Tetracont","Pentacont","Hexacont","Heptacont","Octacont","Nonacont"]

    if n<10:
        root=one_to_ten[n]
    elif n<100:
        root=one_to_ten_counters[n%10]+times_ten[int(n/10)]


    else:
        root="Invalid in this tool"

    root=root.lower().capitalize()
    return root+"ane"

def chain_maker(array,main_dict,already_done,ix,iy):
    adjacent=ajdjacent_finder(array,ix,iy)
    already_done.add((ix,iy))
    adjacent.difference_update(already_done)
    listed_adjacent = list(adjacent)

    if len(listed_adjacent)==0:
        return 0

    if len(listed_adjacent)==1:

        ix=listed_adjacent[0][0]
        iy=listed_adjacent[0][1]
        result[-1].append(listed_adjacent[0])

        chain_maker(array, main_dict, already_done, ix, iy)

    else:
        copy.append([])
        iteration[0] = iteration[0] + 1
        copy[iteration[0]] = result[-1].copy()
        for x in listed_adjacent:
            result[-1].append(x)
            result.append(copy[iteration[0]])
            chain_maker(array,main_dict,already_done,x[0],x[1])

        print(copy)






def ajdjacent_finder(array,ix,iy):
    result=set()
    for ind in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]:
        if ix + ind[0] >= 0 and ix + ind[0] < rows and iy + ind[1] >= 0 and iy + ind[
            1] < columns:
            if array[ix + ind[0]][iy + ind[1]] and array[ix][iy] :
                result.add((ix+ind[0],iy+ind[1]))
    return result
def func(array):

    main_dict=dict()
    for ix in range(0,rows):
        for iy in range(0,columns):
            count=0
            for ind in [(0,1),(1,0),(0,-1),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
                if ix+ind[0]>=0 and ix + ind[0]<rows and iy+ind[1]>=0 and iy + ind[1]<columns:
                    if array[ix+ind[0]][iy+ind[1]] and array[ix][iy]:
                        count+=1
            main_dict.update({(ix,iy):count})

    chain=list()
    counter=0
    for ix in range(0,rows):
        for iy in range(0,columns):
            if array[ix][iy]:
                counter+=1
            if(main_dict[(ix,iy)]==1):
                already_done = set()
                result.clear()
                copy.clear()
                iteration[0]=0
                result.append([(ix,iy)])
                chain_maker(array, main_dict, already_done, ix, iy)
                for x in result:
                    chain.append(x)

    unique_list = []
    for sublist in chain:
        if sublist not in unique_list:
            unique_list.append(sublist)
    chain=unique_list
    max=0
    print(chain)
    for x in chain:
        if len(x)>max:
            max=len(x)
    if (counter==1):
        max=1
    for x in chain:
        if len(x)==max:
            print(x)
    return parent_chain_name_giver(max)





