
def pixels(temp_pixels):
    char_pixels=['A','B','C','D','E','F']
    pixels =[]
    newint=''
    for i in range(len(temp_pixels)):
        if temp_pixels[i] in char_pixels:
            if i != 0:
                pixels.append(newint)
                newint=''
            newint += temp_pixels[i]
        else:
            newint +=temp_pixels[i]

    view1 = [[" " for _ in range(36)] for _ in range(6)]
    for pixel in pixels:
        row = ord(pixel[0]) - ord("A") 
        col = int(pixel[1:])
        view1[row][col] = "*"
    return view1
