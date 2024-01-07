# Loop from 97 to 122, which are the ASCII codes for lowercase letters
for i in range(97, 123):
    # Use chr() function to convert ASCII code to character
    # Use end="" parameter to avoid printing a new line
    # Use if statement to skip q and e
    if i != 101 and i != 113:
        print(chr(i), end="")

