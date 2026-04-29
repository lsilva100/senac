Algoritmo "senha"




Var
   senha: caractere
   tentativas: inteiro


Inicio


      tentativas <- 0
      enquanto tentativas < 3 faca
      escreva ("Digite a senha: ")
      leia (senha)
      
      se senha = "1234" entao
      escreval ("Acesso permitido")
      interrompa
      
      senao
      escreva ("Senha incortreta, ")
      tentativas <- tentativas +1
      fimse
      fimenquanto
      
      se tentativa = 3 entao
      escreval ("Acesso Bloqueado")
      fimse


Fimalgoritmo