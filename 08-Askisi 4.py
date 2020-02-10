#-*- coding: utf-8 -*-

##4. Να καταχωρήσετε τα ονόματα και το ύψος (cm) των  μαθητών μιας τάξης.
##Σταµατάει η είσοδος των δεδοµένων όταν δοθεί αντί για όνοµα το γράµµα “Τ” 
##Να υπολογίσετε τον ΜΟ του ύψους της τάξης.  
##Να εμφανίσετε πόσοι μαθητές έχουν ύψος από 140 εώς 150 cm. 
##Να εμφανίσετε τα ονόματα των 5 ψηλότερων

total = 0.0
pl = 0
name = []
height = []
n = raw_input("Δώστε όνομα μαθητή. Δώστε 'Τ' για τέλος: ")
while n != "T":
    h = input("Δώστε ύψος μαθητή: ")
    total += h
    pl += 1
    name.append(n)
    height.append(h)
    n = raw_input("Δώστε όνομα μαθητή. Δώστε 'Τ' για τέλος: ")

print name
print height

if pl != 0:
    mo = total/pl
else:
    mo = 0
print "Μέσος όρος ύψους τάξης:", mo

pl2 = 0

for item in height:
    if item >= 140 and item <= 150:
        pl2 += 1
    
print pl2, "μαθητές έχουν ύψος από 140 έως 150 cm."

N = len(height)

for i in range(N-1):
    for j in range(N-1, i, -1):
        if height[j] > height[j-1]:
            height[j], height[j-1] = height[j-1], height[j]
            name[j], name[j-1] = name[j-1], name[j]

print height
print name
print "Οι πέντε ψηλότεροι μαθητές είναι οι:", name[0:5]

    
            
                
 
