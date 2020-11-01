L-System - Lucas Russo

Sistema com angulo fixo de 90°, sendo "F" a variável de desenho e os sinais "+ -" utilizados para virar, 90° para direita e 90° para esquerda, respectivamente. Outros caracteres, após a execução das regras, são ignorados.

O programa cria um arquivo "HTML" com uma estrutura SVG interna, com tamanho fixo de 15000 pixels², sendo que o mesmo lê um arquivo chamado "gramatica.txt" onde possui as regras, o axiom e a posição inicial das coordenadas(X, Y). Onde podem ser alteradas conforme desejar.


Bom divertimento.


- Regra inicial
  variáveis: F
  constantes: + -
  axiom: FX
  rules: (X → X+YF+)
  rules: (Y → -FX-Y)
  angulo: 90° (Fixo)
