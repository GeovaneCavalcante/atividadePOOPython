from ClassSegu import estoque

def adm():
    q = estoque ("Arroz", 25, 0)
    print(q.descriçao())
    q.darbaixa(6)
    q.repor(9)
    print(q.descriçao())
    if (q.check()==False):
        print("Não precisa repor")
    else:
        print("Precisa repor")

adm()
