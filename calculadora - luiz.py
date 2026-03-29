while True:
    print(f'''
    
    
    
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Calculadora - Luiz\n
Indice de operacoes: 
+    ->   Soma
-    ->   Subtracao
*    ->   Multiplicacao
/    ->   Divisao
ou digite 'sair' para sair.''')

    num1 = input('\nDigite seu primeiro numero: ')
    if num1 == 'sair':
        print(f'''Voce escolheu sair.
Fechando a calculadora...''')
        break
    opt = input('Digite o operador: ')
    if opt == 'sair':
        print(f'''Voce escolheu sair.
Fechando a calculadora...''')
        break
    num2 = input('Digite seu segundo numero: ')
    if num2 == 'sair':
        print(f'''Voce escolheu sair.
Fechando a calculadora...''')
        break
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
         print('Valor invalido, tente usar apenas numeros ou "sair" para sair.')
         continue

    if opt == '+':
        resultado = num1 + num2
    elif opt == '-':
        print(f'\n{num1} {opt} {num2}')
        resultado = num1 - num2
    elif opt == '*':
        print(f'\n{num1} {opt} {num2}')
        resultado = num1 * num2
    elif opt == '/':
        if num2 != 0:
            print(f'\n{num1} {opt} {num2}')
            resultado = num1 / num2
        else:
            print(f'Erro: divisao por zero!')
    else:
        print(f'Operador invalido.')
    print(f'Resultado: {resultado} <-')
    continue
    
    #26/03/2026 ~ 30 min