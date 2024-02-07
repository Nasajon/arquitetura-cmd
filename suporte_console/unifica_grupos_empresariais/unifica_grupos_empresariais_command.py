import argparse
import copy
import time
import uuid

from typing import Any, Dict, List

from suporte_console.command import Command


class UnificaGruposEmpresariaisCommand(Command):

    # Dicionário entre a numeração dos cadastros, e suas respectivas tabelas de associação com os dados:
    CADASTROS = {
        0: 'conjuntosprodutos',
        1: 'conjuntosunidades',
        2: 'conjuntoscombustiveis',
        3: 'conjuntosservicos',
        4: 'conjuntosclassificacoesparticipantes',
        5: 'conjuntosfichas',
        6: 'conjuntosclientes',
        7: 'conjuntosfornecedores',
        8: 'conjuntostransportadoras',
        9: 'conjuntosvendedores',
        10: 'conjuntosservicosdecatalogos',
        11: 'conjuntosmodeloscontratos',
        12: 'conjuntostecnicos',
        13: 'conjuntosrubricas',
        14: 'conjuntosrepresentantescomerciais',
        15: 'conjuntosrepresentantestecnicos',
        16: 'conjuntosprospects'
    }

    # Queries para ajustar apontamento dos grupos_empresariais
    QUERIES_GRUPOS_EMPRESARIAIS = [
        'update compras.acordoscompras set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update compras.itenscompras set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update contabilizacao.classificacaofinanceiraporcontas set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update crm.documenttemplate set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update crm.documenttemplate set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update crm.listascontatos set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update crm.negociosoperacoes set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update crm.old_propostas set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update crm.pagemaster set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update crm.pagemaster set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update crm.segmentosatuacao set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update crm.tabelas_de_precos set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update estoque.atributos set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update estoque.categoriasdeprodutos set id_grupo_empresarial=:grupo_destino where id_grupo_empresarial in :grupos_origem',
        'update estoque.figurastributarias set id_grupo_empresarial=:grupo_destino where id_grupo_empresarial in :grupos_origem',
        'update estoque.itensparacalculosaldo set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update estoque.operacoes set id_grupo_empresarial=:grupo_destino where id_grupo_empresarial in :grupos_origem',
        'update estoque.perfil_importacao set id_grupo_empresarial=:grupo_destino where id_grupo_empresarial in :grupos_origem',
        'update estoque.perfiltrib_est set id_grupo_empresarial=:grupo_destino where id_grupo_empresarial in :grupos_origem',
        'update estoque.perfiltrib_fed set id_grupo_empresarial=:grupo_destino where id_grupo_empresarial in :grupos_origem',
        'update estoque.producao_modelos set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update estoque.producao_modelos_processos set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update estoque.rotas set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.ajustes set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.aplicacoes set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.arquivoretornoserasa set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update financas.arquivosremessaserasa set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update financas.benspatrimoniais set familia=:grupo_destino where familia in :grupos_origem',
        'update financas.cenariosorcamentarios set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.centroscustos set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.chequescustodias set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        # 'update financas.classificacoesfinanceiras set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.clientesenviadosserasa set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update financas.configuracoescontasinvestimentos set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.configuracoesfluxocaixa set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.configuracoesintegracoesconciliadoras set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.configuracoesterceirizacao set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update financas.contas set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update financas.contratos set familia=:grupo_destino where familia in :grupos_origem',
        'update financas.contratoscartoes set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.gruposcotgruposemp set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.historicosanalisesinadimplencias set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.inadimplenciasexcecoesclientes set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update financas.lancamentostituloscoberturascontas set idgrupoempresarial=:grupo_destino where idgrupoempresarial in :grupos_origem',
        'update financas.processamentoscontratos set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.projetos set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.rateiospadrao set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.rateiospadraorestricoes set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.reguascobrancas set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.reguascobrancas set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.relatoriosgruposclassificadores set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.renegociacoescontratos set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update financas.resgates set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.restricoescobrancas set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.restricoescobrancas set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update financas.vinculosgruposempresariais set grupoempresarialorigem=:grupo_destino where grupoempresarialorigem in :grupos_origem',
        'update financas.vinculosgruposempresariais set grupoempresarialvinculado=:grupo_destino where grupoempresarialvinculado in :grupos_origem',
        'update locacoes.lancamentomultiploativos set grupoempresarial_id=:grupo_destino where grupoempresarial_id in :grupos_origem',
        'update locacoes.modalidadesdepagamento set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update ns.atributos set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        # 'update ns.configuracoes set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update ns.configuracoescategoriasporclassfinan set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        # 'update ns.configuracoesnumeracoesdnf set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update ns.destinos_sincronizacao_gruposempresariais set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update ns.df_docfis set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update ns.documentosgeddetalhes set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update ns.emailsenviados set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update ns.empresas set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update ns.faixasdecreditos set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update ns.filtrosformularios set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update ns.gruposempresariaisacessosusuarios set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update ns.gruposempresariaiscadastros set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update ns.limitesdecreditosacessos set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update ns.limitesdecreditosconfiguracoes set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update ns.limitesdecreditosentidadesempresariais set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update ns.locaisdeuso set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update ns.pendencias set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update ns.regrasvencimentosclientes set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update ns.tabelas_precos_de_entregas set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update ns.usuarios set ultimogrupo=:grupo_destino where ultimogrupo in :grupos_origem',
        'update servicos.catalogosdeofertas set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update servicos.categoriasfuncoes set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update servicos.componentes set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update servicos.composicoes set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update servicos.custosmaodeobra set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update servicos.docpedidosvendasservicos set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update servicos.eventoscontratos set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update servicos.funcoes set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update servicos.gruposdecomponentes set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update servicos.gruposdeservicos set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update servicos.nfsoperacoes set grupoempresarial_id=:grupo_destino where grupoempresarial_id in :grupos_origem',
        'update servicos.objetosservicosbase set grupoempresarial_id=:grupo_destino where grupoempresarial_id in :grupos_origem',
        'update servicos.orcamentos set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update servicos.ordensservicos set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update servicos.pedidosvendasservicos set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update servicos.receitasdespesas set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update servicos.rpss set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update servicos.servicostecnicos set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update servicos.tiposfuncoes set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update servicos.tiposprojetos set grupoempresarial_id=:grupo_destino where grupoempresarial_id in :grupos_origem',
        'update servicos.tiposservicos set id_grupoempresarial=:grupo_destino where id_grupoempresarial in :grupos_origem',
        'update servicos.variaveisorcamentarias set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem',
        'update util.indices_gruposempresariais set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem'
    ]

    def ajusta_persmissoes_group_nasajon(self):
        """
        Roda a função ns.permissoes, para ajustar as permissões do BD.
        """

        try:
            sql = f"select * from ns.permissoes()"
            self.db_adapter.execute(sql)
        except Exception as e:
            self.log_warning(
                f"Erro manipulando permissões do BD clonado: {e}")

    def is_modo_empresa(self):
        """
        Retorna true se o BD estiver em modo empresa, e false, caso contrário.
        """

        sql = """
        SELECT VALOR as modo FROM NS.CONFIGURACOES WHERE CAMPO = 1 AND APLICACAO = 0
        """

        modo = self.db_adapter.execute_query_first_result(sql)

        if str(modo['modo']) == '0':
            return True
        else:
            return False

    def get_conjuntos_grupos(self, codigos_grupos: List[str]) -> List[Dict[str, Any]]:
        sql = f"""
        select
            gemp.grupoempresarial, ec.cadastro, ec.conjunto
        from
            ns.estabelecimentosconjuntos as ec
            join ns.estabelecimentos as est on (est.estabelecimento = ec.estabelecimento)
            join ns.empresas as emp on (emp.empresa = est.empresa)
            join ns.gruposempresariais as gemp on (gemp.grupoempresarial = emp.grupoempresarial)
        where
            gemp.codigo in :codigos_grupos
            and ec.cadastro <> 13
        	and ec.conjunto <> coalesce((select conjunto from ns.conjuntos where cadastro=7 and codigo='11'), '00000000-0000-0000-0000-000000000000'::UUID)
        group by
            gemp.grupoempresarial, ec.cadastro, ec.conjunto
        """

        return self.db_adapter.execute_query(
            sql, codigos_grupos=tuple(codigos_grupos))

    def migra_dados_conjunto(self, tipo_cadastro: int, conjunto_origem: uuid.UUID, conjunto_destino: uuid.UUID):

        tabela = self.CADASTROS[tipo_cadastro]
        sql = f"update ns.{tabela} set conjunto=:conjunto_destino where conjunto=:conjunto_origem"
        self.db_adapter.execute(
            sql, conjunto_origem=conjunto_origem, conjunto_destino=conjunto_destino)

    def migra_estabelecimentos_conjunto(self, tipo_cadastro: int, conjunto_origem: uuid.UUID, conjunto_destino: uuid.UUID):

        sql = f"update ns.estabelecimentosconjuntos set conjunto=:conjunto_destino where conjunto=:conjunto_origem and cadastro=:tipo_cadastro"
        self.db_adapter.execute(
            sql, conjunto_origem=conjunto_origem, conjunto_destino=conjunto_destino, tipo_cadastro=tipo_cadastro)

    def excluir_conjunto(self, tipo_cadastro: int, conjunto: uuid.UUID):

        sql = f"delete from ns.conjuntos where conjunto=:conjunto and cadastro=:tipo_cadastro"
        self.db_adapter.execute(sql, conjunto=conjunto,
                                tipo_cadastro=tipo_cadastro)

    def get_ids_grupos(self, codigos_grupos: List[str]) -> List[uuid.UUID]:
        sql = f"""
        select
            gemp.grupoempresarial
        from
            ns.gruposempresariais as gemp
        where
            gemp.codigo in :codigos_grupos
        """

        lista = self.db_adapter.execute_query(
            sql, codigos_grupos=tuple(codigos_grupos))

        return [g['grupoempresarial'] for g in lista]

    def excluir_grupos_empresariais(self, ids_grupos_empresariais: List[uuid.UUID]):

        sql = f"delete from ns.gruposempresariais where grupoempresarial in :grupos"
        self.db_adapter.execute(sql, grupos=tuple(ids_grupos_empresariais))

    def backup_conjuntos(self):
        """
        Cria tabelas para backup completo da estrautura de conjuntos do BD (os conjuntos em si,
        suas associações com os estabelecimentos e com os dados).
        """

        # Copiando tabelas de estrutura
        sqls = [
            'create table conjuntos_bkp as select * from ns.conjuntos;',
            'create table estabelecimentosconjuntos_bkp as select * from ns.estabelecimentosconjuntos;'
        ]

        for sql in sqls:
            try:
                self.db_adapter.execute(sql)
            except Exception as e:
                self.log_warning(f'Problema ao criar tabela de backup: {e}')

        # Tratando do owner destas tabelas
        try:
            sqls = [
                'alter table conjuntos_bkp owner to group_nasajon;'
                'alter table estabelecimentosconjuntos_bkp owner to group_nasajon;'
            ]

            for sql in sqls:
                self.db_adapter.execute(sql)
        except:
            pass

        # Copiando tabelas de cadastro
        for cadastro in self.CADASTROS:
            tabela = self.CADASTROS[cadastro]

            try:
                sql = f"create table {tabela}_bkp as select * from ns.{tabela};"
                self.db_adapter.execute(sql)
            except Exception as e:
                self.log_warning(f'Problema ao criar tabela de backup: {e}')

            # Tratando do owner da tabela
            try:
                sql = f"alter table {tabela}_bkp owner to group_nasajon;"
                self.db_adapter.execute(sql)
            except:
                pass

    def backup_grupos_empresariais(self):

        # Criando tabela de backup
        try:
            sql = "create table gruposempresariais_bkp as select * from ns.gruposempresariais"
            self.db_adapter.execute(sql)
        except Exception as e:
            self.log_warning(
                f'Problema ao criar tabela de backup: {e} - Origem grupo empresarial')

        # Tratando do owner da tabela de backup
        try:
            sql = f"alter table gruposempresariais_bkp owner to group_nasajon;"
            self.db_adapter.execute(sql)
        except:
            self.log_warning(
                f'Erro ao dar permissão para tabela de backup: {e} - Origem grupo emprearial')

    def backup_tabela(self, schema: str, tabela: str):

        # Criando tabela de backup
        try:
            sql = f"create table {tabela}_bkp as select * from {schema}.{tabela}"
            self.db_adapter.execute(sql)
        except Exception as e:
            self.log_warning(
                f'Problema ao criar tabela de backup: {e} - Origem {schema}.{tabela}')

        # Tratando do owner da tabela de backup
        try:
            sql = f"alter table {tabela}_bkp owner to group_nasajon;"
            self.db_adapter.execute(sql)
        except:
            self.log_warning(
                f'Erro ao dar permissão para tabela de backup: {e} - Origem {schema}.{tabela}')

    def tratar_casos_especiais(self, id_grupo_destino: uuid.UUID, ids_grupos_origem: uuid.UUID):

        # tabela ns.configuracoesnumeracoesdnf
        self.log(f"Tabela especial: ns.configuracoesnumeracoesdnf.")
        self.backup_tabela('ns', 'configuracoesnumeracoesdnf')
        self.tratar_configuracoesnumeracoesdnf(
            id_grupo_destino, ids_grupos_origem)

        # tabela financas.classificacoesfinanceiras
        self.log(f"Tabela especial: financas.classificacoesfinanceiras.")
        self.backup_tabela('financas', 'classificacoesfinanceiras')
        self.tratar_classificacoesfinanceiras(
            id_grupo_destino, ids_grupos_origem)

        # tabela ns.configuracoes
        self.log(f"Tabela especial: ns.configuracoes.")
        self.backup_tabela('ns', 'configuracoes')
        self.tratar_configuracoes(id_grupo_destino, ids_grupos_origem)

    def tratar_configuracoes(self, id_grupo_destino: uuid.UUID, ids_grupos_origem: List[uuid.UUID]):

        # Copiando as configurações que não existam no destino (escolhendo uma ao acaso), e que não sejam de empresa, estabelecimento e nem de usuário
        sql = """
        select
           c.campo, c.valor, c.grupo, c.sessao, c.camadasistema, c.maquina, c.versao, c.aplicacao, c.ano, c.ano_ini, c.tipo_ini, c.nome_ini, c.grupo_ini, c.campo_ini, c.date_ini, c.boolean_ini, c.integer_ini, c.largeint_ini, c.currency_ini, c.float_ini, c.guid_ini, c.string_ini, c.empresa, c.chave_ini, c.estabelecimento, c.usuario, c.identificacao, c.grupoempresarial, c.lastupdate, c.tenant, c.valorbytea
        from
            ns.configuracoes as c
            left join ns.configuracoes as c2 on (
                coalesce(c.campo, -1) = coalesce(c2.campo, -1)
                and coalesce(c.grupo, -1) = coalesce(c2.grupo, -1)
                and coalesce(c.sessao, -1) = coalesce(c2.sessao, -1)
                and coalesce(c.camadasistema, -1) = coalesce(c2.camadasistema, -1)
                and coalesce(c.aplicacao, -1) = coalesce(c2.aplicacao, -1)
                and c.configuracao <> c2.configuracao
                and c2.grupoempresarial = :grupo_destino
                and c2.empresa is null
                and c2.estabelecimento is null
                and c2.usuario is null
                and c2.identificacao is null
            )
        where
            c.grupoempresarial in :grupos
            and c2.configuracao is null
            and c.empresa is null
            and c.estabelecimento is null
            and c.usuario is null
            and c.identificacao is null
            and c.valor <> c2.valor
        """
        configuracoes_origem = self.db_adapter.execute_query(
            sql, grupos=tuple(ids_grupos_origem), grupo_destino=id_grupo_destino)
        configs_resolvidas = set()

        for config_origem in configuracoes_origem:
            id_config = f"{config_origem['campo']}__{config_origem['grupo']}__{config_origem['sessao']}__{config_origem['camadasistema']}__{config_origem['aplicacao']}"

            if id_config in configs_resolvidas:
                continue

            sql = """
            insert into ns.configuracoes (
            campo, valor, grupo, sessao, camadasistema, maquina, versao, aplicacao, ano, ano_ini, tipo_ini, nome_ini, grupo_ini, campo_ini, date_ini, boolean_ini, integer_ini, largeint_ini, currency_ini, float_ini, guid_ini, string_ini, empresa, chave_ini, estabelecimento, usuario, identificacao, grupoempresarial, lastupdate, tenant, valorbytea)
            values (:campo, :valor, :grupo, :sessao, :camadasistema, :maquina, :versao, :aplicacao, :ano, :ano_ini, :tipo_ini, :nome_ini, :grupo_ini, :campo_ini, :date_ini, :boolean_ini, :integer_ini, :largeint_ini, :currency_ini, :float_ini, :guid_ini, :string_ini, :empresa, :chave_ini, :estabelecimento, :usuario, :identificacao, :grupoempresarial, :lastupdate, :tenant, :valorbytea)
            """
            self.db_adapter.execute(sql, grupoempresarial=id_grupo_destino, campo=config_origem['campo'], valor=config_origem['valor'], grupo=config_origem['grupo'], sessao=config_origem['sessao'], camadasistema=config_origem['camadasistema'], maquina=config_origem['maquina'], versao=config_origem['versao'], aplicacao=config_origem['aplicacao'], ano=config_origem['ano'], ano_ini=config_origem['ano_ini'], tipo_ini=config_origem['tipo_ini'], nome_ini=config_origem['nome_ini'], grupo_ini=config_origem['grupo_ini'], campo_ini=config_origem['campo_ini'], date_ini=config_origem[
                                    'date_ini'], boolean_ini=config_origem['boolean_ini'], integer_ini=config_origem['integer_ini'], largeint_ini=config_origem['largeint_ini'], currency_ini=config_origem['currency_ini'], float_ini=config_origem['float_ini'], guid_ini=config_origem['guid_ini'], string_ini=config_origem['string_ini'], empresa=config_origem['empresa'], chave_ini=config_origem['chave_ini'], estabelecimento=config_origem['estabelecimento'], usuario=config_origem['usuario'], identificacao=config_origem['identificacao'], lastupdate=config_origem['lastupdate'], tenant=config_origem['tenant'], valorbytea=config_origem['valorbytea'])

            configs_resolvidas.add(id_config)

        # Copiando as configurações que não existam no destino (escolhendo uma ao acaso), e que sejam de usuário (mas não de empresa, nem de estabelecimento)
        sql = """
        select
           c.campo, c.valor, c.grupo, c.sessao, c.camadasistema, c.maquina, c.versao, c.aplicacao, c.ano, c.ano_ini, c.tipo_ini, c.nome_ini, c.grupo_ini, c.campo_ini, c.date_ini, c.boolean_ini, c.integer_ini, c.largeint_ini, c.currency_ini, c.float_ini, c.guid_ini, c.string_ini, c.empresa, c.chave_ini, c.estabelecimento, c.usuario, c.identificacao, c.grupoempresarial, c.lastupdate, c.tenant, c.valorbytea
        from
            ns.configuracoes as c
            left join ns.configuracoes as c2 on (
                coalesce(c.campo, -1) = coalesce(c2.campo, -1)
                and coalesce(c.grupo, -1) = coalesce(c2.grupo, -1)
                and coalesce(c.sessao, -1) = coalesce(c2.sessao, -1)
                and coalesce(c.camadasistema, -1) = coalesce(c2.camadasistema, -1)
                and coalesce(c.aplicacao, -1) = coalesce(c2.aplicacao, -1)
                and c.usuario = c2.usuario
                and c.configuracao <> c2.configuracao
                and c2.grupoempresarial = :grupo_destino
                and c2.empresa is null
                and c2.estabelecimento is null
                and c2.identificacao is null
                and c2.usuario is not null
            )
        where
            c.grupoempresarial in :grupos
            and c2.configuracao is null
            and c.empresa is null
            and c.estabelecimento is null
            and c.identificacao is null
            and c.usuario is not null
        """
        configuracoes_origem = self.db_adapter.execute_query(
            sql, grupos=tuple(ids_grupos_origem), grupo_destino=id_grupo_destino)
        configs_resolvidas = set()

        for config_origem in configuracoes_origem:
            id_config = f"{config_origem['campo']}__{config_origem['grupo']}__{config_origem['sessao']}__{config_origem['camadasistema']}__{config_origem['aplicacao']}"

            if id_config in configs_resolvidas:
                continue

            sql = """
            insert into ns.configuracoes (
            campo, valor, grupo, sessao, camadasistema, maquina, versao, aplicacao, ano, ano_ini, tipo_ini, nome_ini, grupo_ini, campo_ini, date_ini, boolean_ini, integer_ini, largeint_ini, currency_ini, float_ini, guid_ini, string_ini, empresa, chave_ini, estabelecimento, usuario, identificacao, grupoempresarial, lastupdate, tenant, valorbytea)
            values (:campo, :valor, :grupo, :sessao, :camadasistema, :maquina, :versao, :aplicacao, :ano, :ano_ini, :tipo_ini, :nome_ini, :grupo_ini, :campo_ini, :date_ini, :boolean_ini, :integer_ini, :largeint_ini, :currency_ini, :float_ini, :guid_ini, :string_ini, :empresa, :chave_ini, :estabelecimento, :usuario, :identificacao, :grupoempresarial, :lastupdate, :tenant, :valorbytea)
            """
            self.db_adapter.execute(sql, grupoempresarial=id_grupo_destino, campo=config_origem['campo'], valor=config_origem['valor'], grupo=config_origem['grupo'], sessao=config_origem['sessao'], camadasistema=config_origem['camadasistema'], maquina=config_origem['maquina'], versao=config_origem['versao'], aplicacao=config_origem['aplicacao'], ano=config_origem['ano'], ano_ini=config_origem['ano_ini'], tipo_ini=config_origem['tipo_ini'], nome_ini=config_origem['nome_ini'], grupo_ini=config_origem['grupo_ini'], campo_ini=config_origem['campo_ini'], date_ini=config_origem[
                                    'date_ini'], boolean_ini=config_origem['boolean_ini'], integer_ini=config_origem['integer_ini'], largeint_ini=config_origem['largeint_ini'], currency_ini=config_origem['currency_ini'], float_ini=config_origem['float_ini'], guid_ini=config_origem['guid_ini'], string_ini=config_origem['string_ini'], empresa=config_origem['empresa'], chave_ini=config_origem['chave_ini'], estabelecimento=config_origem['estabelecimento'], usuario=config_origem['usuario'], identificacao=config_origem['identificacao'], lastupdate=config_origem['lastupdate'], tenant=config_origem['tenant'], valorbytea=config_origem['valorbytea'])

            configs_resolvidas.add(id_config)

        # Alterando as configurações que eram de empresa ou estabelecimento
        sql = """
        update ns.configuracoes set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem and (empresa is not null or estabelecimento is not null)
        """
        self.db_adapter.execute(
            sql, grupo_destino=id_grupo_destino, grupos_origem=tuple(ids_grupos_origem))

        # Excluindo as configurações dos grupos empresariais de origem
        sql = """
        delete from ns.configuracoes where grupoempresarial in :grupos_origem
        """
        self.db_adapter.execute(sql, grupos_origem=tuple(ids_grupos_origem))

    def tratar_classificacoesfinanceiras(self, id_grupo_destino: uuid.UUID, ids_grupos_origem: List[uuid.UUID]):

        grupos = copy.deepcopy(ids_grupos_origem)
        grupos.append(id_grupo_destino)

        # Adicionando o codigo dos grupos empresariais no início do código das classificações financeiras repetidas entre os grupos
        # de origem (há uma UK que não permite mais de uma classificação com mesmo código num mesmo grupo; mas, como estamos unificando
        # # grupos, é necessário antes remediar as repeitos, no caso, adicionando o código do grupo no no código das classficações
        # # repetidas):
        sql = """
        with codigos_repetido as (
        select codigo from financas.classificacoesfinanceiras where grupoempresarial in :grupos group by codigo having count(*)>1
        )
        update financas.classificacoesfinanceiras set codigo = ge.codigo || '_' || financas.classificacoesfinanceiras.codigo
        from ns.gruposempresariais as ge, codigos_repetido as cr
        where ge.grupoempresarial=financas.classificacoesfinanceiras.grupoempresarial
        and cr.codigo=financas.classificacoesfinanceiras.codigo
        """

        self.db_adapter.execute(sql, grupos=tuple(grupos))

        # Movendo as classificações financeiras para o destino
        sql = """
        update financas.classificacoesfinanceiras set grupoempresarial=:grupo_destino where grupoempresarial in :grupos_origem
        """

        self.db_adapter.execute(
            sql, grupo_destino=id_grupo_destino, grupos_origem=tuple(ids_grupos_origem))

    def tratar_configuracoesnumeracoesdnf(self, id_grupo_destino: uuid.UUID, ids_grupos_origem: uuid.UUID):

        # Recuperando as configurações do grupo de destino (para geração automática ou semi automática)
        sql = """
        SELECT configuracaonumeracaodnf, entidade, proximonumero FROM ns.configuracoesnumeracoesdnf where tiponumeracao in (0,1) and modogeracao=0 and grupoempresarial=:grupo
        """

        configuracoes_destino = self.db_adapter.execute_query(
            sql, grupo=id_grupo_destino)

        # Tratando cada configuração de destino
        for config_destino in configuracoes_destino:
            # Recuperando as configurações equivalentes para os grupos de origem
            sql = """
            SELECT proximonumero FROM ns.configuracoesnumeracoesdnf where tiponumeracao in (0,1) and modogeracao=0 and grupoempresarial in :grupos and entidade=:entidade
            """

            configuracoes_origem = self.db_adapter.execute_query(
                sql, grupos=tuple(ids_grupos_origem), entidade=config_destino['entidade'])

            # Resolvendo o maior próximo número
            proximo_numero = config_destino['proximonumero']
            for config_origem in configuracoes_origem:
                if config_origem['proximonumero'] is None:
                    continue

                if (proximo_numero or 0) < config_origem['proximonumero']:
                    proximo_numero = config_origem['proximonumero']

            # Atualizando o próximo número do destino (para o maior dentre todos os equivalentes nos outros grupos)
            if proximo_numero is not None:
                sql = """
                update ns.configuracoesnumeracoesdnf set proximonumero=:proximo_numero where configuracaonumeracaodnf=:id
                """
                self.db_adapter.execute(
                    sql, proximo_numero=proximo_numero, id=config_destino['configuracaonumeracaodnf'])

        # Copiando as configurações que eventualmente não existissem no destino
        # Obs.: Uma configuração (dentre as muitas possíveis, para os grupos empresariais de origem, é selecionada aleatoriamente)
        sql = """
        select
            d.grupoempresarial, d.entidade, d.tiponumeracao, d.modogeracao, d.codigo, d.descricao, d.mascara, d.novomodelo, d.proximonumero
        from
            ns.configuracoesnumeracoesdnf as o
            left join ns.configuracoesnumeracoesdnf as d on (
                d.entidade = o.entidade
                and d.configuracaonumeracaodnf <> o.configuracaonumeracaodnf
                and d.grupoempresarial = :grupo_destino
            )
        where
            o.grupoempresarial in :grupos
            and d.configuracaonumeracaodnf is null
        """
        configuracoes_origem = self.db_adapter.execute_query(
            sql, grupos=tuple(ids_grupos_origem), grupo_destino=id_grupo_destino)
        entidades_resolvidas = set()

        for config_origem in configuracoes_origem:
            if config_destino['entidade'] in entidades_resolvidas:
                continue

            sql = """
            insert into ns.configuracoesnumeracoesdnf (
            grupoempresarial, entidade, tiponumeracao, modogeracao, codigo, descricao, mascara, novomodelo, proximonumero)
            values (:grupoempresarial, :entidade, :tiponumeracao, :modogeracao, :codigo, :descricao, :mascara, :novomodelo, :proximonumero)
            """
            self.db_adapter.execute(sql, grupoempresarial=id_grupo_destino, entidade=config_origem['entidade'], tiponumeracao=config_origem['tiponumeracao'], modogeracao=config_origem['modogeracao'], codigo=config_origem[
                                    'codigo'], descricao=config_origem['descricao'], mascara=config_origem['mascara'], novomodelo=config_origem['novomodelo'], proximonumero=config_origem['proximonumero'])

            entidades_resolvidas.add(config_origem['entidade'])

        # Excluindo as configurações dos grupos de origem
        sql = """
        delete from ns.configuracoesnumeracoesdnf where grupoempresarial in :grupos
        """
        self.db_adapter.execute(sql, grupos=tuple(ids_grupos_origem))

    def main(self, pars: List[str]):
        # self.config_logger()

        start_time = time.time()
        try:
            # Parsing command line arguments
            parser = argparse.ArgumentParser(
                description="""Utilitário para unificar vários grupos empresariais num único grupo de destino.""")

            parser.add_argument(
                "-r", "--origem", help="Lista dos códigos dos grupos empresariais de origem, os quais deixarão de existir (separados por vírgulas).", required=True)

            parser.add_argument(
                "-i", "--destino", help="Código do grupo empresarial de destino, que receberá todas os dados dos grupos de origem.", required=True)

            # Guardando os parâmetros de entrada em variáveis para uso interno
            args, _ = parser.parse_known_args(pars)
            grupos_origem = args.origem.split(',')
            grupos_origem = [c for c in grupos_origem if c.strip() != '']

            grupo_destino = args.destino

            # Validando de o destino está na origem
            if grupo_destino in grupos_origem:
                raise Exception(
                    f"O grupo de destino {grupo_destino} não pode constar nos grupos de origem: {grupos_origem}")

            # Notificando início do processamento
            self.log(
                f"Unificando os grupos empresariais de origem: {grupos_origem}, para o grupo de destino {grupo_destino}")

            # Ajustando as permissões do BD
            self.log('Ajustando permissoes do group nasajon')
            self.ajusta_persmissoes_group_nasajon()

            if self.is_modo_empresa():
                self.log(
                    'Banco em modo empresa, será necessário alterar as estruturas dos conjuntos.')

                # Fazendo backup da estrutura de conjuntos:
                self.log('Criando um backup da estrutura de conjuntos')
                self.backup_conjuntos()

                # Recuperando os conjuntos (por tipo de cadastro), do grupo empresarial de destino
                conjuntos_destino = self.get_conjuntos_grupos([grupo_destino])
                conjuntos_destino = {c['cadastro']: c['conjunto']
                                     for c in conjuntos_destino}
                
                if len(conjuntos_destino) == 0:
                    raise Exception(
                        f"O grupo de destino {grupo_destino} deve conter pelo menos uma empresa e um estabelecimento vinculado.")

                # Recuperando os conjuntos (por tipo de cadastro), dos grupos empresariais de origem
                conjuntos_origem = self.get_conjuntos_grupos(grupos_origem)

                # Migrando os dados de cada conjunto de origem, para o destino correspondente
                for conjunto in conjuntos_origem:
                    # Migrando os dados
                    self.log(
                        f"Migrando os dados do conjunto {conjunto['conjunto']}, para o conjunto {conjuntos_destino[conjunto['cadastro']]}.")
                    self.migra_dados_conjunto(
                        conjunto['cadastro'], conjunto['conjunto'], conjuntos_destino[conjunto['cadastro']])

                    # Migrando os estabelecimentos
                    self.log(
                        f"Migrando a associação do estabelecimentos do conjunto {conjunto['conjunto']}, para o conjunto {conjuntos_destino[conjunto['cadastro']]}.")
                    self.migra_estabelecimentos_conjunto(
                        conjunto['cadastro'], conjunto['conjunto'], conjuntos_destino[conjunto['cadastro']])

                    # Excluíndo o conjunto de origem
                    self.log(f"Excluindo o conjunto {conjunto['conjunto']}.")
                    self.excluir_conjunto(
                        conjunto['cadastro'], conjunto['conjunto'])

            # Fazendo backup dos grupos_empresariais
            self.log(f"Fazendo backup dos grupos_empresariais.")
            self.backup_grupos_empresariais()

            # Recuperando os ids dos grupos empresariais envolvidos
            ids_grupos_origem = self.get_ids_grupos(grupos_origem)
            id_grupo_destino = self.get_ids_grupos([grupo_destino])[0]

            # Reponterando as tabelas que apontavam para os grupos empresariais de origem para o destino
            self.log(
                f"Reponterando as tabelas que apontavam para os grupos empresariais de origem para o destino.")
            for sql in self.QUERIES_GRUPOS_EMPRESARIAIS:
                try:
                    self.log(f"QUERY: {sql}")
                    self.db_adapter.execute(
                        sql, grupo_destino=id_grupo_destino, grupos_origem=tuple(ids_grupos_origem))
                except Exception as e:
                    self.log_exception(f"Erro executando query: {sql}")

            # Tratando casos especiais
            self.log(f"Tratando casos especiais.")
            self.tratar_casos_especiais(id_grupo_destino, ids_grupos_origem)

            # Excluindo os grupos_empresariais
            self.log(f"Excluindo os grupos empresariais unificados.")
            self.excluir_grupos_empresariais(ids_grupos_origem)

            # Notificando o fim do processamento
            self.log('Concluindo a unificação dos grupos empresariais')
        finally:
            self.log("--- TEMPO TOTAL GERAL %s seconds ---" %
                     (time.time() - start_time))
