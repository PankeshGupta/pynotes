l_s = input("please enter thhe list")
l = [int(i) for i in l_s.split()]
def bubble_sort(l_u):
    
    for i in range(len(l_u)-1,0,-1):
        for p in range(0,i):
            if l_u[p] > l_u[p+1]:
                l_u[p],l_u[p+1] = l_u[p+1],l_u[p]
            else:
                pass
    
bubble_sort(l)
print(l)
 
