
capital = float(input("capital: "))
interes = float(input("interés %: ")) / 100
años = int(input("años: "))
final = capital * (1 + interes) ** años
print(final)