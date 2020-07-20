# def compound_interest(principle, rate, time):
#    CI = principle * (pow((1 + rate / 100), time))
#    print("Compound interest : ", CI)
# main
# compound_interest(10000, 7.78, 2)
# John borrow 1000$ from Kate
p = 1000 # principal

# Kate says that has an interest of 10%
r = 10 # rate

# John only pay back after 5 years
t = 5 # time
import math
ci = p * (pow((1 + r / 100), t))

print(f"John will pay back {round(ci, 2)}$")