import string
import random 

a1 = string.ascii_lowercase
a2 = string.ascii_uppercase
a3 = string.octdigits
a4 = string.hexdigits
a5 = string.punctuation
passlen = int(input("\n Enter the length of your password: "))

p = []
p.extend(list(a1))
p.extend(list(a2))
p.extend(list(a3))
p.extend(list(a4))
p.extend(list(a5))

print("Your password is: ")
print("".join(random.sample(p,passlen)))

