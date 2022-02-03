# Lista 2 de I.A (IC-UFAL)

## Formato do input

Para o conjunto de regras, as seguintes condições precisam ser atendidas:

- Inicialmente deve ser informado a quantidade de regras
- Uma regra por linha
- Uma regra deve iniciar pela palavra reservada "se" seguido de uma ou mais condições
- Cada condição tem a forma: "X = Y", sendo X e Y palavras representando chave e valor respectivamente
- As condições devem ser concatenadas utilizando a palavra reservada "e"
- Por último deve vir a palavra reservada "entao" seguido de uma expressão da forma: "X = Y", sendo X e Y palavras representando chave e valor respectivamente
- Cada palavra deve estar separada por espaços
- Uma palavra não deve conter espaços
- Nenhuma chave ou valor deve ser igual a "?", "e" ou "entao" por serem palavras reservadas
- As regras são indexadas a partir do 0 de acordo com o número da linha em que ela está

Para o conjunto de fatos iniciais, as seguintes condições precisam ser atendidas:

- Inicialmente deve ser informado a quantidade de fatos
- Um fato por linha
- Um fato tem a forma: "X = Y", sendo X e Y palavras representando chave e valor respectivamente
- Nenhuma chave ou valor deve ser igual a "?", "e" ou "entao" por serem palavras reservadas

Para o conjunto de hipóteses (objetivos), as seguintes condições precisam ser atendidas:

- Inicialmente deve ser informado a quantidade de hipóteses
- Uma hipótese por linha
- Uma hipótese tem a forma: "X = Y", sendo X e Y palavras representando chave e valor respectivamente
- Nenhuma chave ou valor deve ser igual a "?", "e" ou "entao" por serem palavras reservadas

Caso o conjunto de fatos iniciais não seja suficiente para chegar em uma conclusão sobre uma das hipóteses, poderão ser feitas novas perguntas ao usuário.
