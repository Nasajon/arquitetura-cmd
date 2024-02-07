import argparse
import datetime
import logging
import sys
import time
import shlex

from typing import List

# from arquitetura_cmd.database_config import create_pool
# from arquitetura_cmd.db_adapter2 import DBAdapter2

from arquitetura_cmd.rest_lib_dto.command import RestLibDTOCommand
from arquitetura_cmd.rest_lib_entity.command import RestLibEntityCommand

COMMANDS = {
    "rest_lib_dto": RestLibDTOCommand,
    "rest_lib_entity": RestLibEntityCommand,
}


def config_logger():
    # Configuring logger
    data = datetime.datetime.now()
    log_file_name = f"arquitetura_cmd - {data.year}-{data.month}-{data.day}-{data.hour}-{data.minute}.log"

    logger = logging.getLogger("arquitetura_cmd")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(log_file_name)

    console_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


def internal_main(
    pars: List[str],
    # database_name: str,
    # database_user: str,
    # database_pass: str,
    # database_host: str,
    # database_port: str,
    command: str,
    # database_default_name: str,
):
    logger = logging.getLogger("suporte_console")
    logger.info("Abrindo conexão com o banco de dados...")

    start_time = time.time()
    try:
        # Criando o pool de conexoes
        # pool = create_pool(
        #     database_user, database_pass, database_host, database_port, database_name, 1
        # )

        # # Abrindo conexao com o BD
        # with pool.connect() as conn:
        #     # Instanciando o DBAdapter
        #     db_adapter = DBAdapter2(conn)

        # Resolvendo os passos a executar
        commands_list = [k for k in COMMANDS]
        if not (command in commands_list):
            logger.warning(
                f"Parâmetro command inválido {command}. Use: {commands_list}"
            )
            sys.exit(4)

        # Executando o comando
        # command_obj = COMMANDS[command](db_adapter, command)
        command_obj = COMMANDS[command](command)
        command_obj.main(pars)

    finally:
        logger.info("--- TEMPO TOTAL GERAL %s seconds ---" % (time.time() - start_time))


def main():
    interative_mode = False
    try:
        # Configuring logger
        config_logger()
        logger = logging.getLogger("arquitetura_cmd")

        # Initialize parser
        parser = argparse.ArgumentParser(
            description="""Ferramenta de linha de comando com utilitários diversos para os desenvolvedores da Nasajon."""
        )

        # Adding arguments
        # parser.add_argument(
        #     "-d",
        #     "--database",
        #     help="Nome do banco de dados para conexão",
        #     required=True,
        # )
        # parser.add_argument(
        #     "-n",
        #     "--new_database",
        #     help="Nome do banco de dados criado pelo procedimento",
        #     required=False,
        # )
        # parser.add_argument(
        #     "-f",
        #     "--database_default_name",
        #     help="Nome do banco de dados default para conexão, ao criar uma cópia do BD a ser tratado.",
        #     required=False,
        #     default="postgres",
        # )
        # parser.add_argument(
        #     "-u",
        #     "--user",
        #     help="Usuário para conexão com o banco de dados",
        #     required=False,
        #     default="postgres",
        # )
        # parser.add_argument(
        #     "-p",
        #     "--password",
        #     help="Senha para conexão com o banco de dados",
        #     required=False,
        #     default="postgres",
        # )
        # parser.add_argument(
        #     "-t",
        #     "--host",
        #     help="IP ou nome do servidor do banco de dados",
        #     required=False,
        #     default="localhost",
        # )
        # parser.add_argument(
        #     "-o",
        #     "--port",
        #     help="Porta para conexão com o banco de dados",
        #     required=False,
        #     default="5432",
        # )

        parser.add_argument(
            "-c", "--command", help="Comando a ser executado.", required=True
        )

        # Check if is interative mode
        interative_mode = is_interative_mode()

        # Read arguments from command line or console
        cli_pars = sys.argv[1:]
        if interative_mode:
            aguarda_args = True
            exit = False
            while aguarda_args:
                try:
                    user_input = input(
                        "Adicione os parâmetros desejados para a execução do SuporteConsole\n"
                    )
                    user_input = user_input.replace("\r", "")
                    user_input = user_input.replace("\n", "")

                    if user_input.lower() in ["q", "quit", "exit"]:
                        exit = True
                        break
                    else:
                        pars = cli_pars + shlex.split(user_input)

                        # Interpreting args
                        args, _ = parser.parse_known_args(pars)

                        aguarda_args = False
                except:
                    pass

            if exit:
                sys.exit(-1)
        else:
            # Interpreting args
            pars = cli_pars
            args, _ = parser.parse_known_args(pars)

        # Calling internal main
        internal_main(
            pars,
            # args.database,
            # args.user,
            # args.password,
            # args.host,
            # args.port,
            args.command,
            # args.database_default_name,
            # args.new_database,
        )

        if interative_mode:
            input("Enter para terminar")

        sys.exit(0)
    except Exception as e:
        logger.exception(f"Erro fatal. Mensagem original do erro {e}")
        if interative_mode:
            input("Enter para terminar")
        sys.exit(5)


def is_interative_mode() -> bool:
    # Initialize parser
    parser = argparse.ArgumentParser(description="")

    # Adding arguments
    parser.add_argument(
        "-v",
        "--interative",
        help="Inidica se o comando deve ser executado de modo iterativo (com entradas do usuário após execução).",
        required=False,
        action="store_true",
    )

    # Read arguments from command line
    args, _ = parser.parse_known_args()

    return args.interative


if __name__ == "__main__":
    main()
