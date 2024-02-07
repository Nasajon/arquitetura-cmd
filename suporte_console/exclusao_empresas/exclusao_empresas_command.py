import argparse
import datetime
import logging
import sys
import time

from typing import List

from suporte_console.command import Command

from suporte_console.exclusao_empresas.ajuste_buffer_step import AjusteBufferStep
from suporte_console.exclusao_empresas.apaga_buffer_temp_step import ApagaBufferTempStep
from suporte_console.exclusao_empresas.auto_dependencias_step import AutoDependenciasStep
from suporte_console.exclusao_empresas.criacao_buffer_step import CriacaoBufferStep
from suporte_console.exclusao_empresas.exclusao_step import ExclusaoStep
from suporte_console.exclusao_empresas.melhorias_modelagem_step import MelhoriasModelagemStep
from suporte_console.exclusao_empresas.permissoes_nasajon_step import PermissoesNasajonStep
from suporte_console.exclusao_empresas.popula_pks_step import PopularPKsStep
from suporte_console.exclusao_empresas.selecao_dados_step import SelecaoDadosStep
from suporte_console.exclusao_empresas.selecao_dados_incremental_step import SelecaoDadosIncrementalStep


STEPS = {
    'exclusao': ExclusaoStep,
    'criacao_buffer': CriacaoBufferStep,
    'auto_dependencias': AutoDependenciasStep,
    'selecao_dados': SelecaoDadosStep,
    'selecao_dados_incremental': SelecaoDadosIncrementalStep,
    'ajuste_buffer': AjusteBufferStep,
    'melhorias_modelagem': MelhoriasModelagemStep,
    'apaga_buffer_temp': ApagaBufferTempStep,
    'permissoes_nasajon': PermissoesNasajonStep,
    'popula_pks': PopularPKsStep
}

LISTA_STEPS = [STEPS[k] for k in STEPS]
LISTA_STEPS.append('processo_basico')

STEPS_PROCESSO_BASICO = ['melhorias_modelagem', 'criacao_buffer',
                         'selecao_dados', 'ajuste_buffer', 'exclusao',
                         'apaga_buffer_temp']


class ExclusaoEmpresasCommand(Command):

    def config_logger_fks(self):
        # Configuring logger
        data = datetime.datetime.now()
        log_file_name = f"fks - {data.year}-{data.month}-{data.day}-{data.hour}-{data.minute}.log"

        logger = logging.getLogger('log_fks')
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_file_name)

        file_format = logging.Formatter('%(message)s')
        file_handler.setFormatter(file_format)

        logger.addHandler(file_handler)

    def main(self, pars: List[str]):
        self.config_logger_fks()

        logger = logging.getLogger(self.command_id)

        start_time = time.time()
        try:
            # Parsing command line arguments
            parser = argparse.ArgumentParser(
                description="""Utilitário para exclusão de empresas de um banco de dados.""")

            parser.add_argument(
                "-e", "--empresas", help="Lista dos códigos das empresas a excluir (separados por vírgulas)", required=False, default='')

            parser.add_argument(
                "-s",
                "--step",
                help=f"Etapa do processo de exclusão a ser executada. Válidos: {LISTA_STEPS}.",
                required=False,
                default='processo_basico'
            )

            parser.add_argument(
                "-i",
                "--invert",
                help=f"Permite inverter a seleção de empresas (a lista de empresas será entendida como as empresas a manter no BD, e não as empesas a excluir).",
                required=False,
                action='store_true'
            )

            args, _ = parser.parse_known_args(pars)
            step_id = args.step
            empresas = args.empresas
            invert_selecao = args.invert

            # Resolvendo os passos a executar
            steps = [step_id]
            if not(step_id in LISTA_STEPS):
                logger.warning(
                    f"Parâmetro step inválido {step_id}. Use: {LISTA_STEPS}")
                sys.exit(4)
            if step_id == 'processo_basico':
                steps = STEPS_PROCESSO_BASICO

            # Executando cada step
            for id in steps:
                step_obj = STEPS[id](self.db_adapter)
                step_obj.main(empresas, invert_selecao)

        finally:
            self.log("--- TEMPO TOTAL GERAL %s seconds ---" %
                     (time.time() - start_time))
