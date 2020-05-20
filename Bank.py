# Consulta ao saldo na conta corrente e liberação do valor somente se for dentro do valor disponível na conta
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

print("\n\n\tBANCO 24 HORAS - Não aceite ajuda de estranhos\n")

auxiliar = 0            # Declarei um auxiliar para encerrar o while quando o usuário desejar encerrar a operação
saldo = 500.00          # Saldo do usuário é inicialmente fixo

while (auxiliar == 0):          # Somente vai sair do while quando o auxiliar for diferente de 0
    
    operacao = input("\nQual a operação desejada?\n\n"      # Instrução para o usuário digitar qual operação ele deseja
        "Para consultar saldo, digite 1\n"
        "Para saque, digite 2\n"
        "Para finalizar a operação, digite 3\n")
    
    while (operacao != '1') and (operacao != '2') and (operacao != '3'):    # Caso usuário digite um número diferente
        operacao = input("   OPÇÃO INVÁLIDA! DIGITE OPERAÇÃO NOVAMENTE.\n")
    
    clear()

    if (operacao == '3'):       # Caso usuário solicite finalizar a operação, uma mensagem é exibida e o progama é encerrado
        print("\n\n\tOBRIGADO POR USAR O BANCO 24 HORAS!\n\n")
        auxiliar = 1            # Alteração do valor do auxiliar para encerrar o while macro
    
    if (operacao == '1'):       # Caso o usuário solicite ver o saldo, o mesmo será exibido na tela
        print("\n\n\tSALDO DISPONÍVEL PARA SAQUE: ",round(float(saldo),2),"\n\n")
    elif (operacao == '2'):     # Caso usuário solicite sacar valor
        valorSaque = input("\n\nDigite valor que deseja sacar: ")   # Instrução para o usuário digitar valor do saque
        while (float(valorSaque) > saldo) or (float(valorSaque) < 0 or (int(float(valorSaque)) != float(valorSaque))):
            # Valor do saque não pode ser maior que o saldo, negativo ou conter casas decimais (não trabalhamos com moedas)
            valorSaque = input("\n\tSALDO INSUFICIENTE OU VALOR INVÁLIDO! DIGITE OUTRO VALOR.\n\n")
        clear()
        print("\n\n\tVALOR SACADO: ",round(float(valorSaque),2),"\n\n")     # Informa valor sacado
        saldo = saldo - float(valorSaque)                   # Subtrai o valor sacado do saldo, gerando um saldo atualizado
    
    if (auxiliar == 0):
        simNao = input("Dejesa fazer mais alguma operação?\n\n"     # Opção do usuário continuar com outra operação ou não
            "Sim, digite 1\n"           # Se usuário quiser continuar, todo o processo é repetido
            "Não, digite qualquer outro valor\n")
        if (simNao != '1'):        # Caso ele não queira continuar, uma mensagem é exibida e o progama é encerrado
            clear()
            print("\n\n\tOBRIGADO POR USAR O BANCO 24 HORAS!\n\n")
            auxiliar = 1    # Alteração do valor do auxiliar para encerrar o while macro
