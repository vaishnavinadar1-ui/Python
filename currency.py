pesos = int(input("how much do you have left in pesos? "))
soles = int(input("how much do you have left in soles? "))
reais = int(input("how much do you have left in reais? "))

# Exchange rates to USD
pesos_to_usd = 0.00027
soles_to_usd = 0.286
reais_to_usd = 0.198

total_usd = (pesos * pesos_to_usd) + (soles * soles_to_usd) + (reais * reais_to_usd)

print(total_usd)