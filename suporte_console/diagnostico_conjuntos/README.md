# Diagnóstico de Conjuntos

Comando capaz de:

* Tentar criar uniques na estrutura de conjuntos, para evitar futuros problemas de conjuntos numa base de dados.
* Identificar problemas já existentes, numa base de dados (por hora, por não conseguir criar as tais uniques).
* Aplicar diversos patches de correção, tentando restaurar os problemas identificados.

Assim, esse comando tem duplo objetivo, corrigindo uma base, e bucando evitar novos problemas no futuro.

Obs. 1: O diagnóstico é automático, e devem ser observados os patches (ver abaixo) que o mesmo é capaz de aplicar.

Obs. 2: O diagnóstico aplica os patches na mesma ordem apresentada na documentação, e portanto deve analisar se a ordem é satisfatória para o BD em questão.

## Criação de Uniques

As uniques são criadas nas tabelas:

* **ns.estabelecimentosconjuntos:** Serve para garantir que um estabelecimento vê apenas um conjunto de cada tipo.
* **ns.conjuntos<REGISTRO>:** Serve para garantir que um registro esteja associado a apenas um conjunto de seu tipo.

## Patches de Correção Disponíveis

* **recriar_estrutura:** Patch preferencial, pois recria toda a estrutura de conjuntos (resolvendo "qualquer" inconsistência). Mas, só é aplicável quando a base contém apenas um grupo empresarial, e se encontra em modo empresa.
* **estabelecimento:** Resolve o caso quando um estabelecimento está associado, mais de uma vez, a um mesmo conjunto.
* **replicacoes_simples_registros:** Resolve o caso quando um registro (de qualquer tipo) está associado mais de uma vez a um determinado conjunto (causando falsa duplicação do registro no respetivo browser).
* **conjuntos_clientes_fornecedores_compartilhados:** Resolve o caso de quando um conjunto de cliente ou fornecedor estiver compartilhado por mais de uma empresa ou grupo empresarial (de acordo com o modo de instalação da base). A estratégia de correção consiste em copiar os dados para os grupos ou empresas que tinham acesso (mantendo o original no grupo ou empresa com maior uso do dado). A ideia é que o usuário já via o dado replicado, e portanto, pouco ou não notará a cópia.
* **clientes_fornecedores_compartilhados:** Resolve o caso de quando um dado de cliente ou fornecedor estiver compartilhado por mais de um conjunto. A estratégia de correção consiste em copiar os dados para conjuntos que tinham acesso (mantendo o original no conjunto que apresentava maior uso do dado). A ideia é que o usuário já via o dado replicado, e portanto, pouco ou não notará a cópia.
  * Note que esse patch é semelhante ao anterior, mas ele trata dados compartilhados entre conjuntos, e não conjuntos inteiros compartilhados.
