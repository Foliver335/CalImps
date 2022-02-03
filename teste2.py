# IRPF CALCULATOR
# https://receita.economia.gov.br/interface/cidadao/irpf/2020/declaracao/preenchimento
import webbrowser

def calculo():


    if renda_por_calculo <= 2500:
        print('isento')
        faixa = 0
        irfaixa = 0
        vaproxano = 0
        return [faixa, renda_por_calculo, irfaixa, vaproxano]
    # Valor calculado o qual haverá deduçoes
    # Calculo = (VALOR DA FAIXA / 100)  * ALIQUOTA/ VALOR DA FAIXA - DEDUÇÃO
    # O governo nao cobra a aliquota do recebedor do salario sobre o valor integral
    # recebido, mas sim, do valor de isenção até o seu valor recebido. VOcê não paga tributo da parte que é isenta

    if  renda_por_calculo > 2500.00 and renda_por_calculo <= 3200.00:
        faixa = 1
        irfaixa = (renda_por_calculo / 100) * 7.5 - 142.8
        valmensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é:', valmensal)
        vaproxano = irfaixa * 12
        varredano = "{:.2f}".format(vaproxano)
        print('o valor aproximado anual do tributo é', varredano)
        return [faixa, renda_por_calculo, irfaixa, vaproxano]

    if renda_por_calculo > 3200.01 and renda_por_calculo <= 4250.00:
        faixa = 2
        irfaixa = (renda_por_calculo / 100) * 15 - 354.8
        valmensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é:', valmensal)
        vaproxano = irfaixa * 12
        varredano = "{:.2f}".format(vaproxano)
        print('o valor aproximado anual do tributo é', varredano)
        return [faixa, renda_por_calculo, irfaixa, vaproxano]

    if renda_por_calculo > 4250.01 and renda_por_calculo <= 5300.00:
        faixa = 3
        irfaixa = (renda_por_calculo / 100) * 22.5 - 636.13
        valmensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é:', valmensal)
        vaproxano = irfaixa * 12
        varredano = "{:.2f}".format(vaproxano)
        print('o valor aproximado anual do tributo é', varredano)
        return [faixa, renda_por_calculo, irfaixa, vaproxano]

    if renda_por_calculo > 5300.01:
        faixa = 4
        irfaixa = (renda_por_calculo / 100) * 27.5 - 869.36
        valmensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é: ', valmensal)
        vaproxano = irfaixa * 12
        varredano = "{:.2f}".format(vaproxano)
        print('o valor aproximado anual do tributo é', varredano)
        return [faixa, renda_por_calculo, irfaixa, vaproxano]


print('Insira abaixo o valor mensal referente ao ano de exercicio (2022)')


while True:

    renda_por_calculo: str = input("Valor mensal de renda: ")

    try:

        renda_por_calculo = float(renda_por_calculo)
        calculosemdesconto = calculo()
        break

    except:
        print('Favor inserir valor numérico')

print('O valor de referencia é o valor do tributo devido sem a adição de descontos.')

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
        renda_por_calculo = input('Valor: ')

        try:

            renda_por_calculo = float(renda_por_calculo) / 12
            renda_por_calculo = calculosemdesconto[1] - renda_por_calculo
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
    print('não será necessário passar pela segunda fase do cálculo')
