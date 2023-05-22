# o programa le varios valores e para quando o user digita 999
# mostre quantos valores foram digitados e a soma entre eles

c = soma = 0

while True:
    num = int(input("Insira um valor (digite 999 para encerrar e somar): "))
    if num == 999:
        break
    soma += num
    c += 1

print("\nEncerrando:\n")
print(f"Foram digitados {c} valores e a soma entre eles é {soma}\n")
