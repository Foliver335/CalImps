# IRPF CALCULATOR
# https://receita.economia.gov.br/interface/cidadao/irpf/2020/declaracao/preenchimento
import webbrowser

def calculo():


    if renda_por_calculo <= int(2500):
        print('isento')
        faixa = 0
        irfaixa = 0
        valor_prox_ano = 0
        return [faixa, renda_por_calculo, irfaixa, valor_prox_ano]
    # Valor calculado o qual haverá deduçoes
    # Calculo = (VALOR DA FAIXA / 100)  * ALIQUOTA/ VALOR DA FAIXA - DEDUÇÃO
    # O governo nao cobra a aliquota do recebedor do salario sobre o valor integral
    # recebido, mas sim, do valor de isenção até o seu valor recebido. VOcê não paga tributo da parte que é isenta

    if  renda_por_calculo > 2500.00 and renda_por_calculo <= 3200.00:
        faixa = 1
        irfaixa = (renda_por_calculo / 100) * 7.5 - 142.8
        valor_mensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é:', valor_mensal)
        valor_prox_ano = irfaixa * 12
        var_red_ano = "{:.2f}".format(valor_prox_ano)
        print('o valor aproximado anual do tributo é', var_red_ano)
        return [faixa, renda_por_calculo, irfaixa, valor_prox_ano]

    if renda_por_calculo > 3200.01 and renda_por_calculo <= 4250.00:
        faixa = 2
        irfaixa = (renda_por_calculo / 100) * 15 - 354.8
        valor_mensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é:', valor_mensal)
        valor_prox_ano = irfaixa * 12
        var_red_ano = "{:.2f}".format(valor_prox_ano)
        print('o valor aproximado anual do tributo é', var_red_ano)
        return [faixa, renda_por_calculo, irfaixa, valor_prox_ano]

    if renda_por_calculo > 4250.01 and renda_por_calculo <= 5300.00:
        faixa = 3
        irfaixa = (renda_por_calculo / 100) * 22.5 - 636.13
        valor_mensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é:', valor_mensal)
        valor_prox_ano = irfaixa * 12
        var_red_ano = "{:.2f}".format(valor_prox_ano)
        print('o valor aproximado anual do tributo é', var_red_ano)
        return [faixa, renda_por_calculo, irfaixa, valor_prox_ano]

    if renda_por_calculo > 5300.01:
        faixa = 4
        irfaixa = (renda_por_calculo / 100) * 27.5 - 869.36
        valor_mensal = "{:.2f}".format(irfaixa)
        print('o valor mensal do tributo descontado em folha (em reais) é: ', valor_mensal)
        valor_prox_ano = irfaixa * 12
        var_red_ano = "{:.2f}".format(valor_prox_ano)
        print('o valor aproximado anual do tributo é', var_red_ano)
        return [faixa, renda_por_calculo, irfaixa, valor_prox_ano]


print('Insira abaixo o valor mensal referente ao ano de exercicio (2022)')


while True:

    renda_por_calculo: str = input("Valor mensal de renda: ")

    try:

        renda_por_calculo = float(renda_por_calculo)
        calculo_sem_desconto = calculo()
        break

    except:
        print('Favor inserir valor numérico')

print('O valor de referencia é o valor do tributo devido sem a adição de descontos.')

if calculo_sem_desconto[0] != 0:

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

        print('Após consultar e somar os valores para dedução, insira abaixo o valor total anual')
        print('em reais e separando as casas decimais(centavos) por ponto.')
        renda_por_calculo = input('Valor:')

        try:

            renda_por_calculo = float(renda_por_calculo) / 12
            renda_por_calculo = calculo_sem_desconto[1] - renda_por_calculo
            valor_com_descontos = calculo()
            tipo = 1

        except:
            print('Por favor, insira um valor numérico separando as casas decimais por ponto')

    valor_ano_sem_desc = float(calculo_sem_desconto[3])
    saldo_para_calculo = float(valor_com_descontos[3])

    if saldo_para_calculo > 0:
        valor_restituicao = abs(saldo_para_calculo - valor_ano_sem_desc)
        valor_restituicao = "{:.2f}".format(float(valor_restituicao))
        saldo_para_calculo = "{:.2f}".format(float(saldo_para_calculo))
        print('O valor final de implemento do tributo ficou no valor (em reais) de: ', saldo_para_calculo)
        print('A sua restituição de IR ficou no valor (em reais) de: ', valor_restituicao)

    else:
        valor_restituicao1 = "{:.2f}".format(calculo_sem_desconto[3])
        print('A sua restituição de IR ficou no valor (em reais) de:', valor_restituicao1)
        print('A situação de restituição do valor total do tributo, é equivalente')
        print('a isenção')

else:
    print('Como na primeira fase do cálculo, o valor inserido lhe coloca como isento,')
    print('não será necessário passar pela segunda fase do cálculo')
