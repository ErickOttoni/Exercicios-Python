soma=0
qnt=0
for i in range (1,101):
    if i%2==0:
        print(i)
        soma+=i
        qnt+=1
med=soma/qnt
print(med)