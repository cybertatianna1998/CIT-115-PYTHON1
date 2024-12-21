# Grade analyzer
name=input("Name of person that we are claculating the grades for:" )


# prompt the user for person's four test scores

i_TESTSCORE1 = int(input("Test 1 : "))
i_TESTSCORE2 = int(input("Test 2 : "))
i_TESTSCORE3 = int(input("Test 3 : "))
i_TESTSCORE4 = int(input("Test 4 : "))
if i_TESTSCORE1 < 0 or i_TESTSCORE2 <0 or i_TESTSCORE3 <0 or i_TESTSCORE4 <0 :
    print(" score cannot be negative")
    exit()

# lowest grade drop

drop= input("Do you wish to drop the lowest grade Y or N ? ")
if drop == "n" or drop == "N":
   total = i_TESTSCORE1+ i_TESTSCORE2+ i_TESTSCORE3 +i_TESTSCORE4
   average = total/4
   print("average:",average)
elif drop =="y" or drop == "Y":
   if i_TESTSCORE1 <= i_TESTSCORE2 and i_TESTSCORE1 <= i_TESTSCORE3 and i_TESTSCORE1 <= i_TESTSCORE4 :
       total = i_TESTSCORE2+ i_TESTSCORE3 +i_TESTSCORE4
       average = total/3
   if i_TESTSCORE2 <= i_TESTSCORE1 and i_TESTSCORE2 <= i_TESTSCORE3 and i_TESTSCORE2 <= i_TESTSCORE4 :
       total = i_TESTSCORE1+ i_TESTSCORE3 +i_TESTSCORE4
       average = total/3

   if i_TESTSCORE3 <= i_TESTSCORE1 and i_TESTSCORE3 <= i_TESTSCORE2 and i_TESTSCORE3 <= i_TESTSCORE4 :
       total = i_TESTSCORE1+ i_TESTSCORE2 +i_TESTSCORE4
       average = total/3

   if i_TESTSCORE4 <= i_TESTSCORE1 and i_TESTSCORE4 <= i_TESTSCORE2 and i_TESTSCORE4 <= i_TESTSCORE3 :
       total = i_TESTSCORE1+ i_TESTSCORE2 +i_TESTSCORE3
       average = total/3
else:
    print("input isnt correct")
    exit()
average = round(average,1)
print("Tatianna's test average is :",average)
if average >= 97:
    print("A+")
elif average >= 94:
    print("A")
elif average >= 90:
    print("A-")
elif average >= 87:
    print("B+")
elif average >= 84:
    print("B")
elif average >= 80:
    print("B-")
elif average >= 77:
    print("C+")
elif average >= 74:
    print("c")
elif average >= 70:
    print("c-")
elif average >= 67:
    print("D+")
elif average >= 64:
    print("D")
elif average >= 60:
    print("D-")
else:
    print("F")

