def realizar_operacao(operacao, num1, num2):
    if operacao == 'soma':
        resultado = num1 + num2
        print('{} + {} = {}'.format(num1, num2, resultado))
    elif operacao == 'subtracao':
        resultado = num1 - num2
        print('{} - {} = {}'.format(num1, num2, resultado))
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
        print('{} * {} = {}'.format(num1, num2, resultado))
    elif operacao == 'divisao':
        if num2 != 0:
            resultado = num1 / num2
            print('{} / {} = {}'.format(num1, num2, resultado))
        else:
            print('Erro: Divisão por zero!')
            return
    else:
        print('Operação inválida, por favor, tente novamente.')
        return

    return resultado


def main():
    operacao = input("Digite qual operação deseja fazer (soma, subtracao, multiplicacao, divisao): ")
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    resultado = realizar_operacao(operacao, num1, num2)

    if resultado is not None:
        novamente = input('Deseja fazer outra operação? (sim/nao): ')
        if novamente.lower() == 'sim':
            main()
        elif novamente.lower() == 'nao':
            print('Até depois!')
        else:
            print("Opção inválida. Obrigado por usar nosso programa!")

main()