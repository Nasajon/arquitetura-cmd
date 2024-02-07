import uuid

from suporte_console.exclusao_empresas.step import Step
from typing import Any, Dict, List


class Vertice:
    """
    Vértice para a busca em profundidade.
    """

    id: str
    schema: str
    table: str
    pk: str
    dependecia: str
    dependencias: List[Dict[str, Any]]
    pular: bool

    # Dicionário: key=chave vizinho; value=fk_column
    arestas: Dict[str, str]

    def __init__(self, id: str, schema: str, table: str, pk: str, pular: bool) -> None:
        self.id = id
        self.schema = schema
        self.table = table
        self.pk = pk
        self.arestas = {}
        self.dependecia = None
        self.dependencias = []
        self.pular = pular


class Grafo:
    """
    Grafo para a busca em profundidade.
    """

    # Dicionário: key=chave vertice; value=Vertice
    vertices: Dict[str, Vertice]

    def __init__(self) -> None:
        self.vertices = {}


class SelecaoDadosStep(Step):
    """
    Navega pelas dependências entre os dados, populando as tabelas de buffer,
    e preparando assim para a exclusãi de fato.
    """

    def dfs(self, grafo, id_vertice):
        """
        Algortimo de busca em profundidade (ligeriamente alterado para as necessidades locais).
        """

        vertice = grafo.vertices[id_vertice]
        visitados = []
        ordem_dependencias = []

        def dfs_recursiva(grafo: Grafo, vertice: Vertice, dependecia: Dict[str, str]):
            vertice.dependecia = dependecia
            visitados.append(vertice)

            for id_vizinho in vertice.arestas:
                vizinho = grafo.vertices[id_vizinho]
                next_dependecia = vertice.arestas[id_vizinho]
                if vizinho not in visitados:
                    dfs_recursiva(grafo, vizinho, next_dependecia)

            ordem_dependencias.append(vertice)

        dfs_recursiva(grafo, vertice, None)

        return (visitados, ordem_dependencias)

    def get_ids_empresas(self, codigos_empresas: str, invert_selecao: bool):
        # Tratando os códigos das empresas
        codigos = codigos_empresas.split(',')
        codigos = [c for c in codigos if c != '']

        # Fazendo a consulta no BD
        if not invert_selecao:
            sql = """
            select empresa as id from ns.empresas as e where e.codigo in :codigos_empresas
            """
        else:
            sql = """
            select empresa as id from ns.empresas as e where e.codigo not in :codigos_empresas
            """

        ids = self.db_adapter.execute_query(
            sql, codigos_empresas=tuple(codigos))

        return [i['id'] for i in ids]

    def is_modo_empresa(self):
        # Recuperando todas as entidades passiveis de exclusao
        sql = """
        SELECT VALOR as modo FROM NS.CONFIGURACOES WHERE CAMPO = 1 AND APLICACAO = 0
        """

        modo = self.db_adapter.execute_query_first_result(sql)

        if str(modo['modo']) == '0':
            return True
        else:
            return False

    def list_entidades(self, grafo: Grafo):
        # Recuperando todas as entidades passiveis de exclusao
        sql = """
        select * from exclusao.entidades where pk_name is not null and (not apenas_modo_contabil or :modo_contabil)
        """

        if self.is_modo_empresa():
            modo_contabil = False
        else:
            modo_contabil = True

        entidades = self.db_adapter.execute_query(
            sql, modo_contabil=modo_contabil)

        for entidade in entidades:
            id = '{}.{}'.format(
                entidade['schema_name'], entidade['table_name'])
            v = Vertice(id, entidade['schema_name'],
                        entidade['table_name'], entidade['pk_name'], entidade['pular'])
            grafo.vertices[id] = v

    def list_entidades_dependencias(self, grafo: Grafo):
        # Recuperando todas as depenências entre as entidades
        sql = """
        select * from exclusao.entidades_dependencias
        """

        dependencias = self.db_adapter.execute_query(sql)

        for dependencia in dependencias:
            id_origem_fk = '{}.{}'.format(
                dependencia['schema_name_origem'], dependencia['table_name_origem'])
            id_destino_fk = '{}.{}'.format(
                dependencia['schema_name_destino'], dependencia['table_name_destino'])

            if not(id_origem_fk in grafo.vertices) or not (id_destino_fk in grafo.vertices):
                continue

            vertice_mestre = grafo.vertices[id_destino_fk]
            vertice_mestre.arestas[id_origem_fk] = dependencia
            vertice_mestre.dependencias.append(dependencia)

    def popula_chaves_para_exclusao(self, grafo: Grafo, ordem: List[Vertice], empresas: List[uuid.UUID]):

        # Inserindo as empresas na tabela para exclusao
        for emp in empresas:
            sql = """
            insert into exclusao.ns (table_name, id, excluido)
            select 'empresas', :id, false where not exists (
                select 1 from exclusao.ns where table_name='empresas' and id=:id
            )
            """
            self.db_adapter.execute(sql, id=emp)

        # Percorrendo as tabelas para exclusao
        # for vertice in ordem[1:]:
        #     sql = f"""
        #     insert into exclusao.{vertice.schema} (table_name, id)
        #     select
        #         distinct '{vertice.table}', tv.{vertice.pk}
        #     from
        #         {vertice.schema}.{vertice.table} as tv
        #         join exclusao.{vertice.dependecia['schema_name_destino']} as te on (
        #             te.table_name = '{vertice.dependecia['table_name_destino']}'
        #             and tv.{vertice.dependecia['fk_column']} = te.id
        #         )
        #     """
        #     db_adapter.execute(sql)

        for vertice in ordem:
            self.log(f'Entidade {vertice.schema}.{vertice.table}')

            if vertice.pular:
                self.log(f'Pulando...')
                continue

            for dependencia in vertice.dependencias:
                id_origem_fk = '{}.{}'.format(
                    dependencia['schema_name_origem'], dependencia['table_name_origem'])
                vertice_aresta = grafo.vertices[id_origem_fk]

                self.log(
                    f"FK {id_origem_fk} Coluna: {dependencia['fk_column']}")

                # while True:
                # sql = f"""
                # insert into exclusao.{vertice_aresta.schema} (table_name, id)
                # select
                #     distinct '{vertice_aresta.table}', tv.{vertice_aresta.pk}
                # from
                #     {vertice_aresta.schema}.{vertice_aresta.table} as tv
                #     join exclusao.{vertice.schema} as te on (
                #         te.table_name = '{vertice.table}'
                #         and tv.{dependencia['fk_column']} = te.id
                #     )
                #     left join exclusao.{vertice_aresta.schema} as texist on (
                #         texist.table_name = '{vertice_aresta.table}'
                #         and texist.id = tv.{vertice_aresta.pk}
                #     )
                # where
                #     texist.id is null
                # limit {LIMITE_LINHAS_INSERT_SELECT}
                # """

                sql = f"""
                insert into exclusao.{vertice_aresta.schema} (table_name, id, excluido)
                select
                    distinct '{vertice_aresta.table}', tv.{vertice_aresta.pk}, false
                from
                    {vertice_aresta.schema}.{vertice_aresta.table} as tv
                    join exclusao.{vertice.schema} as te on (
                        te.table_name = '{vertice.table}'
                        and tv.{dependencia['fk_column']} = te.id
                    )
                """
                self.db_adapter.execute(sql)

                # if qtd_inseridas <= 0:
                #     break

    def main(self, data: str, invert_selecao: bool):
        self.log(
            'Selecionando os dados a excluir, de acordo com suas dependências para as empresas (populando os buffers de dados da exclusão)...')

        # Iniciando o Grafo
        grafo = Grafo()

        # Recuperando todas as entidades passiveis de exclusao, e adicionando no grafo
        self.list_entidades(grafo)

        # Recuperando as dependências entre entidades e adicionando no grafo
        self.list_entidades_dependencias(grafo)

        # Fazendo a busca em profundidade, para resolver a ordem de deleção
        _, ordem = self.dfs(grafo, 'ns.empresas')
        ordem.reverse()

        # Imprimindo a ordem de deleção
        for vertice in ordem:
            self.log(vertice.id)

        # Populando as chaves para exclusao
        ids_empresas = self.get_ids_empresas(data, invert_selecao)
        self.popula_chaves_para_exclusao(
            grafo,
            ordem,
            ids_empresas
        )
