
count=0.0
total=0.0
smallest=None
largest=None

while True:
    
    try:
        inp=input("Please Add Numbers to get the sum, count and average > ")
    
        if inp=="done":
            break

        inp=int(inp)    
        total=total+inp
        count=count+1

        if largest is None:
            largest=inp #Changing the none to the first value
            smallest=inp 

        if inp>largest:
            largest=inp
        
        if inp<smallest:
            smallest=inp
        

    except:
        # print("Please Just add numbers ONLY :)")
        print("Invalid input")
        continue # to go up again

#print(f"The Sum = {total} - The Count = {count} - The Average = {total/count}")
#print(f"The Largest Number is {largest}, and The Smallest number is {smallest}")
print(f"Maximum is {largest}")
print(f"Minimum is {smallest}")