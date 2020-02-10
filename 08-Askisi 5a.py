#-*- coding: utf-8 -*-

##5. Να καταχωρήσετε τους κωδικούς 30 προϊόντων και τις τιμές τους. 
##Να καταχωρήσετε σε 2 ξεχωριστούς πίνακες τα προϊόντα ανάλογα
##με τον κωδικό τους (Α’ κατηγορία, όσα λήγουν σε 0-4, Β’ κατηγορία
##όσα λήγουν σε 5-9). Ποια κατηγορία έχει τα ακριβότερα
##κατά μέσο όρο προϊόντα. (Χρησιμοποιείστε συνάρτηση για τον 
##υπολογισμό του μέσου όρου κάθε λίστας) 
##Να εμφανίσετε τους κωδικούς προϊόντων
##της Α’ κατηγορίας από το φθηνότερο προς το ακριβότερο.

def mo(L):
    total = 0.0
    pl = 0
    for item in L:
        total += item
        pl += 1
    if pl != 0:
        mesor = total/pl
    else:
        mesor = 0
    return mesor
    
code = []
price1 = []
price2 = []
code1 = []
for i in range(5):
    c = raw_input("Δώσε κωδικό προϊόντος: ")
    p = input("Δώσε τιμή προϊόντος: ")
    code.append(c)
    if c[-1] >= "0" and c[-1] <= "4":
        price1.append(p)
        code1.append(c)
    else:
        price2.append(p)


a = mo(price1)
b = mo(price2)

if a > b:
    print "Τα ακριβότερα προϊόντα τα έχει η κατηγορία Α'."
else:
    print "Τα ακριβότερα προϊόντα τα έχει η κατηγορία Β'."

print "Κωδικοί προϊόντων: "
for item in code:
    print item


N = len(price1)

for i in range(N-1):
    for j in range(N-1, i, -1):
        if price1[j] < price1[j-1]:
            price1[j],price1[j-1] = price1[j-1],price1[j]
            code1[j],code1[j-1] = code1[j-1],code1[j]
            
print "Κωδικοί κατηγορίας Α':"
print code1
