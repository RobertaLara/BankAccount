# Modelando a  solução

  Opções que precisam estar disponíveis para o usuário:
  
    - Consultar saldo
    - Sacar valor

  Informações que preciso saber:
  
    - Saldo do usuário
    - Valor que ele deseja sacar

  Como será feito o sistema:
  
    - Buscando ser o mais semelhante possível com um caixa eletrônico
    - Para isso o usuário poderá solicitar a operação que desejar até que ele finalize a operação
    - Ele poderá fazer quantas consultas e saques forem necessárias

  Variáveis:
  
    - O saldo será inicialmente fixo, mas será alterado a medida que os saques forem sendo realizados
    - O saque não poderá ser maior que o saldo disponível, negativo ou conter casas decimais (não trabalha com moedas)
    - A operção será informada pelo usuário de acordo com a instrução dada na tela e 
    - Não será aceito valores diferentes dos sugeridos
    - Ao final de cada operação, o usuário irá informar se deseja realizar mais alguma operação ou não


# Algorítmo

Perguntar ao usuário qual a operação desejada (1-Saldo, 2-Saque, 3-Finalizar operação)

Usuário digita valor correspondente à operação desejada

Se valor for diferente dos descritos, exibir mensagem de erro e solicitar que o usuário digite novamente até o valor estar de acordo

Se usuário desejar finalizar operação, exibir mensagem de agradecimento e encerrar programa. Se não, continuar verificando qual foi a opção

Se usuário desejar visualizar saldo, exibir valor do saldo na tela. Exibir em seguida opção para o usuário continuar a operação ou finalizar o processo

Se usuário desejar continuar a operação, retornar ao começo. Se não, exibir mensagem de agradecimento e encerrar programa

Se usuário desejar sacar, solicitar que ele digite o valor a ser sacado

Se o valor a ser sacado for maior que o saldo, negativo ou possuir casas decimais, retornar mensagem de erro e solicitar que o usuário digite novamente até o valor estar de acordo

Retornar na tela a confirmação do valor que foi sacado e subtrair esse valor no saldo do usuário. Exibir em seguida opção para o usuário continuar a operação ou finalizar o processo

Se usuário desejar continuar a operação, retornar ao começo. Se não, exibir mensagem de agradecimento e encerrar programa
