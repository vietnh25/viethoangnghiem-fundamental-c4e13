xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
try:
    sh = float(xh)
    sr = float(xr)
except:
    print("Error, please enter numeric input")
    quit()
print(sh,sr)
if sh > 40:
    # print("Overtime")
    reg = sh * sr
    otp = (sh - 40.0) * (sr * 0.5)
    # print(reg,otp)
    xp = reg + otp
else:
    xp = sh * sr
    # print("Regular")

print('Pay: ',xp)