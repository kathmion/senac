programa {
  funcao inicio() {
    //variveis
    real n1, n2, media
    //ler da tela as duas notas
    escreva("Digite a nota da prova: ")
    leia(n1)
    escreva("Digite a nota do trabalho: ")
    leia(n2)
    //calculo da média 
    media = (n1 + n2)/2
    escreva("Media é",media)
    //comando condicioal 
    se (media >=6){
    escreva("\nAprovado - PD")
    }senao{
      escreva("\nReprovado - ND")
    }
    
  }
}
