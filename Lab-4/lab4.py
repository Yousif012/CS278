def print_sequence(a, b, c, M):

    print("The first 100 elements of the sequence:")

    prev = c

    for i in range(100):
        print(prev, end = "\n" if (i+1)%10 == 0 else " ")
        prev = (a * prev + b) % M
def get_cycle_point(a, b, c, M):

    prev = c
    
    slow = fast = (a * prev + b) % M
    fast = (a * fast + b) % M

    while(slow != fast):
        slow = (a * slow + b) % M
        fast = (a * fast + b) % M
        fast = (a * fast + b) % M
        
    
    return slow
def get_length_of_cycle(a, b, c, M, cyclePoint):

    i = 0

    prev = c
    while prev != cyclePoint:
        prev = (a * prev + b) % M

    i+=1
    prev = (a * prev + b) % M

    while prev != cyclePoint:
        prev = (a * prev + b) % M
        i+=1
    
    return i
def run_program():
    input_string = input("Please enter values of a, b, c, and M in this order: ")
    values = list(map(int, input_string.split()))
    a, b, c, M = values[0], values[1], values[2], values[3]
    
    print_sequence(a, b, c, M)

    cycleLength = get_length_of_cycle(a, b, c, M, get_cycle_point(a, b, c, M))
    
    print("\n" + "Cycle length is " + str(cycleLength))


run_program()
