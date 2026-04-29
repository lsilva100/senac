Algoritmo "energia"

Var

consumo, geracao, tarifa, taxaFixa: real
consumoLiquido, valorFinal: real
bandeira: caractere
adicionalBandeira, adicionalTotal: real
blocos: real

//consumo = energia consumida pela casa
//geração = energia gerada pelos paineis solares
//tarifa = preço de cada kWh
//taxa fia = valor fixo da conta
//consumoLiq = consumo depois de descontar a geração solar
//valorFinal = total que será pago
//adicionalBandeira =  valor da bandeira a cada 100kWh
//adicionalTotal = total cobrado pela bandeira
//blocos = quantidade de blocos a cada 100kWh
Inicio


//ler a energia consumida pela casa
escreva("Digite o consumo mensal em kWh: ")
leia(consumo)

//ler o consumo da geração solar
escreva("Digite a geração solar mensal em kWh: ")
leia(geracao)

//ler tarifa mensal da energia
escreva("Digite a tarifa da energia em R$/kWh: ")
leia(tarifa)

 //ler a tarifa de iluminação publica
escreva("Digite a taxa fixa de iluminação pública: ")
leia(taxaFixa)

//ler a bandeira do cliente
escreva("Digite a bandeira (V=Verde, A=Amarela, P1=Patamar, P2=Patamar): ")
leia(bandeira)


//aqui vamos definir um valor por bloco 100kWh
se bandeira = "V" ou bandeira = "v" entao
   adicionalBandeira <- 0 //Não haverá cobrança
   
se bandeira = "A" ou bandeira = "a" entao
   adicionalBandeira <- 1.8885 //Cobrança de 1,8885 reais adicionais a cada 100kWh
   
se bandeira = "P1" ou bandeira = "p1" entao
   adicionalBandeira <- 4.463  //Cobrança de 4,463 reais adicionais a cada 100kWh
   
se bandeira = "P2" ou bandeira = "p2" entao
   adicionalBandeira <- 7.877 //Cobrança de 7,877 reais adicionais a cada 100kWh
   
   senao
   //se o usuário digitar a bandeira errada, considera o verde
   escreval("Bandeira Inválida! Considerando verde.")
   adicionalBandeira <- 0
   fimse
   fimse
   fimse
   fimse


//calcula o desconto da energia
consumoLiquido <- consumo - geracao


//nesse bloco estamos declarando se o consumoLiq for negativo, só paga a taxa
//fixa, se for positivo paga o consumo com a conta abaixo.
se (consumoLiquido <= 0) entao
   valorFinal <- taxaFixa
senao
     //calculando quantos blocos de 100kWh existem na conta informada caso
     // ainda haja consumo para pagar
     bloco <- int(consumoLiquido / 100)
     adicionalTotal <- blocos * adicionalBandeira

                  //   energia consumida     + bandeira       + taxa fixa
     valorFinal <- (consumoLiquido * tarifa) + adicionalTotal + taxaFixa


                              //declaro 2 casa depois da virgula
escreval("Consumo liquido: ", consumoLiquido:0:2, " kWh")
Escreval("Valor final da conta: R$ ", valorFinal:0:2)



Fimalgoritmo