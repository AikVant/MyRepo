#-*- coding: utf-8 -*-

##6. (Βλέπε Σχ. βιβλίο σελ 56 - Παραλλαγή) Σε έναν αθλητικό μαθητικό αγώνα στίβου,
##στο αγώνισμα του μήκους, συμμετέχουν στους προκριματικούς 20 μαθητές. Στον τελικό περνούν
##όσοι μαθητές σημειώσουν επίδοση μεγαλύτερη ή ίση από 4.5 μέτρα. Κάθε αθλητής έχει 3 προσπάθειες.
##Αν σημειώσει επίδοση ίση ή μεγαλύτερη από το όριο πρόκρισης, σταματάει τις προσπάθειες.  
##Να γραφεί πρόγραμμα σε Python, που να διαβάζει τα ονόματα και τις επιδόσεις των αλμάτων κάθε 
##αθλητή. Οι αθλητές που  προκρίθηκαν και η καλύτερη επίδοσή τους  εισάγονται σε δύο λίστες.
##Στο τέλος εμφανίζει στην οθόνη τους αθλητές που προκρίθηκαν και την καλύτερη επίδοση που 
##σημείωσαν. 

name = []
epidosi = []
for i in range(5):
    n = raw_input("Δώσε το όνομα του αθλητή: ")
    pr = 1
    ep = input("Δώσε την επίδοση του αθλητή: ")
    while ep < 4.5 and pr < 3:        
        ep = input("Δώσε την επίδοση του αθλητή: ")
        pr += 1
    if ep >= 4.5 and pr <= 3:
        print "Ο αθλητής", n, "προκρίθηκε με επίδοση", ep, u"στην", pr, "προσπάθεια. "
        name.append(n)
        epidosi.append(ep)
    else:
        print "Ο αθλητής", n, "δεν προκρίνεται."

print "Οι αθλητές που προκρίθηκαν είναι:"

for i in range(len(name)):
    print name[i], u"με επίδοση", epidosi[i]
