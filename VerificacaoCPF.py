def validar_cpf_2(cpf):
    corpo_cpf = cpf[:9]
    digito_cpf = cpf[-2:]

    calculo_1 = 0
    calculo_2 = 0

    multiplicacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    for i, j in zip(multiplicacao, corpo_cpf):
        calculo_1 += i * int(j)
    # print(f'Cálculo 1: {calculo_1}')

    resto_1 = calculo_1 % 11
    # print(f'Resto 1: {resto_1}')

    digito_1 = 0 if resto_1 < 2 else 11 - resto_1
    # print(f'Dígito 1: {digito_1}\n')

    corpo_cpf += str(digito_1)

    for i, j in zip(multiplicacao, corpo_cpf[1:]):
        calculo_2 += i * int(j)

    # print(f'Cálculo 2: {calculo_2}')

    resto_2 = calculo_2 % 11
    # print(f'Resto 2: {resto_2}')

    digito_2 = 0 if resto_2 < 2 else 11 - resto_2
    # print(f'Dígito 2: {digito_2}')

    return digito_cpf == f'{digito_1}{digito_2}'


blocklist = [
    '00000000000',
    '11111111111',
    '22222222222',
    '33333333333',
    '44444444444',
    '55555555555',
    '66666666666',
    '77777777777',
    '88888888888',
    '99999999999'
]

while True:

    entrada = input('> Digite um CPF para validar ou X para sair: ')
    entrada_sem_ponto = entrada.replace('.', '')
    entrada_formatada = entrada_sem_ponto.replace('-', '')

    if entrada.isnumeric():

        if len(entrada) == 11:

            if entrada in blocklist:

                print('> O CPF não pode ter todos os números iguais!\n')

            else:

                if validar_cpf_2(entrada):
                    print('# CPF Válido!\n')

                else:
                    print('# CPF Inválido!\n')
        else:

            print('> O número de CPF deve ter 11 dígitos!\n')

    elif entrada.lower() == 'x':
        break

    else:
        print('> Digite apenas números ou X para sair.\n')

print('OPERAÇÃO ENCERRADA!!!')