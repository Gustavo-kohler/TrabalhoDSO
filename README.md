# TrabalhoDSO
UNIVERSIDADE FEDERAL DE SANTA CATARINA
INE5605 - Desenvolvimento de Sistemas Orientados a Objetos I
Lucas Nunes Bossle (23100751)
Gustavo Luiz Kohler (23102480)

PROBLEMA:
Desenvolver um sistema orientado a objetos de gestão de catálogo de filmes e cardápio da lanchonete de um cinema em Python.

ESCOPO DO DESENVOLVIMENTO E REGRAS DE NEGÓCIO:
O projeto serve de catálogo de filmes um cinema, onde é possível inserir, listar, remover e editar. E também serve de gestão de cardápio da lanchonete desse cinema, onde também é possível fazer um CRUD em relação aos alimentos disponibilizados aos clientes.

O usuário do produto é o funcionário de um cinema, que faz a gestão dos itens descritos.

Em relação a usabilidade:

Primeiro, o usuário irá receber uma mensagem de boas-vindas, e deverá selecionar se gostaria de gerir o catálogo de filmes, gerir o cardápio de alimentos ou listar relatórios.

Caso o catálogo seja escolhido, o usuário receberá uma nova lista de operações, contando:
Adicionar filme;
Listar filmes;
Remover filme;
Editar filme;
Gerenciar gêneros cinematográficos.

Então, basicamente, o filme é uma agregação de gêneros cinematográficos, sendo possível gerenciar os gêneros que estarão guardados na memória como objetos. Além disso, há as operações padrão para filmes como está descrito nas opções.

Agora, caso o cardápio seja escolhido, o usuário irá receber a seguinte lista de operações:
Adicionar alimento;
Listar alimento;
Remover alimento;
Editar alimento;

Então aqui constam as operações básicas para os alimentos do cardápio. Vale dizer que os alimentos podem receber “Adicionais”, que seriam temperos, acessórios, e outros, que dependem do alimento em questão. Um “Adicional” não existe sem o alimento no sistema, portanto, alimento é uma composição de adicionais.

Em relação ao escopo, há:
Cadastros: filmes e alimentos;
Registros: adicionais e gêneros;
Relatórios: manejo de catálogo e de cardápio.

SEPARAÇÃO DAS  IMPLEMENTAÇÕES:
Lucas Nunes Bossle: será o responsável por implementar todo o MVC relacionado a filme, assim como classes abstratas que servem para herança e controlador principal.

Gustavo Luiz Kohler: responsável por implementar os MVCs relacionados a alimento, cinema e relatório.

