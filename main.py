# Function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. 
# The function should optionally take a second argument. When the second argument is set to True.

# Function Call:

# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
# Output:

#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----

# Function Call:

# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
# Output:

#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474

import operator

def arithmetic_formatter(list_problems):
    #covert string into list
    problems_list = list_problems.split(", ")
    
    #turn string into operator
    ops = { "+": operator.add, "-": operator.sub }

    #for the first line of the output
    for first_line in problems_list:
        question1 = first_line.split()
        
        max_space = 0
        if(len(question1[0]) > len(question1[2])):
            max_space = len(question1[0]) + 2
        else:
            max_space = len(question1[2]) + 2

        spaces = max_space - len(question1[0])

        for print_spaces in range(spaces):
            print(" ",end="")

        print(question1[0],end="")
        print("    ",end="")

    print()

    #for the second line of the output
    for second_line in problems_list:
        question2 = second_line.split()
        
        max_space = 0
        if(len(question2[0]) > len(question2[2])):
            max_space = len(question2[0]) + 2
        else:
            max_space = len(question2[2]) + 2

        spaces = max_space - len(question2[2]) - 1

        print(question2[1],end="")
        for print_spaces in range(spaces):
            print(" ",end="")

        print(question2[2],end="")
        print("    ",end="")

    print()

    #for the third line of the output
    for third_line in problems_list:
        question3 = first_line.split()
        
        max_dash = 0
        if(len(question3[0]) > len(question3[2])):
            max_dash = len(question3[0]) + 2
        else:
            max_dash = len(question3[2]) + 2

        dashes = max_dash

        for print_dash in range(dashes):
            print("_",end="")

        print("    ",end="")

    print()

    #iterate each problem & solve
    for problem in problems_list:
        question = problem.split()
        
        first_value = int(question[0])
        second_value = int(question[2])
        
        result = str(ops[question[1]](first_value,second_value))
        
        max_space = 0
        if(len(question[0]) > len(question[2])):
            max_space = len(question[0]) + 2
        else:
            max_space = len(question[2]) + 2   

        spaces = max_space - len(result)

        for print_spaces in range(spaces):
            print(" ",end="")

        print(result,end="")
        print("    ",end="")

    print()

problem_string_inp = input("Enter problems: ")
arithmetic_formatter(problem_string_inp)
