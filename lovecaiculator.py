name1=(input("Enter your Name:"))
name2=(input("Enter your Partner Name:"))
Bothnames=name1+name2
print(Bothnames)
small_letters=Bothnames.lower()
print(small_letters)
t=small_letters.count('t')
r=small_letters.count('r')
u=small_letters.count('u')
e=small_letters.count('e')
true=t+r+u+e
l=small_letters.count('l')
o=small_letters.count('o')
v=small_letters.count('v')
e=small_letters.count('e')
love=l+o+v+e
lovescore=int(str(true)+str(love))
if lovescore < 10 or lovescore > 90:
    print("you are very lucky to have your partner")
elif lovescore<=40 or lovescore>=50:
    print("you are the unique couple in the world")
