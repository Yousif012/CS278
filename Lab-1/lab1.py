def print_all_truth_tables():

    count = 1
    
    for row1 in "F", "T":
        for row2 in "F", "T":
            for row3 in "F", "T":
                for row4 in "F", "T":
                    for row5 in "F", "T":
                        for row6 in "F", "T":
                            for row7 in "F", "T":
                                for row8 in "F", "T":
                                    print("Truth table " + str(count) + ":" )
                                    print("---------------------")
                                    print("F " + "F " + "F " + row1)
                                    print("F " + "F " + "T " + row2)
                                    print("F " + "T " + "F " + row3)
                                    print("F " + "T " + "T " + row4)
                                    print("T " + "F " + "F " + row5)
                                    print("T " + "F " + "T " + row6)
                                    print("T " + "T " + "F " + row7)
                                    print("T " + "T " + "T " + row8)
                                    print("\n\n")
                                    count += 1

print_all_truth_tables()

    

