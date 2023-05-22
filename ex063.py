# leia um número n e mostre os n primeiros elementos de uma sequencia de Fibonacci

t = int(input("Quantos termos da sequencia de Fibonnati você gostaria de ver? :"))
f1 = 1
f2 = 1
f3 = 1
c = 1

if t > 0:
    print(f1, end=" ")

while c < t:
    print(f1, end=" ")
    f1 = f2 + f3
    f3 = f2
    f2 = f1
    c += 1

print(" Fim!")