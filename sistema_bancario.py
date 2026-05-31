#Importação Json
import json

usuario_certos = {}

try:
    with open('usuario.json', 'r', encoding='utf-8') as arquivo:
        usuario_certos = json.load(arquivo)
except FileNotFoundError:
    usuario_certos = {}

#Funções de arquivos
def salvar_usuarios():
    
    with open('usuario.json', 'w', encoding='utf-8') as arquivo:
        json.dump(usuario_certos, arquivo, indent=4)


#Funções bancarias
def deposito(usuario):
    try:
        valor = float(input('\nValor do depósito: '))
    except ValueError:
        print('Digite apenas numeros')
        return

    if valor <= 0:
        print('Valor inválido')
    else:  
        usuario_certos[usuario]['saldo'] += valor

        usuario_certos[usuario]['extrato'].append(
            f'Depósito: +R$ {valor:.2f}'
        )

        salvar_usuarios()

        print('Depósito realizado!')
        print(f"Saldo atual: R$ {usuario_certos[usuario]['saldo']:.2f}")


def saque(usuario):
    try:
        valor = float(input('\nDigite o valor do saque: '))
    except ValueError:
        print('Digite apenas numeros')
        return
    if valor <= 0:
        print('Valor inválido')

    elif valor <= usuario_certos[usuario]['saldo']:

        usuario_certos[usuario]['saldo'] -= valor

        usuario_certos[usuario]['extrato'].append(
            f'Saque: -R$ {valor:.2f}'
        )

        salvar_usuarios()

        print('Saque realizado!')
        print(f"Saldo atual: R$ {usuario_certos[usuario]['saldo']:.2f}")

    else:
        print('Saldo insuficiente!')


def saldo(usuario):
    print(f"\nSeu saldo é R$ {usuario_certos[usuario]['saldo']:.2f}")


def transferencia(usuario):
    destinatario = input('\nDestinatário: ').lower()

    if destinatario == usuario:
        print('Você não pode transferir para si mesmo')

    elif destinatario in usuario_certos:
        try:
            valor = float(input('Valor da transferência: '))
        except ValueError:
            print('Digite apenas numeros')
            return
        if valor <= 0:
            print('Valor inválido')

        elif valor <= usuario_certos[usuario]['saldo']:

            usuario_certos[usuario]['saldo'] -= valor
            usuario_certos[destinatario]['saldo'] += valor

            usuario_certos[usuario]['extrato'].append(
                f'Transferência para {destinatario}: -R$ {valor:.2f}'
            )

            usuario_certos[destinatario]['extrato'].append(
                f'Transferência recebida de {usuario}: +R$ {valor:.2f}'
            )

            salvar_usuarios()

            print('Transferência realizada!')

        else:
            print('Saldo insuficiente!')

    else:
        print('Usuário não encontrado!')


def extrato(usuario):
    print('\n=== EXTRATO ===')

    if not usuario_certos[usuario]['extrato']:
        print('Nenhuma movimentação encontrada')

    else:
        for movimentacao in usuario_certos[usuario]['extrato']:
            print(movimentacao)

#Sistema de cadastro
def cadastro():
    novo_usuario = input('\nNovo usuário: ').lower()
    nova_senha = input('Nova senha: ')

    if novo_usuario in usuario_certos:
        print(f'\nO usuário "{novo_usuario}" já existe!')

    else:
        usuario_certos[novo_usuario] = {
            'senha': nova_senha,
            'saldo': 0,
            'extrato': []
        }

        salvar_usuarios()
        print('Usuário criado com sucesso!')

#Programa principal
while True:

    print('\n=== Sistema de Login NuBank ===')
    print('\n1 - Login')
    print('2 - Cadastro')
    print('3 - Sair')

    opcao = input('\nDigite a opção desejada: ')

    if opcao == '1':

        tentativas = 3

        while tentativas > 0:

            usuario = input('\nDigite o usuário: ').lower()
            senha = input('Digite a senha: ')

            if (
                usuario in usuario_certos
                and usuario_certos[usuario]['senha'] == senha
            ):

                if 'extrato' not in usuario_certos[usuario]:
                    usuario_certos[usuario]['extrato'] = []
                    salvar_usuarios()

                print(f'\nSeja bem-vindo {usuario}!')

                
                
                while True:

                    print('\n1 - Depósito')
                    print('2 - Saque')
                    print('3 - Saldo')
                    print('4 - Transferência')
                    print('5 - Extrato')
                    print('6 - Logout')

                    escolha = input('\nEscolha: ')

                    if escolha == '1':
                        deposito(usuario)

                    elif escolha == '2':
                        saque(usuario)

                    elif escolha == '3':
                        saldo(usuario)

                    elif escolha == '4':
                        transferencia(usuario)

                    elif escolha == '5':
                        extrato(usuario)

                    elif escolha == '6':
                        print('Logout realizado!')
                        break

                    else:
                        print('Opção inválida')

                break

            else:

                tentativas -= 1

                print('\nCredenciais inválidas!')

                if tentativas > 0:
                    print(f'Restam {tentativas} tentativas')
                else:
                    print('Usuário bloqueado!')

    elif opcao == '2':
        cadastro()

    elif opcao == '3':
        print('Sistema encerrado!')
        break

    else:
        print('Opção inválida')