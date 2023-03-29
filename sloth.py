print("Hello, What would you like to do!")
print("1: Calculate Best Flip")
print("2: Exit")
print("9: Debug Menu")

inp=input("Option: ")
if inp == 1:
    print("This portion is not currently functional")
    exit
if inp == 2:
    exit
if inp == 9:
    print("DEBUG MENU DO NOT TOUCH. NO OPTIONS ARE SHOWN FOR OBVIOUS REASONS.")
    debugin = input ("Enter Option, Options hidden for obvious reasons.")
    if debugin==TN_SETREFRESHRATE:
        print("**DEBUG** How often should it refresh per minute? **DEBUG**")
        refresh = input ("Refresh per minute:")
        exit
    if debugin==TN_MANUALPRICEOVERWRITE:
        print("**DEBUG** What item would you like to change, Refresh rate should be at 0 to keep it. **DEBUG**")
        exit
