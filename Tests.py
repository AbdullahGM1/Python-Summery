def computepay(hour,rate):

    if hour<=40:
        payment=hour*rate
        return(payment)
    
    elif hour>40:
       normal=40*rate
       extra_hour=hour-40
       over_time=extra_hour*1.5
       extra_pay=over_time*rate
       total_payment=normal+extra_pay
       return(total_payment) 
    
h=input("please add you work hours: ")
r=input("Please add your rate per hour: ")

h=float(h)
r=float(r)

print(f"Your total Payment is: ${computepay(h,r)}")
