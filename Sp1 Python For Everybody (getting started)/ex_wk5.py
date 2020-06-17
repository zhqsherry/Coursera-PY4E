hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if 0 <= h <= 40:
    pay = h * r
else:
    pay = 40*r + (h-40)*1.5*r

print(pay)


