# o programa le um numero e mostra a tabuada
# o programa só para quando o valor digitado for negativo
while True:
    num = int(input("\nInsira um número para exibir a sua tabuada (numero negativo para parar): "))
    if num < 0:
        break
    c = 1
    print("\n"+("="*12))
    while c <= 10:
        print(f"{num} x {c} = {num*c}")
        c += 1
    print("="*12)
