test_cases_no = int(input("int"))
test_cases = []
for i in range(test_cases_no):
    a = input("str")
    test_cases.append(a)
def solution(a):
    a1 = a.title()
    a2 = a1.split()
    if len(a2)==3 :
        print("{}.{}.{}".format(a2[0][0],a2[1][0],a2[2]))
    elif len(a2)==2 :
        print("{}.{}".format(a2[0][0],a2[1]))
    else:
        print("{}".format(a2[0]))


for t in range(test_cases_no):
    print(t)
    solution(test_cases[t])
  
if __name__=="main":
    main()            
