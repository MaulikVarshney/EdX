budget=input("Type yout budget")
budget=float(budget)
if (budget<450000):
    print(f"Sorry...!!! No car is available in your {budget}")
elif(budget<=450000)&(budget>=650000):
    print(f"CarA is possible in {budget}")
elif(budget>=650000)&(budget<=1250000):
    print(f"CarB is present in {budget}")
elif(budget>=1250000)&(budget<=1650000):
    print(f"CarC is possible in {budget}")
elif(budget>=1650000)&(budget<=2250000):
    print(f"CarD is possible in {budget}")
else :
    print(f"CarE is possible in {budget}")
print("Hope you like the car")

                                
