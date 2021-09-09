import time

V = int(input("Aantal vrienden: "))
T = float(7.50)
M = int(input("Aantal minuten: "))
Min = float(5)

time.sleep(1)

print("Te betalen:")
print(V+M + Min*T)

time.sleep(2)

print("Hoe wilt u betalen?")
time.sleep(2)
print("Ideal")
print("Paypal")
betaalmiddel = input("Uw betaalmethode: ")
time.sleep(1)
print("U word verzonden naar uw aanbieder.")