print("Hello, What would you like to do!")
print("1: Calculate Best Flip")
print("2: Change Tax")
print("3: Exit")
print("Debug menu hidden!")

inp=input("Option: ")
if inp == 1:
    print("This portion is not currently functional")
    exit
if inp == 2: 
    print("What is your bazzar tax rate. Use percent.")
    bztax = input("Tax %: ")
if inp == 3:
    exit
if inp == 9:
    print("DEBUG MENU DO NOT TOUCH. NO OPTIONS ARE SHOWN FOR OBVIOUS REASONS.")
    debugin = input("Enter Option, Options hidden for obvious reasons, Do Not Touch! Option: ")
    
    if debugin==TN_SETREFRESHRATE:
        print("**DEBUG** How often should it refresh per minute, Do NOT set higher than 1 due to rate limiting **DEBUG**")
        refresh = input("Refresh per minute: ")
        exit
    
    if debugin==TN_MANUALPRICEOVERWRITE:
        print("**DEBUG** What item would you like to change, Refresh rate should be at 0 as to not overwrite the manual setting. **DEBUG**")
        exit
    
    if debugin==TN_APIKEYSET
        print("**DEBUG** Please enter the new API key! **DEBUG**")
        exit
