#  algorithme : facture
#   variables : 
#  HT,j,nbr,i,s:réels
#  tableau somme(3):réels
#  tableau nom(3):chaine de caractères
#  début
#       pour i --> 0 à 2 pas 1 faire 
#          ecrire("entrer le nom complet du client numéro : ",i+1," svp : ")
#          lire(nom(i))
#          ecrire("entrer le nombre d'article svp : ")
#          lire(nbr)
#          s<--0
#          pour j--> 1 à nbr pas 1 faire 
#              ecrire ("entrer le prix HT d'article numéro :",j," svp : ")
#              lire(HT)
#              s<-- s + HT*1.13
#          finpour
#        somme(i)<--s
#      finpour
#      pour i-->0 à 2 pas 1 faire 
#         ecrire("le prix ttc du client : ",nom(i)," est ",somme(i))
#      finpour
#   fin

nom=[]
somme=[]
client=int(input("entrer le nombre de clients svp : "))
for i in range (0,client) : 
    x=input(f"entrer le nom complet du client numéro {i+1} svp : ")
    nom.append(x)
    nbr=int(input("entrer le nombre d'article svp : "))
    s=0
    for j in range (1,nbr+1) :
        HT=float(input(f"entrer le prix HT d'article numéro {j} svp : "))
        s=s+HT*1.13
    somme.append(s)
for z in range (0,client) :
    print("le prix ttc du client : ",nom[z]," est : ",somme[z])

