a = [1, 2]
b = [2, 3]
c = a
d = [9, 10]
x = [a, b, d]
x.remove(c)
print(x)



'''
x = 30
x %= 9
if x:
    print("YES")
else:
    print("NO")

x = {"1", "2", "3"}
y = {"1", "2", "3"}
z = {"1", "2", "3"}
if x:
    z.remove("1")
elif y:
    z.add("4")
else:
    if z:
        z.remove("2")

print(z)

print([x for x in range(0,11) if x%2==0])

y = ""
x = 10
if y:
    print("A")
else:
    if x:
        print("B")
    else:
        print("C")

x = 5
print(str(x) * x)

a = 20
a %= 3
if a:
    print(a)
else:
    print(555)

x=1
y=[0]
z=0
t=99
w = " "

if x:
    print(x)
if y:
    print(y)
if z:
    print(z)
if t:
    print(t)
if w:
    print(w)
'''