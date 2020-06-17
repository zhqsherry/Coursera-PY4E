def computepay(h,r):
    if h > 40:
        p = 40 * r + (h - 40) * 1.5 * r
    else:
        p = h * r
    return p


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
p = computepay(h, r)
print("Pay", p)