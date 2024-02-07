# exclusao_empresas

Comando capaz de realizar a deleção de empresas de um banco de dados, com alta performance.

## Atenção

Para alcançar melhor performance, foram tomadas medidas que impedem a utilização do script num banco de dados em produção, principalmente com usuários logados. O procedimento recomendado é:

* Realizar a exclusão das empresas num backup da base de produção, numa ambinte controlado e passível de homologação após a execução do script.
* Outra opção é utilizar o parâmetro ```-n```, para garantir que a execução se dará sobre uma base cópia da original.

Após se alcançar maior nível de confiança nesse script, ainda assim não se deve contar com o mesmo para apagar dados de um banco com outros usuários conectados, pois o script remove FKs, e até mesmo trunca tabelas (o que pode quebrar um BD, no caso de conexões simultâneas).

## Estratégia básica do script

1. Por meio de duas tabelas de controle ```exclusao.entidades``` e ```exclusao.entidades_dependencias```, o script constroi um grafo para descobrir a ordem de visita às tabelas (para levantar os dados a serem excluídos, por meio de uma busca em profundidade).
2. O script cria tabelas de buffer dos dados a excluir (uma tabela por schema do BD, com uma coluna ```table```, para identificar a tabela de origem), e, navegando pelas dependências entre as tabelas, seleciona todos os dados que devem ser excluídos do BD, para se remover uma determinada empresa (note que o script é senssível ao modo de instalação, só apagando dados na tabela ns.pessoas, em caso de instalação em modo contábil, por exemplo).
3. O script navega pelas entidades (contidas na tabela ```exclusoa.entidades```), e apaga os dados de acordo com os buffers, por meio dos seguintes passos:
    1. Desliga as triggers
    1. Remove as FKs de cada tabela
    3. Apaga os dados, e, de acordo com a quantidade de linhas a pagar:
        1. Se forem poucos dados: Faz delete direto.
        2. Se forem muitos dados: Cria uma tabela temporária com os dados a manter, faz truncate na tabela origina, e restaura os dados a manter

**Assim, o script tem escopo de deleção limitado às tabelas contidas nas tabelas de controle (tabelas novas, se precisarem de deleção, precisão ser excluídas nas tabelas de controle, se não, serão ignoradas, e podem gerar erros futuros de FKs, nesse script). Essa mesma característica evita comportamentos imprevistos do script.**

## Parâmetros adicionais para a linha de comando

* **-e:** Lista de códigos das empresas a serem excluídas, separados por vírgula (```,```). Obs.: Se for necessário passar um código que contenha um caracter de espaçamento, é preciso envolver toda a lista de códigos das empresas, com aspas duplas (exemplo: ```"CODIGO1,CODIGO EMPRESA 2,CODIGO3"```).
* **-s:** Etapa do processo de exclusão a ser executada. Valor padrão: `processo_basico`.

**Vale destacar que o valor padrão do parâmetro `-s`, assume que o processo básico de exclusão será executado (ver sobre etapas a seguir).**

### Sobre as etapas de execução

O script foi preparado para realidades distintas, e para permitir melhorias incrementais no próprio código.

Portanto, a lógica de execução do mesmo consiste na execução de um ```processo_basico```, ou na execução de um passo por vez, de acordo com o uso do parâmetro step (-s).

O ```processeo_basico``` (que também é o modo padrão de execução), implica, na prática, na execução dos seguintes passos em sequência: ```'melhorias_modelagem', 'criacao_buffer', 'selecao_dados', 'ajuste_buffer', 'exclusao', 'apaga_buffer_temp'```

Mas, o usuário sempre pode invocar a execução de um único passo de modo isolado (por meio do parâmetro -s).

Assim, segue o significado de cada etapa suportada:

* **processo_basico:** Padrão do script, que implica na execução sequencial do "caminho feliz" (conforme já explicado acima).
* **melhorias_modelagem:** Aplica melhorias e ajustes na modelagem original do BD, para dar suporte a exclusão. Também cria a estrutura básica de controle do processo (schema exclusao, e tabelas: entidades e entidades_dependencias).
* **auto_dependencias:** Popula a tabela exclusao.entidades_dependencias com as FKs que estiverem faltando (retiradas da modelagem do BD).
* **criacao_buffer:** Cria as tabelas primárias de buffer para a exclusão, onde as etapas de seleção dos dados irão armazenar os IDs dos dados a excluir (porém ainda sem garantir a unicidade).
* **selecao_dados:** Navega pelas dependências entre os dados, populando as tabelas de buffer, e preparando assim para a exclusãi de fato.
* **selecao_dados_incremental:** Navega pelas dependências entre os dados, populando as tabelas de buffer, e preparando assim para a exclusãi de fato. No entanto, esta estapa só deve ser usada no meio de um processo já iniciado anteriormente, porque faz um join a mais, para evitar inserções desnecessárias (o que torna tudo mais lento, para um processo desde o zero).
* **exclusao:** Etapa que promove de fato a exclusão dos dados, utilizando as tabelas de buffer secundárias (com unicidade dos dados), como controle das exclusões (por meio da coluna booleana excluido).
* **ajuste_buffer:** Responsavel por criar ou atualizar as tabelas "2" do buffer de exclusão, as quais são as que de fato a etapa de exclusão usa, e onde se garante a unicidade das chaves a excluir.
* **apaga_buffer_temp:** Apaga as tabelas de buffer primárias da exclusão (onde não é garantida a unicidade).
* **permissoes_nasajon:** Aplica permissões para o group_nasajon, para a estrutura que permanecerá no BD, após o processo de exclusão.
* **popula_pks:** Popula as PKs faltantes na tabela de controle exclusao.entidades.

