"""
programare dinamica
Se calculeaza suma posibila pt fiecare numar de elemente preluate din lista data folosindu-se de o matrice de sume
pentru eficienta

Problema se putea rezolva mai ineficient calculand fiecare combinatie de (lungime lista) luate cate k si verificand fiecare suma
"""

# suma elementelor dintr-o partitie trebuie sa fie egala cu (lungimea ei *suma totala)/lungime toatala
# plecam de la premiza ca cele 2 diviziuni trebuie sa aiba media aritmetica egala intre ele chiar daca nu au acelasi numar de elemente
# se verifica pentru fiecare combinatie de lungime
def verifica(lungime_div2, suma, lungime):
    for i in range(1, lungime_div2 + 1):
        if suma * i % lungime == 0:
            return True
    return False


def split_array_average(list_A):
    lungime = len(list_A)
    lungime_div2 = lungime // 2
    suma = sum(list_A)

    # conditie necesara pentru a putea imparti vectorul in 2 vectori cu media aritmetica egala
    if not verifica(lungime_div2, suma, lungime):
        return False

    # initializare suma_partiala o lista formata din liste (matrice) care pastreaza fiecare suma partiala pana la un 
    # moment dat, se foloseste set in loc de lista normala pentru a nu retine toate duplicatele astfel reducandu-se 
    # complexitatea de memorie 
    suma_partiala = [set([0]) for _ in range(lungime_div2 + 1)]

    # fiecare rand reprezinta sumele posibile cu i elemente
    # se merge doar de la lungime/2 pentru ca apoi se repeta in oglinda n1=2 n2=7 si n1=7 n2=2 n1,n2 fiind diviziuni
    # se folosesc sumele deja calculate la care se adauga doar elementul curent
    # i merge in ordine inversa pentru a putea adauga fiecare numar in suma cu i elemente fara a strica suma initiala
    for index in range(len(list_A)):
        for i in range(lungime_div2, 0, -1):
            suma_partiala[i] |= set([t + list_A[index] for t in suma_partiala[i - 1]])

    # se verifica din nou ca diviziunea sa fie valida cu formula (suma*i%lungime) si
    # cautam valoare optinuta in suma_partiala
    for i in range(1, lungime_div2+1):
        if suma * i % lungime == 0 and suma * i // lungime in suma_partiala[i]:
            return True

    return False

print(split_array_average([1, 2, 3, 4, 5, 6, 7, 8]))