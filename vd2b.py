print('TINH GIA TRI BIEU THUC 1 - x + (x^3)/3! - (x^5)/5! + (x^7)/7! ... (x^n)/n!')
print('Lan luot nhap gia tri x, n (so nguyen va >0):')
x = int(input())
n = int(input())
s = 0
t = 1
a = 1

for i in range (n+1):
    s = ((-1)**(i+1))*(x**(2*i+1))
    for j in range (2*i+1):
        t = t*(j+1)
    a += s/t
print('Bieu thuc da cho =', a)