import logging

from suporte_console.db_adapter2 import DBAdapter2


class PatchRecriarEstruturaConjuntos:
    def __init__(self, db_adapter: DBAdapter2) -> None:
        self.db_adapter = db_adapter

    def can_execute(self, registro_tipo: str) -> bool:
        sql = """
        SELECT VALOR FROM NS.CONFIGURACOES WHERE CAMPO = 1 AND APLICACAO = 0
        """

        modo_instalacao = self.db_adapter.get_single_result(sql)

        sql = """
        select count(*) from ns.gruposempresariais;
        """

        qtd_grupos_empresariais = self.db_adapter.get_single_result(sql)

        return modo_instalacao == 0 and qtd_grupos_empresariais == 1

    def execute(self, registro_tipo: str):

        # Getting logger
        logger = logging.getLogger('diagnostico_conjuntos')

        # Apagando as tabelas de registros
        logger.info('Apagando as tabelas de registros')
        sqls = [
            'truncate ns.conjuntosprodutos;',
            'truncate ns.conjuntosunidades;',
            'truncate ns.conjuntoscombustiveis;',
            'truncate ns.conjuntosservicos;',
            'truncate ns.conjuntosclassificacoesparticipantes;',
            'truncate ns.conjuntosfichas;',
            'truncate ns.conjuntosclientes;',
            'truncate ns.conjuntosfornecedores;',
            'truncate ns.conjuntostransportadoras;',
            'truncate ns.conjuntosvendedores;',
            'truncate ns.conjuntosservicosdecatalogos;',
            'truncate ns.conjuntosmodeloscontratos;',
            'truncate ns.conjuntostecnicos;',
            'truncate ns.conjuntosrubricas;',
            'truncate ns.conjuntosrepresentantescomerciais;',
            'truncate ns.conjuntosrepresentantestecnicos;',
            'truncate ns.conjuntosprospects;'
        ]

        for sql in sqls:
            self.db_adapter.execute(sql)

        # Apagando as tabelas de estrutura
        logger.info('Apagando as tabelas de estrutura')
        sqls = [
            'truncate ns.estabelecimentosconjuntos;',
            'delete from ns.conjuntos;'
        ]

        for sql in sqls:
            self.db_adapter.execute(sql)

        # Refazendo a tabela de ns.conjuntos
        logger.info('Refazendo a tabela de ns.conjuntos')
        sqls = [
            "INSERT INTO ns.conjuntos (conjunto, descricao, cadastro, codigo) VALUES ('11111111-1111-1111-1111-111111111111'::uuid, 'CONJUNTO RESERVADO PARA ERRO DE PREENCHIMENTO DO ID_CONJUNTO.', -1, 'ERRO');",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 0, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 1, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 2, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 3, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 4, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 5, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 6, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 7, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 8, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 9, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 10, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 11, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 12, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 14, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 15, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) VALUES (((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)), 16, ((select ge.codigo from ns.gruposempresariais as ge) || (select e.codigo from ns.estabelecimentos as e where matriz order by lastupdate limit 1)));",
            "INSERT INTO ns.conjuntos (descricao, cadastro, codigo) select ((select ge.codigo from ns.gruposempresariais as ge) || e.codigo), 13, ((select ge.codigo from ns.gruposempresariais as ge) || e.codigo) from ns.empresas as e;"
        ]

        for sql in sqls:
            self.db_adapter.execute(sql)

        # Refazendo a tabela de ns.estabelecimentosconjuntos
        logger.info('Refazendo a tabela de ns.estabelecimentosconjuntos')
        sqls = [
            "insert into ns.estabelecimentosconjuntos (estabelecimento, conjunto, cadastro, permissao) select e.estabelecimento, c.conjunto, c.cadastro, true from ns.estabelecimentos e, ns.conjuntos c where c.cadastro <> 13 and c.cadastro <> -1;",
            "insert into ns.estabelecimentosconjuntos (estabelecimento, conjunto, cadastro, permissao) select e.estabelecimento, c.conjunto, c.cadastro, true from ns.gruposempresariais g join ns.empresas emp on (emp.grupoempresarial = g.grupoempresarial) join ns.estabelecimentos e on (e.empresa = emp.empresa) join ns.conjuntos c on (c.cadastro = 13 and c.codigo = (g.codigo || emp.codigo));"
        ]

        for sql in sqls:
            self.db_adapter.execute(sql)

        # Refazendo as tabelas de registros
        logger.info('Refazendo as tabelas de registros')
        sqls = [
            "insert into ns.conjuntosprodutos (registro, conjunto) select p.produto, c.conjunto from estoque.produtos p join ns.conjuntos c on (c.cadastro=0);",
            "insert into ns.conjuntosprodutos (registro, conjunto) select i.id, c.conjunto from estoque.itens i join ns.conjuntos c on (c.cadastro=0);",
            "insert into ns.conjuntosunidades (registro, conjunto) select u.unidade, c.conjunto from estoque.unidades u join ns.conjuntos c on (c.cadastro=1);",
            "insert into ns.conjuntoscombustiveis (registro, conjunto) select cc.id, c.conjunto from scritta.cmb_combustiveis cc join ns.conjuntos c on (c.cadastro=2);",
            "insert into ns.conjuntosservicos (registro, conjunto) select s.id, c.conjunto from servicos.servicos s join ns.conjuntos c on (c.cadastro=3);",
            "insert into ns.conjuntosclassificacoesparticipantes (registro, conjunto) select cp.id, c.conjunto from ns.clapes cp join ns.conjuntos c on (c.cadastro=4);",
            "insert into ns.conjuntosfichas (registro, conjunto) select p.id, c.conjunto from ns.pessoas p join ns.conjuntos c on (c.cadastro=5);",
            "insert into ns.conjuntosclientes (registro, conjunto) select p.id, c.conjunto from ns.pessoas p join ns.conjuntos c on (c.cadastro=6 and p.clienteativado = 1);",
            "insert into ns.conjuntosfornecedores (registro, conjunto) select p.id, c.conjunto from ns.pessoas p join ns.conjuntos c on (c.cadastro=7 and p.fornecedorativado = 1);",
            "insert into ns.conjuntostransportadoras (registro, conjunto) select p.id, c.conjunto from ns.pessoas p join ns.conjuntos c on (c.cadastro=8 and p.transportadoraativado = 1);",
            "insert into ns.conjuntosvendedores (registro, conjunto) select p.id, c.conjunto from ns.pessoas p join ns.conjuntos c on (c.cadastro=9 and p.vendedorativado = 1);",
            "insert into ns.conjuntosservicosdecatalogos (registro, conjunto) select s.servicocatalogo, c.conjunto from servicos.servicoscatalogo s join ns.conjuntos c on (c.cadastro=10);",
            "insert into ns.conjuntosmodeloscontratos (registro, conjunto) select m.modelocontrato, c.conjunto from financas.modeloscontratos m join ns.conjuntos c on (c.cadastro=11);",
            "insert into ns.conjuntostecnicos (registro, conjunto) select p.id, c.conjunto from ns.pessoas p join ns.conjuntos c on (c.cadastro=12 and p.tecnicoativado = 1);",
            "insert into ns.conjuntosrepresentantescomerciais (registro, conjunto) select p.id, c.conjunto from ns.pessoas p join ns.conjuntos c on (c.cadastro=14 and p.representantecomercialativado = 1);",
            "insert into ns.conjuntosrepresentantestecnicos (registro, conjunto) select p.id, c.conjunto from ns.pessoas p join ns.conjuntos c on (c.cadastro=15 and p.representantetecnicoativado = 1);",
            "insert into ns.conjuntosprospects (registro, conjunto) select p.id, c.conjunto from ns.pessoas p join ns.conjuntos c on (c.cadastro=16 and p.prospectativado = 1);",
            "insert into ns.conjuntosrubricas (registro, conjunto) select ev.evento, ec.conjunto from persona.eventos ev join ns.empresas emp on (emp.empresa = ev.empresa) join ns.estabelecimentos e on (e.empresa = emp.empresa) join ns.estabelecimentosconjuntos ec on (ec.cadastro=13 and ec.estabelecimento = e.estabelecimento);"
        ]

        for sql in sqls:
            self.db_adapter.execute(sql)
