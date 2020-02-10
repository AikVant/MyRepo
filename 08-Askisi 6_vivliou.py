#-*- coding: utf-8 -*-

##6. (Βλέπε Σχ. βιβλίο σελ 56 - Αυτούσιο) Σε έναν αθλητικό μαθητικό αγώνα στίβου,
##στο αγώνισμα του μήκους, συμμετέχουν στους προκριματικούς 20 μαθητές από όλα τα
##σχολεια της περιφέρειας. Στον τελικό περνούν όσοι μαθητές σημειώσουν επίδοση μεγαλύτερη
##ή ίση από 4.5 μέτρα. Κάθε αθλητής έχει 3 προσπάθειες. Αν σημειώσει επίδοση ίση ή μεγαλύτερη
##από το όριο πρόκρισης, σταματάει τις προσπάθειες.
##Να γραφεί αλγόριθμος και στη συνέχεια αντίστοιχο πρόγραμμα σε Python, που να διαβάζει
##τις επιδόσεις των αλμάτων κάθε αθλητή και να υπολογίζει την καλύτερη επίδοσή του. Να ελέγχει
##δίνοντας ανάλογο μήνυμα στην οθόνη αν ο αθλητής προκρίθηκε ή όχι στον τελικό και τελικά
##να εμφανίζει στην οθόνη, πόσοι αθλητές προκρίθηκαν και ποιά ήταν η καλύτερη επίδοση που σημειώθηκε.


max_all = 0
pl = 0
for i in range(5):
    name = raw_input("Δώσε το όνομα του αθλητή: ")
    max_ep = 0
    pr = 1
    ep = input("Δώσε την επίδοση του αθλητή: ")
    while ep < 4.5 and pr <= 3:
        pr += 1
        if ep > max_ep:
            max_ep = ep
            max_name = name
        if pr > 3:
            print "Ο αθλητής δεν προκρίθηκε. Η καλύτερη επίδοσή του ήταν", max_ep
        else:
            ep = input("Δώσε την επίδοση του αθλητή: ")

    if ep >= 4.5 and pr <= 3:
        max_ep = ep
        pl += 1
        print "Ο αθλητής", name, "προκρίθηκε με επίδοση", max_ep, u"στην", pr, "προσπάθεια. "

    if max_ep > max_all:
        max_all = max_ep
        max_all_name = name

print "Προκρίθηκαν", pl, u"αθλητές."
print "Την καλύτερη επίδοση σημείωσε ο αθλητής", max_all_name, u"με", max_all, u"επίδοση."
