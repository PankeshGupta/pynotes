u_input = input()
l_input = u_input.split(" ")
n = int(l_input[0])
m = int(l_input[1])
u_array = input()
l_array = [int(i) for i in u_array.split()]
x = -1
i = n
while x == -1 and i>=0:
    if l_array[i-1] == m:
        x = i
    else:
        i-=1
print(x)
