import math
toplam = 0
n = 1
while n<1000:
    toplam = toplam + (1 / n ** 2)
    pi = (6 * toplam) ** (1 / 2)
    n = n + 1

print(pi)
# gerçek değeri ile karşılaştırmak için math sınıfını kullandım
print(math.pi)

# Döngüyü bu şekilde kurmak da mantıklı geldi ancak sanırım sonsuz toplam
# olduğu için sonsuz döngüden çıkamıyorum. Bu yüzden yaklaşık değer bulabilmek
# için döngünün belli bir değere kadar tekrar etmesini sağladım.
while True:
    toplam = toplam + (1 / n ** 2)
    pi = (6 * toplam) ** (1 / 2)
    n = n + 1

    if pi == math.pi:
        print(pi)
        break
