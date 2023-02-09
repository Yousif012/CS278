def quantified_statements():

    input_string = input("Please enter 10 different integers: ")

    values = list(map(int, input_string.split()))

    output = {
        "a" : True,
        "b" : False,
        "c" : False,
        "d" : True,
        "e" : False
    }

    # statement 1
    for val in values:
        if(val < 0 and val % 2 != 0):
            output["a"] = False
            break
    
    # statement 2
    for val in values:
        if((val < 0 and val % 2 == 0) or (val >= 0)):
            output["b"] = True
    
    # statement 3
    for val in values:
        if(val < 0 and val % 2 == 0):
            output["c"] = True
    
    # statement 4
    for val in values:
        if(val % 3 == 1 and val % 5 != 0):
            output["d"] = False
    
    # statement 5
    for val in values:
        if((val % 3 == 1 and val % 5 == 0) or (val % 3 != 1)):
            output["e"] = True

    
    for keys, values in output.items():
        print(str(keys) + ") is " + str(values))


quantified_statements()