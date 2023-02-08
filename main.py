from ElectronicSign import ElectronicSign
from pixels import pixels
from Electronic_pixels import electronic_pixels

sign = ElectronicSign()

# Enter a view as a sequence of pixels and save it in memory
print("type of input either 1 or 2.")
print("1 for entering pixels and 2 for sequence :")
type_choice = input()
if type_choice=="1":
    print("Enter the pixels:")
    temp_pixels = input()
    view1 = pixels(temp_pixels)
    sign.add_view(view1)
    del view1
    sign.print_views()
    sign.clear_memory()
elif type_choice=="2":
    print("Enter the sequence any between A,B,C,1,2,3:")
    sequence = input()
    choice =0
    view1,choice = electronic_pixels(sequence,choice) 
    if choice == 0:
        sign.add_view(view1)
        del view1
        sign.print_views1()

        # Clear the memory
        sign.clear_memory()
else:
    print("PLEASE ENTER CORRECT INPUT")