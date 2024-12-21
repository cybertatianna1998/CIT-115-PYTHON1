# welcome message
print("tatianna's temp converter :\n")

userTempture = int(input("Enter a tempture:"))
temptureType = input("Is the temp F for fahrenheit or C for celsius? ")
if not ((temptureType == "f") or (temptureType == "F")) and not ((temptureType == "c" or temptureType == "C")):
    print(" enter F or C")
    exit()
if temptureType == "f":
    if userTempture > 212:
        print("temp can not be > 212")
    else:
        celsius = (5.0/9)*(userTempture-32)
        round(celsius, 1)
        print ("The celcius equivalent is " + str(celsius))
elif temptureType == "c":
    if userTempture > 100:
        print("temp can not be >100")
    else:
        faherenheit = ((9.0 / 5.0) * userTempture)+ 32
        round(faherenheit, 1)
        print("The faherenheit equivalent is " + str(faherenheit))
        
        

                
