# Scout-Futsal

## Projeto criado durante a disciplina de Projeto Interdisciplinar para Sistemas de Informação - UFRPE

### O Scout Futsal foi escrito em Python, com dados de atleta, treino e usuário sendo salvos em arquivo txt. A ferramenta possibilita salvar dados de atleta, de treino e do proprio usuário (treinadores de futsal) em cadastro de usuário. Além de indicar quais os melhores atletas nas posições de Pivô, Fixo e Ala, a ferramenta também sugere duas opções de equipes: uma equipe ofensiva (com os melhores jogadores no quesito Cobertura Ofensiva) e uma equipe defensiva (com os melhores jogadores no quesito Cobertura Defensiva).
### As bibliotecas importadas foram: Os e sleep (da biblioteca time) apenas para limpeza do terminal; e ast (para usar a função literal.eval()) a fim de converter string em dicionário no decorrer do código.

### Funcionalidades entregues: 
### Login - Pede o cpf como entrada (caso o usuário ainda não possua cadastro, traz a opção de realizar o cadastro) e em seguida, a senha.
### Menu - Uma vez logado, o usuário pode escolher as opções contantes neste menu (todas as funcionalidades a seguir além da opção 'sair', caso queira sair do programa)
### Registrar Atleta - Permite que o usuário cadastre informações (número da camisa, nome, idade e posição) de cada atleta.
### Remover Atleta - Permite que o usuário veja a lista de atletas cadastrados e em seguida, através do numero da camisa, remova o atleta de sua base de registros.
### Registrar Treino - Permite que o usuário cadastre informações de treino para cada atleta. As informações incluem: id, nome, data do treino, cobertura ofensiva, cobertura defensiva, penetração, impulsão, mobilidade, qualidade de passe, qualidade de recepção, finalizações e gols marcados.
### Remover Treino - Permite que o usuário remova os registros, de acordo com o id, de cada atleta.
### Previsão por Atleta - Compara os valores dos atribustos especificos de cada posição de todos os atletas, em seguida imprime o nome dos atletas com maior média em cada posição (pivô, fixo e ala).
### Montagem de Equipe - Sugere, com base nos valores dos atributos Cobertura Defensiva e Cobertura Ofensiva, duas equipes com 5 atletas cada, cujas médias são as melhores dentre todos os atletas registrados.

#### Funcionalidades para 1VA: Login, Registrar Atleta e Registrar Treino
#### Funcionalidades para 3VA: Remover Treino, Previsão por Atleta e Montagem de Equipe
#### Ponto Extra: Remover Atleta



