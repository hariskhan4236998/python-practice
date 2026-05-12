hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h>40:
    normalhours = 40
    overtime = h-normalhours
    overtimepay=overtime*r*(1.5)
    normalhourspay= normalhours*r
    totalpay = normalhourspay + overtimepay
    print(totalpay)

else:
    pay = h*r
    print(pay)
    
