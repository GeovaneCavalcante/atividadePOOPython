from ClassPri import funcionario

def adm():
    q = funcionario("Zé do paulo", 20, 4.5)
    print("%s ganha %.1f por mês." % (q.getNome(), q.calcular()))

    q = funcionario("Paulo Preguiça", 10, 6.25)
    print("%s ganha %.1f por mês." % (q.getNome(), q.calcular()))

    q = funcionario("Toin Barca furada", 40, 13)
    print("%s ganha %.1f por mês.\n \n" % (q.getNome(), q.calcular()))

    a = 0
    while (a<=3):
        n1 = str(input("Digite o nome do funcionario %i: " % (a+1)))
        n2 = float(input("Quantas horas ele trabalhou: "))
        n3 = float(input("Digite quanto vale a hora dele:"))
        p = funcionario(n1, n2, n3)
        print("%s ganha %.1f por mês. \n" % (p.getNome(), p.calcular()))
        a+=1

adm()