**Destaque: O passo ```permissoes_nasajon``` pode ser útil caso se use o script numa base local que pode sofre backup via NsjAdmin no futuro (pois ela dá as permissões necessárias, nas novas estruturas de BD, para que o backup não falhe).**

## Possíveis erros

Como já dito, esse script foi criado em caráter evolutivo, e cauteloso, de modo que não exclui tabelas que não estejam em sua estrutura de controle.

Assim, possivelmente, o script pode acabar por não conseguir recriar todas as FKs removidas, ao final do processo, e isso precisa ser notificado a um programador (de preferência do setor responsável pela tabela faltante, por exemplo, se houver um erro na tabela persona.trabalhadores deve-se convocar a equipe do persona), para que o mesmo evolua o script.

No entanto, o modo mais rápido de se recuperar após um erro, é remover manualmente os dados que faltaram ser excluídos, e recriar, manualmente, a FK que ficou pendente (e que foi notificada no LOG).

### Exemplo de tratamento de erro

Erro:
> 2022-04-24 02:04:24,140 - exclusao_empresas - INFO - (pg8000.dbapi.ProgrammingError) {'S': 'ERROR', 'V': 'ERROR', 'C': '23503', 'M': 'insert or update on table "processoscodigosterceiros" violates foreign key constraint "FK_persona.processoscodigosterceiros_processo"', 'D': 'Key (processo)=(f9ac4b76-e4fb-4c28-a33b-2ab4024f05df) is not present in table "processos".', 's': 'persona', 't': 'processoscodigosterceiros', 'n': 'FK_persona.processoscodigosterceiros_processo', 'F': 'd:\\pginstaller.auto\\postgres.windows-x64\\src\\backend\\utils\\adt\\ri_triggers.c', 'L': '2783', 'R': 'ri_ReportViolation'}
[SQL: ALTER TABLE persona."processoscodigosterceiros" ADD CONSTRAINT "FK_persona.processoscodigosterceiros_processo" FOREIGN KEY (processo) REFERENCES persona.processos(processo) DEFERRABLE;]
(Background on this error at: https://sqlalche.me/e/14/f405)

Passos de recuperação:

1. Apagar dados faltantes (note que o comando de criação da FK que deu erro, contém todos os dados necessários para construir um SQL similar ao do exemplo abaixo):

> delete from persona."processoscodigosterceiros" as t1 where not exists (select 1 from persona.processos as t2 where t1.processo=t2.processo);

2. Recriar a FK na mão (copiando o comando do próprio erro):

> ALTER TABLE persona."processoscodigosterceiros" ADD CONSTRAINT "FK_persona.processoscodigosterceiros_processo" FOREIGN KEY (processo) REFERENCES persona.processos(processo) DEFERRABLE;

**Obs. 1: Não deixe de notificar o erro ao desenvolvimento, para que o script seja melhorado, e não incorra mais no mesmo erro.**

**Obs. 2: Por mais manual que seja, esse é o caminho mais rápido de recuperação do erro, pois não exige mais buscas pelos relacionammentos entre as entidades sendo excluídas no BD (e, embora seja possível usar o script de modo incremental, a performance da busca não justifica essa opção).**

### Observações para o pessoal do desenvolvimento

O próprio script está preparado para esse processo adaptativo (por meio dos passos adicionais), não se perdendo todo o trabalho de deleção realizado até o momento do erro de FK.

Em geral, os passos pós erro de FK serão:

1. Analisar os erros de FK (para identificar se é o caso de entidades faltando na tabela ```exclusao.entidades```).
2. Adicionar as tabelas faltantes (atentar na qeustão do modo de instalação).
3. Rodar o passo "popula_pks".
4. Rodar o passo "auto_dependencias"
5. Adicionar, manualmente, o FKs que gerou o erro, na tabela exclusao~entidades_dependencias
6. Rodar o passo "selecao_dados_incremental",
7. Rodar o passo "ajuste_buffer"
8. Rodar o passo "exclusao"

Se ainda houver erros de FK, pode-se rodar repetidamente os passos acima. Se não:

1. Rodar o passo "apaga_buffer_temp"
2. Recriar, manualmente, todas as FKs que geraram erros.

## LOGs de execução

Cada execução do script criará dois arquivos de log:

* ```exclusao - {ano}-{mes}-{dia}-{hora}-{minuto}.log``` - Contendo o log do processo de exclusão em si, inclusive os erros de FK, ou qualquer outro erro (esse log também é impresso no console da linha de comando).
* ```fks - {ano}-{mes}-{dia}-{hora}-{minuto}.log``` - Contendo um buffer com todas as FKs tratadas pelo script (recriadas ou não), para se ter certeza de que todas as FKs podem ser posteriormente recriadas (mesmo que manualmente).