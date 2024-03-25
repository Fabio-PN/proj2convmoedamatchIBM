# Criando um conversor de moedas usando uma API da Exchange Rate para consulta de cotação pela internet

import requests
print()
print('Conversor de moedas - Match!')
print('-'*28)

# Entrada do valor a ser convertido
print()

while True:
    valor_aconverter = input('Digite o valor a ser convertido: ').replace(',','.')
    try:
        valor_aconverter = float(valor_aconverter)
        break
    except:
       print('Valor incorreto. Favor digitar apenas números para conversão!')

print()

#Criação de um menu com opções
def menu():
    print('-'*34)
    print('Moedas disponíveis para conversão:')
    print('1 - Real - BRL')
    print('2 - Dólar - USD')
    print('3 - Euro - EUR')
    print('4 - Libra - GBP')
    print('5 - Encerra o programa')
    print('-' * 34)

# Validando a entrada da moeda de origem de acordo com a lista do menu
opcao_origem = 0
while opcao_origem != 5:
    menu()
    print()
    opcao_origem = int(input("Qual a moeda de origem? (Digite as opções de 0 a 4): "))
    if opcao_origem == 1:
        busca_origem = requests.get('https://v6.exchangerate-api.com/v6/053d0b76004be0863f1e5aee/latest/BRL')
        valor_origem = busca_origem.json()
        moeda1 = valor_origem['base_code']
        moeda_origem = str('real(ais)')
        print('A moeda de origem escolhida foi o(a) {}'.format(moeda_origem))
        break
    elif opcao_origem == 2:
        busca_origem = requests.get('https://v6.exchangerate-api.com/v6/053d0b76004be0863f1e5aee/latest/USD')
        valor_origem = busca_origem.json()
        moeda1 = valor_origem['base_code']
        moeda_origem = str('dólar(es)')
        print('A moeda de origem escolhida foi o(a) {}'.format(moeda_origem))
        break
    elif opcao_origem == 3:
        busca_origem = requests.get('https://v6.exchangerate-api.com/v6/053d0b76004be0863f1e5aee/latest/EUR')
        valor_origem = busca_origem.json()
        moeda1 = valor_origem['base_code']
        moeda_origem = str('euro(s)')
        print('A moeda de origem escolhida foi o(a) {}'.format(moeda_origem))
        break
    elif opcao_origem == 4:
        busca_origem = requests.get('https://v6.exchangerate-api.com/v6/053d0b76004be0863f1e5aee/latest/GBP')
        valor_origem = busca_origem.json()
        moeda1 = valor_origem['base_code']
        moeda_origem = str('libra(s)')
        print('A moeda de origem escolhida foi o(a) {}'.format(moeda_origem))
        break
    elif opcao_origem == 5:
        print('Encerrando o programa... Obrigado por usar o conversor de moedas!!!')
        exit()
    else:
        print('Opção inválida! Escolha outra opção entre 0 e 4')
print()
# Validando a entrada da moeda de destino de acordo com a lista do menu
opcao_destino = 0
while opcao_destino != 5:
    menu()
    print()
    opcao_destino = int(input("Qual a moeda de destino? (Digite as opções de 0 a 4): "))
    if opcao_destino == 1:
        busca_destino = requests.get('https://v6.exchangerate-api.com/v6/053d0b76004be0863f1e5aee/latest/BRL')
        valor_destino = busca_destino.json()
        moeda2 = valor_destino['conversion_rates']
        valor_moeda = float(moeda2[moeda1])
        moeda_destino = str('real(ais)')
        print('A moeda de destino escolhida foi o(a) {}'.format(moeda_destino))
        break
    elif opcao_destino == 2:
        busca_destino = requests.get('https://v6.exchangerate-api.com/v6/053d0b76004be0863f1e5aee/latest/USD')
        valor_destino = busca_destino.json()
        moeda2 = valor_destino['conversion_rates']
        valor_moeda = float(moeda2[moeda1])
        moeda_destino = str('dólar(es)')
        print('A moeda de destino escolhida foi o(a) {}'.format(moeda_destino))
        break
    elif opcao_destino == 3:
        busca_destino = requests.get('https://v6.exchangerate-api.com/v6/053d0b76004be0863f1e5aee/latest/EUR')
        valor_destino = busca_destino.json()
        moeda2 = valor_destino['conversion_rates']
        valor_moeda = float(moeda2[moeda1])
        moeda_destino = str('euro(s)')
        print('A moeda de destino escolhida foi o(a) {}'.format(moeda_destino))
        break
    elif opcao_destino == 4:
        busca_destino = requests.get('https://v6.exchangerate-api.com/v6/053d0b76004be0863f1e5aee/latest/GBP')
        valor_destino = busca_destino.json()
        moeda2 = valor_destino['conversion_rates']
        valor_moeda = float(moeda2[moeda1])
        moeda_destino = str('libra(s)')
        print('A moeda de destino escolhida foi o(a) {}'.format(moeda_destino))
        break
    elif opcao_destino == 5:
        print('Encerrando o programa... Obrigado por utilizar o conversor de moedas!!!')
        exit()
    else:
        print('Opção inválida! Escolha outra opção entre 0 e 4')
print()

# Calculando o valor inicial do programa com o câmbio do dia
valor_convertido = valor_aconverter / valor_moeda

# Exibição dos dados Apresentados e valores convertidos
print('O valor de {:.2f} {} é equivalente a {:.2f} {}!'.format(valor_aconverter,moeda_origem, valor_convertido, moeda_destino))
print('Conversão finalizada. Obrigado por usar o conversor de moedas!!!')