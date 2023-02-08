def electronic_pixels(sequence,choice):
    digital_sign = {
        'A': [
            " *** ",
            "*   *",
            "*****",
            "*   *",
            "*   *",
            "*   *"
        ],
        'B': [
            "**** ",
            "*   *",
            "**** ",
            "*   *",
            "*   *",
            "**** "
        ],
        'C': [
            " *** ",
            "*    ",
            "*    ",
            "*    ",
            "*    ",
            " *** "
        ],
        '1': [
            " * ",
            "** ",
            " * ",
            " * ",
            " * ",
            "***"
        ],
        '2': [
            " *** ",
            "*   *",
            "   * ",
            "  *  ",
            " *   ",
            "*****"
        ],
        '3': [
            " *** ",
            "*   *",
            "  ** ",
            "    *",
            "*   *",
            " *** "
        ]
    }
    view1 = [[" " for _ in range(len(sequence))] for _ in range(6)]

    for i in range(6):
        for j in range(len(sequence)):
            if sequence[j] in digital_sign:
                view1[i][j] = digital_sign[sequence[j]][i]
                # print(digital_sign[sequence[j]][i], end=" ")
            else:
                print("char is not in the memory.please enter valid char A,B,C,1,2,3")
                choice =1
                break 
        if choice == 1:
            break 
    
    return view1,choice


