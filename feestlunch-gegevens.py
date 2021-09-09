Naam = input('Uw naam:')
Adres = input('Adres:')
Postcode = input('Postcode:')
Woonplaats = input('Woonplaats:')

#Gegevens

print("Naam: " + Naam)
print("Adres: " + Adres)
print("Postcode: " + Postcode)
print("Woonplaats: " + Woonplaats)


# Prijzen
print("Bestellen")
S = input("Aantal stokbroodjes: ")
C = input("Aantal Criossantjes: ")
P = S + C

print("Te betalen: €" + P )

#Betaalmiddel
print("Hoe wilt u betalen?")
print("Paypal")
print("iDeal")

Betaalmiddel = input("Uw Betaalmiddel: ")
print("U word verzonden naar uw aanbieder...")