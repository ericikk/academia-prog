def verificar_triangulo():
    r1 = float(input('Primeiro Lado: '))
    r2 = float(input('Segundo Lado: '))
    r3 = float(input('Terceiro Lado: '))

    if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
        print('Não é Triângulo')
    elif (r1 == r2) and (r1 == r3):
        print('Equilátero')
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('Isósceles')
    else:
        print('Escaleno')

while True:
    print("\nMenu:")
    print("1. Verificar um novo triângulo")
    print("2. Sair")
    
    opcao = input("Escolha uma opção (1 ou 2): ")

    if opcao == '1':
        verificar_triangulo()
    elif opcao == '2':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Por favor, escolha 1 ou 2.")