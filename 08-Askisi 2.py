#-*- coding: utf-8 -*-

##2. Να καταχωρήσετε σε λίστα τα ονόματα 10 αθλητών και την επίδοσή τους σε cm στο μήκος.  
##Να γίνει έλεγχος ορθότητας τιμών. Η επίδοση τους πρέπει να είναι θετικός αριθμός >0.   
##Να υπολογίσετε το ΜΟ των επιδόσεων. 
##Να εμφανίσετε τα ονόματα των αθλητών που τον ξεπερνούν. 

total = 0.0
pl = 0
name = []
epidosi = []
for i in range(3):
    n = raw_input("Δώστε όνομα αθλητή: ")
    ep = input("Δώστε επίδοση αθλητή: ")
    while ep <= 0:
        ep = input("Κάνατε λάθος. Δώστε επίδοση αθλητή: ")
    total += ep
    pl += 1
    name.append(n)
    epidosi.append(ep)

if pl != 0:
    mo = total/pl
else:
    mo = 0

print "Επίδοση άνω του μέσου όρου εμφάνισαν οι αθλητές:"

for i in range(len(epidosi)):
    if epidosi[i] > mo:
        print name[i]
    else:
        nobody = 0
if nobody == 0:
    print "Κανένας αθλητής δεν εμφάνισε επίδοση άνω του μέσου όρου."








        
