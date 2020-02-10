#-*- coding: utf-8 -*-

##3. Να καταχωρήσετε σε λίστες τα ονόματα 20 μαθητών και τη βαθμολογία τους όπως προκύπτει 
##από το άθροισμα των βαθμών τους  σε 4 μαθήματα πανελλαδικής εξέτασης. 
##Δηλαδή για κάθε  μαθητή θα εισάγετε 4 βαθμούς αλλά στη λίστα της βαθμολογίας θα εισάγετε το 
##άθροισμά τους. 
##Να εμφανίσετε το όνομα του μαθητή με την μεγαλύτερη βαθμολογία.

name = []
grade = []

for i in range(3):
    n = raw_input("Δώστε όνομα μαθητή: ")
    name.append(n)
    total = 0
    for j in range(4):
        g = input("Δώστε το βαθμό του μαθητή: ")
        total += g   
    grade.append(total)

print name
print grade

maxg = grade[0]

for i in range(len(grade)):
    if grade[i] > maxg:
        maxg = grade[i]
        maxname = name[i]
    else:
        maxname = name[0]

print "Ο μαθητής", maxname, "με σύνολο βαθμών", maxg, "έχει τη μεγαλύτερη βαθμολογία" 
    
    

