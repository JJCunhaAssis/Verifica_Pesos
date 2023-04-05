temp = []
princ = []
maior = men = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    resposta = input("Quer continuar?  [S/N]  ")
    if resposta in 'Nn':
        print('Programa encerrado')
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas\n')

print(f'O maior peso foi de {mai}kg, e o menor foi de {men}kg.\n')
for p in princ:
    if p[1] == mai:
        print(f'Maiores pesos de: \n{p[0]}')
    if p[1] == men:
        print(f'Menores pesos de: \n{p[0]}\n')
