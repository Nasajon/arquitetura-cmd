import logging
import time

from typing import List

from suporte_console.command import Command
from suporte_console.diagnostico_conjuntos.handler_uniques import HandlerUniques
from suporte_console.diagnostico_conjuntos.patch_recriar_estrutura_conjuntos import PatchRecriarEstruturaConjuntos
from suporte_console.diagnostico_conjuntos.patch_replicacoes_simples_estabelecimentos_conjuntos import PatchReplicacoesSimplesEstabelecimentosConjuntos
from suporte_console.diagnostico_conjuntos.patch_replicacoes_simples_registros import PatchReplicacoesSimplesRegistros
from suporte_console.diagnostico_conjuntos.patch_clientes_fornecedores_compartilhados import PatchClientesFornecedoresCompartilhados
from suporte_console.diagnostico_conjuntos.patch_conjuntos_clientes_fornecedores_compartilhados import PatchConjuntosClientesFornecedoresCompartilhados
from suporte_console.diagnostico_conjuntos.registros import REGISTROS

PATCHES = {
    'estabelecimento': PatchReplicacoesSimplesEstabelecimentosConjuntos,
    'replicacoes_simples_registros': PatchReplicacoesSimplesRegistros,
    'conjuntos_clientes_fornecedores_compartilhados': PatchConjuntosClientesFornecedoresCompartilhados,
    'clientes_fornecedores_compartilhados': PatchClientesFornecedoresCompartilhados
}


class DiagnosticoConjuntosCommand(Command):

    def main(self, pars: List[str]):

        start_time = time.time()
        try:
            self.log('Iniciando o diagnóstico de conjuntos')

            # Getting logger
            logger = logging.getLogger(self.command_id)

            #####################################################
            # TENTANDO CRIAR TODAS AS UNIQUES
            logger.info(
                'Tentando criar as uniques de segurança dos conjuntos.')

            handler_uniques = HandlerUniques(self.db_adapter, REGISTROS)
            conseguiu_criar_uniques = handler_uniques.criar_uniques()
            print('Erros criação uniques:')
            print(conseguiu_criar_uniques)

            # Verificando se houve algum erro
            houve_erro = False
            for chave in conseguiu_criar_uniques:
                houve_erro = houve_erro or conseguiu_criar_uniques[chave]

            # TODO Adicionar teste para verificar se há conjuntos compartilhados por mais de uma empresa ou grupo

            #####################################################
            # TENTANDO REMEDIAR BASES MAIS SIMPLES
            logger.info(
                'Tentando remediar bases mais simples (recriando estrutura de conjuntos, para o caso de só haver um grupo empresarial.')

            # Tentando reconstruir toda a organização de conjuntos (se for uma instalação
            # em modo empresa, e com apenas um grupo empresarial):
            patch_recriar_estrutura_conjuntos = PatchRecriarEstruturaConjuntos(
                self.db_adapter)

            if houve_erro and patch_recriar_estrutura_conjuntos.can_execute(None):
                patch_recriar_estrutura_conjuntos.execute()

                logger.info(
                    'Tentando novamente criar as uniques de segurança dos conjuntos')
                conseguiu_criar_uniques = handler_uniques.criar_uniques(
                    self.db_adapter)

            #####################################################
            # REMEDIANDO OS ERROS PELOS PATCHES
            if len(conseguiu_criar_uniques) > 0:
                logger.info(
                    'Como ainda não foi é possível criar as uniques de segurança, serão aplicados os patches de correção cabíveis')

            for patch_key in PATCHES:
                logger.info(
                    f"Patch {patch_key}. Erros: {conseguiu_criar_uniques}")
                patch = PATCHES[patch_key](self.db_adapter)

                for registro in conseguiu_criar_uniques:
                    # Se não houver erros com este registro, pula o tratamento do mesmo
                    if conseguiu_criar_uniques[registro]:
                        continue

                    # Se puder aplicar o patch, tenta aplicar:
                    if patch.can_execute(registro):
                        logger.info(
                            f"Tentando aplicar o patch {patch_key}, para o tipo de registro {registro}")

                        # Rodando o patch
                        patch.execute(registro)

                        # Atualizando os erros de criacao dos FK
                        conseguiu_criar_uniques = handler_uniques.criar_uniques()

            #####################################################
            # IMPRIMINDO LOG FINAL DE ERROS
            tabelas_erro = [
                k for k in conseguiu_criar_uniques if not conseguiu_criar_uniques[k]]
            if len(tabelas_erro) > 0:
                logger.error(
                    'Não foi possível remediar os problemas de conjuntos das seguintes tabelas:')
                tabelas = ', '.join(tabelas_erro)
                logger.error(tabelas)

            self.log('Diagnóstico de conjuntos concluído')
        finally:
            self.log("--- TEMPO TOTAL GERAL %s seconds ---" %
                     (time.time() - start_time))
