#-*- coding: utf-8 -*-

#Να εμφανίζει(συνέχεια άσκησης 1)
#∆3Ε. όλα τα στοιχεία των µαθητών  ταξινομημένους  αλφαβητική προς το όνομα 
#∆3ΣΤ. Τους μέσους όρους βαθμολογίας κάθε  πόλης 

city = ["preveza", "ioannina", "arta", "ioannina", "arta",  "xios",  "xios", "soufli" ]
grade = [12,19,18,16,15,20,12,19]
name = ["petros","nikos","gianna", "lena", "kostas", "anna", "maria", "thanasis"]



N=len(name)-1
for i in range(N-1):
    for j in range(N-1,i,-1):
        if name[j]<name[j-1]:
            name[j],name[j-1]=name[j-1],name[j]
            city[j],city[j-1]=city[j-1],city[j]
            grade[j],grade[j-1]=grade[j-1],grade[j]
print name
print city
print grade

city_one = []
for item in city:
    if item not in city_one:
        city_one.append(item)

print city_one

for i in range(len(city_one)):
    print "-" * 50 
    pl = 0
    total = 0.0
    for j in range(len(city)):      
        if city_one[i]==city[j]:
            pl += 1
            total += grade[j]
    if pl != 0:
        mo = total/pl
        print "Στην πόλη", city_one[i], "ο μέσος όρος βαθμολογίας είναι", mo
    else:
        mo = 0
            
