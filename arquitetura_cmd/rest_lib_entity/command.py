import argparse
import openai
import requests
import time

from typing import List

from arquitetura_cmd.command import Command


class RestLibEntityCommand(Command):

    def main(self, pars: List[str]):
        start_time = time.time()
        try:
            # Parsing command line arguments
            parser = argparse.ArgumentParser(
                description="""Utilitário para geração de DTO, no padrão RestLib, a partir de um arquivo com DDL de uma tabela."""
            )

            parser.add_argument(
                "-f",
                "--file",
                help="Arquivo contendo o DDL da tabela alvo.",
                required=False,
                default="",
            )

            args, _ = parser.parse_known_args(pars)
            file_path = args.file

            # Lendo o DDL
            with open(file_path, "r") as f:
                ddl_content = f.read()

            # Lendo a entrada de exemplos a serem enviados ao ChatGPT
            URL_EXEMPLOS = "https://github.com/Nasajon/arquitetura-cmd/arquitetura_cmd/rest_lib_entity/exemplos_para_chatgpt.txt"
            resp = requests.get(URL_EXEMPLOS, timeout=5)
            resp.raise_for_status()
            exemplos = resp.text

            # Chamando a API da OpenAI
            messages = [
                {
                    "role": "system",
                    "content": "Ao gerar um DTO, nunca oculte campos que existam na tabela de origem.",
                },
                {
                    "role": "system",
                    "content": exemplos,
                },
            ]
            functions = []

            pergunta = f"""
Gere uma Entity para a tabela abaixo:

#####
{ddl_content}
#####
        """

            pergunta = {
                "role": "user",
                "content": pergunta,
            }
            messages.append(pergunta)

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                temperature=0.8,
            )
            response_message = response["choices"][0]["message"]

            messages.append(response_message)
            print(response_message["content"])
        finally:
            self.log(
                "--- TEMPO TOTAL GERAL %s seconds ---" % (time.time() - start_time)
            )
