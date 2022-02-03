# IRPF CALCULATOR
# https://receita.economia.gov.br/interface/cidadao/irpf/2020/declaracao/preenchimento
import webbrowser


def calculo():

    if rendapcalc <= 1903.98:
        print('isento')
        faixa = 0
        irfaixa = 0
        vaproxano = 0
        return [faixa, rendapcalc, irfaixa, vaproxano]
    # Valor calculado o qual haverá deduçoes
    # Calculo = (VALOR DA FAIXA / 100)  * ALIQUOTA/ VALOR DA FAIXA - DEDUÇÃO
    # O governo nao cobra a aliquota do recebedor do salario sobre o valor integral
    # recebido, mas sim, do valor de isenção até o seu valor recebido. VOcê não paga tributo da parte que é isenta

    if rendapcalc > 1903.98 and rendapcalc <= 2826.65:
        faixa = 1
        irfaixa = (rendapcalc / 100) * 7.5 - 142.8
        valmensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é:', valmensal)
        vaproxano = irfaixa * 12
        varredano = "{:.2f}".format(vaproxano)
        print('o valor aproximado anual do tributo é', varredano)
        return [faixa, rendapcalc, irfaixa, vaproxano]

    if rendapcalc > 2826.65 and rendapcalc <= 3751.05:
        faixa = 2
        irfaixa = (rendapcalc / 100) * 15 - 354.8
        valmensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é:', valmensal)
        vaproxano = irfaixa * 12
        varredano = "{:.2f}".format(vaproxano)
        print('o valor aproximado anual do tributo é', varredano)
        return [faixa, rendapcalc, irfaixa, vaproxano]

    if rendapcalc > 3751.05 and rendapcalc <= 4664.68:
        faixa = 3
        irfaixa = (rendapcalc / 100) * 22.5 - 636.13
        valmensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é:', valmensal)
        vaproxano = irfaixa * 12
        varredano = "{:.2f}".format(vaproxano)
        print('o valor aproximado anual do tributo é', varredano)
        return [faixa, rendapcalc, irfaixa, vaproxano]

    if rendapcalc > 4664.68:
        faixa = 4
        irfaixa = (rendapcalc / 100) * 27.5 - 869.36
        valmensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é: ', valmensal)
        vaproxano = irfaixa * 12
        varredano = "{:.2f}".format(vaproxano)
        print('o valor aproximado anual do tributo é', varredano)
        return [faixa, rendapcalc, irfaixa, vaproxano]


print('Insira abaixo o valor mensal auferido no ano de 2019')


while True:

    rendapcalc: str = input("Valor mensal de renda: ")

    try:

        rendapcalc = float(rendapcalc)
        calculosemdesconto = calculo()
        break

    except:
        print('Favor inserir valor numérico')

print('O valor acima é o valor do tributo devido sem adição de descontos.')

if calculosemdesconto[0] != 0:

    print('Como o seu tributo não retornou como isento, vamos ao cálculo de descontos')
    print('da base de cálculo, para sabermos se há a possibilidade de restituição.')
    print('Deseja abrir uma dica de como reduzir seus impostos?')
    answer = input("(Y/N)")
    if answer == "y":
        print('Seu browser abrirá em seguida página para verificação dos valores os quais')
        print('é possível deduzir da base de cálculo acima impressa para a declaração.')
        webbrowser.open('https://blog.nubank.com.br/deduzir-imposto-de-renda-2020/')
    # Do this.
    elif answer == "n":
        tipo = None

    while tipo is None:

        print('Após consultar e somar os valores para dedução, insira o valor todal anual')
        print('em reais e centavos abaixo.')
        rendapcalc = input('Valor: ')

        try:

            rendapcalc = float(rendapcalc) / 12
            rendapcalc = calculosemdesconto[1] - rendapcalc
            comdescontos = calculo()
            tipo = 1

        except:
            print('Favor inserir valor numérico')

    valoranosemd = float(calculosemdesconto[3])
    saldopcalc = float(comdescontos[3])

    if saldopcalc > 0:
        valorrestituicao = abs(saldopcalc - valoranosemd)
        valorrestituicao = "{:.2f}".format(float(valorrestituicao))
        saldopcalc = "{:.2f}".format(float(saldopcalc))
        print('O valor final de adimplemento do tributo ficou no valor (em reais) de: ', saldopcalc)
        print('A sua restituição de IR ficou no valor (em reais) de: ', valorrestituicao)

    else:
        valorrestituicao1 = "{:.2f}".format(calculosemdesconto[3])
        print('A sua restituição de IR ficou no valor (em reais) de: ', valorrestituicao1)
        print('situação de restituição do valor total do tributo, equivalente')
        print('ao ato de ficar isento ^^')

else:
    print('Como na primeira fase do cálculo, o valor inserido lhe coloca como isento,')
    print('não é necessário passar pela segunda fase do cálculo')