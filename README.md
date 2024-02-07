# arquitetura-cmd
Ferramenta de linha de comando com utilitários diversos para os desenvolvedores da Nasajon.

## Modo de uso

1. Baixar o `.exe` "arquitetura-cmd.exe" mais recente, contido na página de [releases do projeto.](https://github.com/Nasajon/arquitetura-cmd/releases)
2. Executar o script em si (ver sessão do manual da linha de comando).

## Manual da linha de comando

Sintaxe básica de uso:

> ./dist/arquitetura-cmd.exe -c {COMANDO_DESEJADO} {PARAMETROS DO COMANDO}

**Obs.: De acordo com o comando escolhido, outros parâmetros podem ser necessários (inclusive podem ser obrigatórios). Donde se torna necessário consultar a documentação do comando desejado.**

## LOGs de execução

Cada execução do script criará o arquivo de log:

* ```arquitetura-cmd - {ano}-{mes}-{dia}-{hora}-{minuto}.log``` - Contendo o log do processo geral, inclusive erros de FK (esse log também é impresso no console da linha de comando).

## Comandos Disponíveis

### Geração do DTO no padrão RestLib

ID do comando (para o parâmetro ```-c```):

> rest_lib_dto

Este comando tem por objetivo gerar uma classe de DTO, a partir de um arquivo contendo um DDL da tabela para a qual se deseja o DTO no padrão RestLib.

**Obs.: Este comando se comunica com a API da OpenAI, e só funcionará caso você tenha a variável de ambiente "OPENAI_API_KEY" definida em seu sistema.**

#### Parâmetros adicionais

| Parâmetro | Obrigatório | Descrição                                                   |
| --------- | ----------- | ----------------------------------------------------------- |
| -f        | Sim         | Indica o path do arquivo contendo o DDL da tabela desejada. |

### Geração do Entity no padrão RestLib

ID do comando (para o parâmetro ```-c```):

> rest_lib_entity

Este comando tem por objetivo gerar uma classe de Entity, a partir de um arquivo contendo um DDL da tabela para a qual se deseja o DTO no padrão RestLib.

**Obs.: Este comando se comunica com a API da OpenAI, e só funcionará caso você tenha a variável de ambiente "OPENAI_API_KEY" definida em seu sistema.**

#### Parâmetros adicionais

| Parâmetro | Obrigatório | Descrição                                                   |
| --------- | ----------- | ----------------------------------------------------------- |
| -f        | Sim         | Indica o path do arquivo contendo o DDL da tabela desejada. |


## Empacotando para Disrtibuição

O comando pode ser empacotado em zip ou exe.

Caso se opte pelo zip, é necessário instalar o Python3.10 (ou maior, ainda dentro da versão 3) e todas as dependências no arquivo requirements.txt, no ambiente que for executado. Já o arquivo executável, pode ser rodado de modo por si só.

Os comandos para empacotar serão apresentados a seguir, mas ambos exportarão para o disretório `dist`:

### ZIP

> python empacotar.py

### Binário Windows (EXE)

> ./run-pyinstaller.bat

### Binário Linux ou Mac

> make pyinstaller