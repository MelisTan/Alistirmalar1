import math

toplam = 0
n = 0
while n<1000:
    toplam = toplam + (1 / math.factorial(n))
    exp = toplam
    n = n + 1

print(exp)
print(math.exp(1))

# Bu soruda da bir önceki soruyla aynı şeyi düşünerek yapmaya çalıştım.
while True:
    toplam = toplam + (1 / math.factorial(n))
    exp = toplam
    n = n + 1
    if exp == math.exp(1):
        print(exp)
        break
