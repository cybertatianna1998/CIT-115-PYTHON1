def getFloatInput(message):
    while True:
        data=input(message)
        if not data .replace("." ,"").replace("-","").isdigit():
            print("input most be numbers")
        elif float(data)<=0:
            print(" input must be >0")
        else:
            return float(data)
def getMedian(array):
    if len(array)%2 == 1:
        med_index=len(array)//2
        return array[med_index]
    else:
        med_index=len(array)//2
        med_number =(array[med_index]+ array[med_index -1])/2
        return med_number
def main():
    sales=[]
    while True:
        data= getFloatInput("enter property sales value:")
        
        temp =input(" enter another value Y or N:")
        if temp =="Y":
            sales.append(data)
        elif temp == "N":
            sales.append (data)
            break
    sales.sort()   
    for i in range (len(sales) ):
       print(f"property {i+1} $  {sales[i]:,.2f}")
    print(f"minimum:   $   {sales[0]:,.2f}")
    print(f" maxium:   $   {sales[-1]:,.2f}")
    total = sum(sales)
    print(f"total:   $   {total:,.2f}")
    average = total/ len(sales)
    print(f"average:  $   {average:,.2f}")
    med= getMedian(sales)
    print(f"median:   $   {med:,.2f}")
    comission  = total*0.03
    print(f"comission:   $   {comission:,.2f}")

main()
    
    
    
