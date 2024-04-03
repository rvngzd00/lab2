#5
#B(n) ədədi massivinin(siyahının) mənfi elementlərinin cəmini hesablayan alqoritm tərtib etməli

B=input('Enter the list of numbers: ').split()
su=0

for n in B:
    if int(n)<0:su+=int(n)
print(su)