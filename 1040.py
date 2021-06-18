# 1040 - Averange 3
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

ave = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

print("Media %0.1f" % ave)

if ave >= 7.0 :
    print("Aluno aprovado.\n")
elif ave < 5.0 :
    print("Aluno reprovado.\n")
elif ave >= 5.0 and ave < 7 :
    print("Aluno em exame.\n")
    ac = float(input())
    ac = (ac+ave)/2

    if ac >= 5.0 :
        print("Aluno aprovado.")
    else :
        print("Aluno reprovado.")
    
    print("Media final: %0.1f\n" % ac)
