print("The program will generate all functions from X={a,b,c} to Y={1,...,n}.")
n = int(input("Please enter the value of n: "))

functions = []

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            functions.append([i,j,k])

count = [0,0,0] # one-to-one, onto, bijection

for func in functions:
    conditions = [False, False, False] # one-to-one, onto, bijection
    
    # Check if one-to-one
    if(func[0] != func[1] and func[0] != func[2] and func[1] != func[2]):
        conditions[0] = True
        count[0] += 1

    # Check if onto
    i = 0
    nums = set()
    for num in func:
        nums.add(num)
    if(len(nums) == n):
        conditions[1] = True
        count[1] += 1
    
    # Check if bijection
    if(conditions[0] == True and conditions[1] == True):
        conditions[2] = True
        count[2] += 1

    print("f1(a)=" + str(func[0]) + "\t\tf1(b)=" + str(func[1]) + "\t\tf1(c)=" + str(func[2]))
    oneToOne = "one-to-one," if conditions[0] else "not one-to-one,"
    onto = " onto," if conditions[1] else " not onto,"
    bijection = "a bijection." if conditions[2] else "not a bijection."
    print("\tf1 is " + oneToOne + onto + " and " + bijection)

print("There are " + str(len(functions)) + " functions total.")
print(str(count[0]) + " of them are one-to-one.")
print(str(count[1]) + " of them are onto.")
print(str(count[2]) + " of them are bijections.")







