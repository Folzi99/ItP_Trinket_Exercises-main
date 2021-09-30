# Modify the program below so that you complete the function that asks the user for an integer and then shows to the user "Yay, we found [your number]" if the number is found. The list of numbers to be used should be a parameter of the function.

def search_number():
    user_num = int(input("Enter an integer: "))
    if user_num in some_numbers:
        print("Yay, we found", user_num)
    else:
        print("number not found in list")

some_numbers = [951, 402, 12, 651, 360, 69, 408, 319, 601, 435, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 855, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 45, 418, 907, 344, 236, 375, 823, 564, 597, 978, 328, 615, 753, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 228, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 829, 443, 742, 717, 958, 609, 842, 451, 688, 753, 854, 402, 685, 93, 857, 442, 380, 126, 721, 326, 753, 470, 743, 527]

search_number()