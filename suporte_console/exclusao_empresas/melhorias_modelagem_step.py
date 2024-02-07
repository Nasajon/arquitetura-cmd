from suporte_console.exclusao_empresas.step import Step

MELHORIAS_MODELAGEM_SCRITTA = """
alter table scritta.sped_pc_c100 add column id_uuid uuid not null default uuid_generate_v4();
alter table scritta.sped_pc_c175 add column id_uuid uuid not null default uuid_generate_v4();
"""

CRIAR_TABELA_ENTIDADES = """
create schema exclusao;

CREATE TABLE exclusao.entidades (
	schema_name varchar(50) NOT NULL,
	table_name varchar(100) NOT NULL,
	pk_name varchar(150) NULL,
	apenas_modo_contabil bool NOT NULL DEFAULT false,
	pular bool NOT NULL DEFAULT false
);
alter table exclusao.entidades add constraint pk_exclusao_entidades primary key (schema_name, table_name);

INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'benscontabilizacoes', 'bemcontabilizacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'bensdadosfiscais', 'bemdadofiscal', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'bensexercicios', 'bemexercicio', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'bensocorrencias', 'bemocorrencia', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'bensparalisacoes', 'bemparalisacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'camposformulasfinanceiras', 'campo', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'centrosdecusto', 'centrodecusto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'centrosdecustoanuais', 'centrodecustoanual', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'classificacaocontas', 'classificacaoconta', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'conciliacao', 'conciliacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'configuracoescontasbens', 'configuracaocontabem', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'configuracoesfluxodecaixa', 'configuracaofluxodecaixa', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'configuracoestextos', 'configuracaotexto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'consolidacoes', 'consolidacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'consolidacoescontas', 'consolidacaoconta', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'consolidacoesempresas', 'consolidacaoempresa', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'contas', 'conta', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'contasanuais', 'contaanual', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'contascontasreferenciais', 'contacontareferencial', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'contasreferenciais', 'contareferencial', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'dmplcelulas', 'dmplcelula', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'dmplcontas', 'dmplconta', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'dmpllancamentos', 'dmpllancamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'dmpllinhas', 'dmpllinha', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'empresasexercicios', 'empresaexercicio', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'exercicios', 'exercicio', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'extratosbancarios', 'lancamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'formulasfinanceiras', 'formula', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'lalurcalculos', 'lalurapuracao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'lalurparteacontasrelacionadas', 'lalurparteacontarelacionada', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'lalurpartealancamentos', 'lalurpartealancamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'lalurpartebcontas', 'lalurpartebconta', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'lalurparteblancamentos', 'lalurparteblancamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'lancamentos', 'lancamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'lancamentosabertos', 'lancamentoaberto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'lancamentosbloqueios', 'lancamentobloqueio', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'lancamentosnumeros', 'lancamentonumero', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'lancamentospadrao', 'lancamentopadrao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'lotes', 'lote', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'loteslancamentos', 'lancamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'loteslancamentosabertos', 'lotelancamentoaberto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'loteslancamentosnumeros', 'lotelancamentonumero', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'notasexplicativas', 'notaexplicativa', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'orcamentos', 'orcamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'saldos', 'saldo', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'signatarios', 'signatario', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'spedpendencias', 'spedpendencia', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'vwcontas_cache', NULL, false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabil', 'vwcontasanaliticas_cache', NULL, false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'comportamentos', 'comportamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'comportamentosobjetos', 'comportamentoobjeto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'contabilizacaorubricas', 'contabilizacaorubrica', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'contabilizacoes', 'contabilizacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'dadosusuarios', 'dadousuario', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'dirty_comportamentos', 'dirty_comportamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'excecoesacoes', 'excecaoacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'fatos', 'fato', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'gruposopcoes', 'opcao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'lancamentoscontabeis', 'lancamentocontabil', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'lancamentoscontabilizacao', 'lancamentocontabilizacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'lancamentosfatos', 'lancamentofato', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'lotes', 'lote', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'participantescontas', 'participanteconta', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'participantescontasvalores', 'participantecontavalor', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'pendencias', 'pendencia', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'processamentosfatos', 'processamentofato', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('contabilizacao', 'sumario_contabilizacoes', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ecf', 'campos', 'campo', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ecf', 'configcampos', 'configcampo', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ecf', 'ecfs', 'ecf', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ecf', 'empresasconfigs', 'empresaconfig', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ecf', 'registros', 'registro', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('esocial', 'eventos', 'evento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('esocial', 'eventostotalizadores', 'eventototalizador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('esocial', 'lotes', 'lote', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('esocial', 'loteseventos', 'loteevento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('esocial', 'ocorrencias', 'ocorrencia', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('esocial', 'recibos', 'recibo', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('esocial', 'retornos', 'retorno', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'beneficios_fiscais', 'beneficio_fiscal', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'figurastributariastemplates', 'figuratributariatemplate', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'inv_ajustes', 'inv_ajuste', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'inv_contagens', 'inv_contagem', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'inv_contagensitens', 'inv_contagemitem', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'inv_itens', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'inventario', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'itens', 'id', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'itens_mov', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'locaisdeestoques', 'localdeestoque', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'locaisdeestoquesenderecos', 'localdeestoqueendereco', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'ordproducao', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'produtos', 'produto', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'produtos_precos_custos_estabelecimentos', 'produto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'produtosenderecos', 'produtoendereco', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'saldosempresas', 'saldoempresa', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'saldosestabelecimentos', 'saldoestabelecimento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'saldoslocaisdeestoques', 'saldolocaldeestoque', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'sumario_saida_mes_quantidade', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'sumario_saida_mes_valor', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'sumario_saida_semana_quantidade', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'sumario_saida_semana_valor', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('estoque', 'unidades', 'unidade', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('financas', 'baixas', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('financas', 'contas', 'conta', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('financas', 'contasfornecedores', 'contafornecedor', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('financas', 'contasperfisusuario', 'contaperfisusuario', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('financas', 'filaprocessamentofluxocaixa', NULL, false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('financas', 'lancamentoscontas', 'lancamentoconta', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('financas', 'titulos', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('locacoes', 'grupo_ativos_estabelecimentos_itens', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'bens', 'bem', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'cartasdecorrecoes', 'cartadecorrecao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'centrosderesultadoestabelecimento', 'centroresultadoestabelecimento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'configuracoes', 'configuracao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'configuracoesemails', 'configuracaoemail', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'configuracoesordenspagamentos', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'conjuntosclientes', 'conjuntocliente', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'conjuntosfichas', 'conjuntoficha', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'conjuntosfornecedores', 'conjuntofornecedor', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'conjuntosprodutos', 'conjuntoproduto', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'conjuntosrubricas', 'conjuntorubrica', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'conjuntostransportadoras', 'conjuntotransportador', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'conjuntosunidades', 'conjuntounidade', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'contabilizacoescampos', 'contabilizacaocampo', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'contabilizacoescamposvalores', 'contabilizacaocampovalor', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'contabilizacoesfatos', 'contabilizacaofato', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'contabilizacoesgrupos', 'contabilizacaogrupo', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'contabilizacoeslancamentos', 'contabilizacaolancamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'df_docfis', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'df_formapagamentos', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'df_itens', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'df_linhas', 'df_linha', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'df_linhas_impostos', 'df_linha_imposto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'df_servicos', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'dipjempresas', 'dipjempresa', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'empresas', 'empresa', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'empresasacessosusuarios', 'empresaacessousuario', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'empresascadastros', 'empresacadastro', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'empresascarteirasclientes', 'empresacarteiracliente', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'enderecos', 'endereco', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'estabelecimentos', 'estabelecimento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'estabelecimentoscadastros', 'estabelecimentocadastro', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'estabelecimentosconjuntos', 'estabelecimentoconjunto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'fechamentos', 'fechamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'feriados', 'feriado', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'inscricoesestaduaisestabelecimentos', 'inscricaoestadualestabelecimento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'pessoas', 'id', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'qualificacoespj', 'qualificacaopj', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'relatoriospath', 'relatoriopath', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'series', 'serie', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'socios', 'socio', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'sociosparticipacoes', 'socioparticipacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'telefones', 'id', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ns', 'valoresdefaultcontabilizacoes', 'valordefaultcontabilizacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'acordosdeprorrogacoes', 'acordodeprorrogacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'acordosdeprorrogacoesfaixas', 'acordodeprorrogacaofaixa', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'acordosmp9362020', 'acordomp9362020', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'acordosmp9362020trabalhadores', 'acordomp9362020trabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'admissoespreliminares', 'admissaopreliminar', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'afastamentostrabalhadores', 'afastamentotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'agentescausadorescatstrabalhadores', 'agentecausadorcattrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'ambientes', 'ambiente', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'aquisicaoproducao', 'aquisicaoproducao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'asostrabalhadores', 'asotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'atividadescondicoesambientestrabalho', 'atividadecondicaoambientetrabalho', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'avisosferiastrabalhadores', 'avisoferiastrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'avisospreviostrabalhadores', 'avisopreviotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'calculostrabalhadores', 'calculotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'camposespeciais', 'campoespecial', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'camposlayoutsimportacoes', 'campolayoutimportacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'cargos', 'cargo', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'catstrabalhadores', 'cattrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'codigosexternosevento', 'codigoexternoevento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'codigosexternostrabalhadores', 'codigoexternotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'codigossefipgpsestabelecimentos', 'codigosefipgpsestabelecimento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'comercializacaoproducao', 'comercializacaoproducao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'condicoesambientestrabalho', 'condicaoambientetrabalho', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'configuracoesordemcalculomovimentos', 'configuracaoordemcalculomovimento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'configuracoesordemcalculomovimentosponto', 'configuracaoordemcalculomovimentoponto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'contascorrentespagadoras', 'contacorrentepagadora', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'convocacoestrabalhadores', 'convocacaotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'darftrabalhadores', 'darftrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'departamentos', 'departamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'dependentestrabalhadores', 'dependentetrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'detalhamentoscalculostrabalhadores', 'detalhamentocalculotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'dispensavalestransportestrabalhadores', 'dispensavaletransportetrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'documentoscolaboradores', 'documentocolaborador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'documentosdependentescolaboradores', 'documentodependentecolaborador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'documentosregrascolaboradores', 'documentoregracolaborador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'emprestimostrabalhadores', 'emprestimotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'escalasfolgastrabalhadores', 'escalafolgatrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'eventos', 'evento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'examesasostrabalhadores', 'exameasotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'examestoxicologicostrabalhadores', 'exametoxicologicotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'faltastrabalhadores', 'faltatrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'fatoresriscoscondicoesambientestrabalho', 'fatorriscocondicaoambientetrabalho', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'fechamentosfolhas', 'fechamentofolha', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'fechamentosfolhasestabelecimentos', 'fechamentofolhaestabelecimento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'grrftrabalhadores', 'grrftrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'guiasprevidenciasocialdepartamentos', 'guiaprevidenciasocialdepartamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'guiasprevidenciasocialempresas', 'guiaprevidenciasocialempresa', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'guiasprevidenciasocialempresastrabalhadores', 'guiaprevidenciaocialempresatrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'guiassefip', 'guiasefip', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'guiassefiptrabalhadores', 'guiasefiptrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'historicosgps', 'historicogps', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'historicosgpsestabelecimentos', 'historicogpsestabelecimento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'historicostrabalhadores', 'historicotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'horarios', 'horario', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'horariosespeciais', 'horarioespecial', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'instituicoesestabelecimentos', 'instituicaoestabelecimento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'intervalosjornadas', 'intervalojornada', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'jornadas', 'jornada', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'layoutsimportacoes', 'layoutimportacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'layoutsrelatoriosempresa', 'layoutrelatorioempresa', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'lotacoes', 'lotacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'membroscipa', 'membrocipa', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'movimentos', 'movimento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'movimentosponto', 'movimentoponto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'mudancastrabalhadores', 'mudancatrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'niveiscargos', 'nivelcargo', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'outrosrecebimentostrabalhadores', 'outrorecebimentotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'parcelasemprestimostrabalhadores', 'parcelaemprestimotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'partesatingidascatstrabalhadores', 'parteatingidacattrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'pendenciaspagamentos', 'pendenciapagamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'planossaude', 'planosaude', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'planossaudedependentestrabalhadores', 'planosaudedependentetrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'planossauderubricas', 'planosauderubrica', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'planossaudetrabalhadores', 'planosaudetrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'processos', 'processo', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'processoslotacoes', 'processolotacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'processosrubricas', 'processorubrica', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'processossuspensoes', 'processosuspensao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'provisoes13', 'provisao13', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'provisoes13trabalhadores', 'provisao13trabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'provisoesferias', 'provisaoferias', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'provisoesferiastrabalhadores', 'provisaoferiastrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'rateioterceiros', 'rateioterceiro', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'reajustestrabalhadores', 'reajustetrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'receitasdesportivas', 'receitadesportiva', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'relatoriosgravadosempresas', 'relatoriogravadoempresa', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'relatoriosliberados', 'relatorioliberado', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'responsaveisregistrocondicoesambientestrabalho', 'responsavelcondicaoambientetrabalho', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'responsaveisregistrosambientaistrabalhadores', 'responsavelregistroambientaltrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'rubricasponto', 'rubricaponto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'salariosliquidos', 'salarioliquido', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'salariosliquidostotais', 'salarioliquidototal', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'salariosliquidostotaistrabalhadores', 'salarioliquidototaltrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'salariosliquidostrabalhadores', 'salarioliquidotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'tarifasconcessionariasvtstrabalhadores', 'tarifaconcessionariavttrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'tiposfuncionarios', 'tipofuncionario', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'trabalhadores', 'trabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'treinamentoscapacitacoestrabalhadores', 'treinamentocapacitacaotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'treinamentoscapacitacoestrabalhadoresdetalhes', 'treinamentocapacitacaotrabalhadordetalhe', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('persona', 'valestransportespersonalizadostrabalhadores', 'valetransportepersonalizadotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ponto', 'ajustes', 'ajuste', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ponto', 'apuracoesponto', 'apuracaoponto', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ponto', 'historicos', 'historico', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ponto', 'lancamentos', 'lancamento', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ponto', 'marcacoes', 'marcacao', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ponto', 'pendenciascalculostrabalhadores', 'pendenciacalculotrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('ponto', 'saidasantecipadascompensaveistrabalhadores', 'saidaantecipadacompensaveltrabalhador', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'apuracao', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'apuracao_sped', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'apuracao_va', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'bens_ciap', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'bens_grupos', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'bens_movimentos', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'cfg_bases', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'cfg_cfop', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'cfg_imposto', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'cfgempresa', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'cfgestab', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'cprb_contab', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'df_docref', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'df_lancpc', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'df_nottra', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'ecf', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'ecf_cro', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'ecf_mr', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'ecf_pg', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'ecf_rz', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'ecf_rz_contabil', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'ecf_rzcf', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'ecf_rzitens', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'ecf_rzpg', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'ecf_rztp', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'ecf_tp', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'feef', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'gnre_codigosprodutos', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'gnre_dados', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'grec_cfg', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'grec_darf', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'grec_gnre', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'grec_icms_iss', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'grec_resumo', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'imovel_contrato', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'imovel_empreendimento', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'inv_contas', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'itensfor', 'id', true, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'lanaju', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'lf_itens', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'lf_lanfis', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'lf_servicos', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'od_gruout', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'od_outdoc', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'od_tipout', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'pc_cred_lanc', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'pc_credito', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'pc_diferimento', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'pendencias', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'perfilimp_config_estoque', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'processo', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'regesp', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'regesp_ajuste', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'regesp_cfop', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'regesp_lanc', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'saldocredor', 'saldo', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sn_cfg', NULL, false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_contab', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_custo', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_defcontas', 'ig', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_ecf', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_ecf_receitas', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_ecf_retencoes', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_pc', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_pc_c100', 'id_uuid', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_pc_c175', 'id_uuid', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_pc_contab', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_pcr', 'id', false, false);
INSERT INTO exclusao.entidades
(schema_name, table_name, pk_name, apenas_modo_contabil, pular)
VALUES('scritta', 'sped_planocontas', 'id', false, false);
"""

CRIAR_TABELA_ENTIDADES_DEPENDENCIAS = """
CREATE TABLE exclusao.entidades_dependencias (
	schema_name_origem varchar(50) NULL,
	table_name_origem varchar(100) NULL,
	schema_name_destino varchar(50) NULL,
	table_name_destino varchar(100) NULL,
	fk_column varchar(255) NULL
);


INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'acordoscompras', 'ns', 'pessoas', 'fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'acordoscomprasitens', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'acordoscomprasitens', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'associacoesitensnotas', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'associacoesitensnotas', 'ns', 'df_docfis', 'id_docorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'associacoesitensnotas', 'ns', 'df_linhas', 'id_linhadocreferenciado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'atendimentositens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'atendimentositens', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'atendimentositens', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'atendimentositens', 'estoque', 'produtos', 'produto_selecionado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'atendimentositens', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'atendimentositens', 'estoque', 'unidades', 'unidade_selecionada');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'atendimentositens', 'ns', 'df_docfis', 'pedidocompra');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'atendimentositens', 'ns', 'df_docfis', 'pedidoservico');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'atendimentositens', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'atendimentositens', 'ns', 'pessoas', 'fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'negociacoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'negociacoesfornecedores', 'ns', 'pessoas', 'fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'negociacoesitens', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'negociacoesitens', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'negociacoesvalores', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'pedidosgerenciais', 'ns', 'empresas', 'empresaemitente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'pedidosgerenciais', 'ns', 'pessoas', 'fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'pedidosgerenciais_distribuicoes', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'pedidosgerenciais_distribuicoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'propostascotacoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'propostascotacoes', 'ns', 'pessoas', 'fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'requisicoescompras', 'estoque', 'locaisdeestoques', 'localestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'requisicoescompras', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'requisicoesfornecedores', 'ns', 'pessoas', 'fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'solicitacoesprodutosservicos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'solicitacoesprodutosservicos', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('compras', 'vinculositenscompras', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensajustessaldos', 'contabil', 'contas', 'contabem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensajustessaldos', 'contabil', 'contas', 'contaredutora');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'benscontabilizacoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensdadosfiscais', 'ns', 'bens', 'bem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensdadosfiscais', 'ns', 'pessoas', 'fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensexercicios', 'contabil', 'contas', 'contacofins');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensexercicios', 'contabil', 'contas', 'contapis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensexercicios', 'ns', 'bens', 'bem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'benshistoricos', 'ns', 'bens', 'bem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensocorrencias', 'contabil', 'bensocorrencias', 'ocorrenciadeorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensocorrencias', 'contabil', 'centrosdecusto', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensocorrencias', 'contabil', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensocorrencias', 'contabil', 'contas', 'contacreditoir');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensocorrencias', 'contabil', 'contas', 'contadebitoir');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensocorrencias', 'ns', 'bens', 'bem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensocorrencias', 'ns', 'bens', 'bemincorporado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'bensparalisacoes', 'ns', 'bens', 'bem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'camposformulasfinanceiras', 'contabil', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'camposformulasfinanceiras', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'centrosdecusto', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'centrosdecustoanuais', 'contabil', 'centrosdecusto', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'centrosdecustoidiomas', 'contabil', 'centrosdecustoanuais', 'centrodecustoanual');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'classificacaocontas', 'contabil', 'contasanuais', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'classificacaocontas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'classificacaocontasdetalhes', 'contabil', 'classificacaocontas', 'classificacaoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'classificacaocontasdetalhes', 'contabil', 'contasanuais', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'conciliacao', 'contabil', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'conciliacao', 'contabil', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'conciliacoescomentarios', 'contabil', 'lancamentos', 'lancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'conciliacoesimplantacoessaldo', 'contabil', 'centrosdecusto', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'conciliacoesimplantacoessaldo', 'contabil', 'contasanuais', 'contrapartida');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'conciliacoesimplantacoessaldo', 'contabil', 'lancamentos', 'lancamentoimplantacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'conciliacoespordia', 'contabil', 'contasanuais', 'contaanual');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoescontasbens', 'contabil', 'contas', 'contabem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoescontasbens', 'contabil', 'contas', 'contacofinsretencao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoescontasbens', 'contabil', 'contas', 'contadespesa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoescontasbens', 'contabil', 'contas', 'contapisretencao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoescontasbens', 'contabil', 'contas', 'contaredutora');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoesdmpl', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoesfluxodecaixa', 'contabil', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoesfluxodecaixa', 'contabil', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoesfluxodecaixa', 'contabil', 'contas', 'contrapartida');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoesfluxodecaixa', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoesfluxodecaixa', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'configuracoestextos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'consolidacoes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'consolidacoescontas', 'contabil', 'consolidacoes', 'consolidacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'consolidacoescontasvinculos', 'contabil', 'consolidacoescontas', 'consolidacaoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'consolidacoescontasvinculos', 'contabil', 'consolidacoesempresas', 'consolidacaoempresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'consolidacoescontasvinculos', 'contabil', 'contasanuais', 'contaanual');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'consolidacoeseliminacoes', 'contabil', 'consolidacoescontas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'consolidacoeseliminacoes', 'contabil', 'consolidacoescontas', 'contacontrapartida');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'consolidacoeseliminacoes', 'ns', 'empresas', 'empresaa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'consolidacoeseliminacoes', 'ns', 'empresas', 'empresab');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'consolidacoesempresas', 'contabil', 'consolidacoes', 'consolidacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'consolidacoesempresas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contasanteriores', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contasanterioresvinculo', 'contabil', 'contasanuais', 'contaatual');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contasanuais', 'contabil', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contasauxiliareslancamentos', 'contabil', 'lancamentos', 'lancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contasauxiliaresloteslancamentos', 'contabil', 'loteslancamentos', 'lancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contascontasauxiliares', 'contabil', 'contasanuais', 'contaanual');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contascontasreferenciais', 'contabil', 'contasanuais', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contascontasreferenciais', 'contabil', 'contasreferenciais', 'contareferencial');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contascontasreferenciaisfcont', 'contabil', 'contasanuais', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contascontasreferenciaisfcont', 'contabil', 'contasreferenciais', 'contareferencial');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contasidiomas', 'contabil', 'contasanuais', 'contaanual');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contasreferenciais', 'contabil', 'contasreferenciais', 'mae');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contasvinculos', 'contabil', 'contas', 'contaanterior');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'contasvinculos', 'contabil', 'contas', 'contanova');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'cooperativasrateios', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'deparaextratobancario', 'contabil', 'centrosdecustoanuais', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'deparaextratobancario', 'contabil', 'contasanuais', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'deparaextratobancario', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'dmplcelulas', 'contabil', 'dmpllinhas', 'dmpllinha');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'dmplcelulas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'dmplcontas', 'contabil', 'contasanuais', 'contaanual');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'dmplcontas', 'contabil', 'dmplcelulas', 'dmplcelula');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'dmpllancamentos', 'contabil', 'contasanuais', 'contaanual');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'dmpllancamentos', 'contabil', 'dmplcelulas', 'dmplcelula');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'dmpllancamentos', 'contabil', 'lancamentos', 'lancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'dmpllinhas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'empresasexercicios', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'estadosorcamentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'exercicios', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'extratosbancarios', 'contabil', 'centrosdecustoanuais', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'extratosbancarios', 'contabil', 'contasanuais', 'contacredito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'extratosbancarios', 'contabil', 'contasanuais', 'contadebito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'extratosbancarios', 'contabil', 'lotes', 'lote');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'extratosbancarios', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'extratosbancarios', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'formulasfinanceiras', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'identificacoesrelacionamentos', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'itemconciliacaolancamento', 'contabil', 'conciliacao', 'conciliacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'itemconciliacaolancamento', 'contabil', 'lancamentos', 'lancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'itemconciliacaolancamento', 'contabil', 'lancamentos', 'lancamentoimplantacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurcalculos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurparteacontasrelacionadas', 'contabil', 'centrosdecustoanuais', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurparteacontasrelacionadas', 'contabil', 'contasanuais', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurparteacontasrelacionadas', 'contabil', 'contasanuais', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurparteacontasrelacionadas', 'contabil', 'lalurpartealancamentos', 'lalurpartealancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurparteacontasrelacionadas', 'contabil', 'lalurpartealancamentos', 'lalurpartealancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurparteacontasrelacionadas', 'contabil', 'lancamentos', 'lancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurpartealancamentos', 'contabil', 'lancamentos', 'lancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurpartealancamentos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurpartebcontas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurparteblancamentos', 'contabil', 'lalurpartealancamentos', 'lalurpartealancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurparteblancamentos', 'contabil', 'lalurpartebcontas', 'contrapartida');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurparteblancamentos', 'contabil', 'lalurpartebcontas', 'lalurpartebconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurprocessos', 'contabil', 'lalurpartealancamentos', 'lalurpartealancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lalurprocessos', 'contabil', 'lalurparteblancamentos', 'lalurparteblancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentos', 'contabil', 'benscontabilizacoes', 'contabilizacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentos', 'contabil', 'bensocorrencias', 'bemocorrencia');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentos', 'contabil', 'centrosdecustoanuais', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentos', 'contabil', 'contasanuais', 'contacredito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentos', 'contabil', 'contasanuais', 'contadebito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentos', 'contabil', 'lotes', 'lote');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentos', 'contabil', 'loteslancamentos', 'lotelancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentos', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentosabertos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentosabertos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentosbloqueios', 'contabil', 'contasanuais', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentosbloqueios', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentosnumeros', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentospadrao', 'contabil', 'centrosdecusto', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentospadrao', 'contabil', 'contas', 'credito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentospadrao', 'contabil', 'contas', 'debito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lancamentospadrao', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lotes', 'contabil', 'contasanuais', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lotes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'lotes', 'ns', 'estabelecimentos', 'estabelecimentoliberado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentos', 'contabil', 'benscontabilizacoes', 'contabilizacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentos', 'contabil', 'bensocorrencias', 'bemocorrencia');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentos', 'contabil', 'centrosdecustoanuais', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentos', 'contabil', 'contasanuais', 'contacredito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentos', 'contabil', 'contasanuais', 'contadebito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentos', 'contabil', 'lotes', 'lote');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentos', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentosabertos', 'contabil', 'lotes', 'lote');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentosabertos', 'contabil', 'lotes', 'lote');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentosabertos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentosabertos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentosnumeros', 'contabil', 'lotes', 'lote');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'loteslancamentosnumeros', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'movimentacoesorcamentos', 'contabil', 'centrosdecusto', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'movimentacoesorcamentos', 'contabil', 'contasanuais', 'contaanual');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'movimentacoesorcamentos', 'contabil', 'contasanuais', 'contrapartida');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'movimentacoesorcamentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'notasexplicativas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'notasexplicativascontas', 'contabil', 'contasanuais', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'notasexplicativascontas', 'contabil', 'notasexplicativas', 'notaexplicativa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'notasexplicativascontas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'notasexplicativascontas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'orcamentos', 'contabil', 'centrosdecusto', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'orcamentos', 'contabil', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'orcamentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'orcamentosbloqueios', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'planosauxiliares', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'saldos', 'contabil', 'centrosdecusto', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'saldos', 'contabil', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'saldos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'signatarios', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'situacoesespeciais', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'sociosproventos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'sociosproventos', 'ns', 'socios', 'socio');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'spedpendencias', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabil', 'spedpendencias', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'codigosexternos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'comportamentos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'comportamentosobjetos', 'contabilizacao', 'comportamentos', 'comportamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'comportamentosobjetos', 'contabilizacao', 'comportamentosobjetos', 'comportamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacaorubricas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacaorubricas', 'persona', 'eventos', 'rubrica');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'contabil', 'lotes', 'lote');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'contabilizacao', 'processamentosfatos', 'processamentofato');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'financas', 'baixas', 'baixa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'financas', 'lancamentoscontas', 'lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'ns', 'df_docfis', 'docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'persona', 'grrftrabalhadores', 'grrftrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'persona', 'guiassefip', 'guiasefip');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'persona', 'provisoes13', 'provisao13');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'persona', 'provisoesferias', 'provisaoferias');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'scritta', 'ecf_rz', 'ecfrz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contabilizacoes', 'scritta', 'od_outdoc', 'outdoc');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contascorrentes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'contasporcontacorrente', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'copiasdepara', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'dadosusuarios', 'contabilizacao', 'contabilizacaorubricas', 'contabilizacaorubrica');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'dadosusuarios', 'contabilizacao', 'lancamentosfatos', 'lancamentofato');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'dadosusuarios', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'dadosusuarios', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'dadosusuarioscentrosdecustos', 'contabil', 'centrosdecusto', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'dadosusuarioscentrosdecustos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'dirty_comportamentos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'estabelecimentosdepara', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'excecoesacoes', 'contabilizacao', 'comportamentos', 'comportamentoobjeto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'excecoesacoes', 'contabilizacao', 'comportamentosobjetos', 'comportamentoobjeto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'fatos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'lancamentoscentrodecusto', 'contabilizacao', 'lancamentoscontabilizacao', 'lancamentocontabilizacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'lancamentoscontabeis', 'contabilizacao', 'contabilizacoes', 'contabilizacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'lancamentoscontabeis', 'contabilizacao', 'processamentosfatos', 'processamentofato');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'lancamentoscontabilizacao', 'persona', 'guiasprevidenciasocialempresastrabalhadores', 'guiaprevidenciasocialempresatrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'lancamentoscontabilizacao', 'persona', 'guiassefiptrabalhadores', 'guiasefiptrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'lancamentoscontabilizacao', 'persona', 'provisoes13trabalhadores', 'provisao13trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'lancamentoscontabilizacao', 'persona', 'provisoesferiastrabalhadores', 'provisaoferiastrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'lancamentosfatos', 'contabilizacao', 'fatos', 'fato');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'lotes', 'contabilizacao', 'processamentosfatos', 'processamentofato');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'lotes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'participantescontas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'participantescontas', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'participantescontasvalores', 'contabilizacao', 'participantescontas', 'participanteconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'pendencias', 'contabilizacao', 'contabilizacaorubricas', 'contabilizacaorubrica');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'pendencias', 'contabilizacao', 'contabilizacoes', 'contabilizacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'pendencias', 'contabilizacao', 'lancamentosfatos', 'id_lancamentofato');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'pendencias', 'contabilizacao', 'processamentosfatos', 'processamentofato');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'pendencias', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'pendencias', 'persona', 'eventos', 'rubrica');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'pendencias', 'persona', 'provisoes13', 'provisao13');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'pendencias', 'persona', 'provisoesferias', 'provisaoferias');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'sumario_contabilizacoes', 'contabilizacao', 'contabilizacoes', 'contabilizacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('contabilizacao', 'sumario_contabilizacoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'agendamentosvisitas', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'antecipacaocomissao', 'financas', 'titulos', 'tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'antecipacaocomissao', 'ns', 'df_docfis', 'id_docfis_pedido');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'codigos_capitulos_clientes', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'comissoesprodutosvigencia', 'estoque', 'itens', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'comissoesvendedoresregimes', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'condicoesdeentrega', 'ns', 'pessoas', 'transportadora');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'contratostecnicos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'contratostecnicos', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'devolucoesservicos', 'ns', 'df_docfis', 'id_docfis_pedido');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'docpropostas', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'docpropostas', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'extratoscomissoes', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'faixasbonificacoes', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'faturamentosperiodoscomissoes', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'historicospadrao', 'ns', 'pessoas', 'cliente_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'historicosqualificacoes', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'itensdevolucoesservicos', 'ns', 'df_servicos', 'id_dfservicos_itempedido');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'itensdocpropostas', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'itensdocpropostas', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'listascontatos_itensfixos', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'metas_vendedores', 'ns', 'pessoas', 'id_vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'negocios', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'negocios', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'negocios', 'ns', 'pessoas', 'vendedor_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'negociosoperacoes', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'negociospropostas', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'negociospropostas_objetosservicos', 'ns', 'enderecos', 'id_endereco_retirada');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'negociospropostasosvisitas', 'ns', 'pessoas', 'id_tecnico');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'negociospropostaspagamentosblocos', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'negociospropostasvendedores', 'ns', 'pessoas', 'id_vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'negociostotalizadores', 'ns', 'pessoas', 'id_vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'old_propostas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'old_propostas', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'old_propostasporvendedores', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'oportunidades', 'ns', 'pessoas', 'participante_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'oportunidades', 'ns', 'pessoas', 'participante_vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'oportunidadesitens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'oportunidadesitens', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'oportunidadesprodutos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'pagamentoscomissoes', 'financas', 'titulos', 'tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'pagamentoscomissoes', 'ns', 'df_docfis', 'id_docfis_pedido');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'pagamentoscomissoes', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'pagamentoscomissoesitens', 'financas', 'titulos', 'id_tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'pagamentoscomissoesitens', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'pagamentoscomissoesitens', 'ns', 'df_itens', 'id_df_itens');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'proximoscontatos', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'resumopagamentoscomissoes', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'resumovendasapuradas', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'tabelas_de_precos', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'ufestabelecimentogeracaocontratos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'vendasapuradas', 'ns', 'df_docfis', 'id_docfis_pedido');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'vendasapuradas', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('crm', 'vouchers', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ecf', 'campos', 'ecf', 'campos', 'campoequivalente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ecf', 'campos', 'ecf', 'registros', 'registro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ecf', 'configcampos', 'ecf', 'campos', 'campo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ecf', 'ecfs', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ecf', 'empresasconfigs', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ecf', 'modelosvalores', 'ecf', 'campos', 'campo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ecf', 'registros', 'ecf', 'registros', 'registropai');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('esocial', 'configuracoesintegracaobrmed', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('esocial', 'controlesacessoseventos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('esocial', 'eventos', 'esocial', 'eventos', 'eventoorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('esocial', 'eventos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('esocial', 'eventostotalizadores', 'esocial', 'retornos', 'retorno');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('esocial', 'loteseventos', 'esocial', 'eventos', 'evento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('esocial', 'loteseventos', 'esocial', 'lotes', 'lote');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('esocial', 'ocorrencias', 'esocial', 'retornos', 'retorno');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('esocial', 'recibos', 'esocial', 'lotes', 'lote');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('esocial', 'retornos', 'esocial', 'loteseventos', 'loteevento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('esocial', 'retornos', 'esocial', 'recibos', 'recibo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'acertosaldo', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'acertosaldo', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'acertosaldoitem', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'acertosaldoitem', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'acordosfornecimentoprodutos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'acordosfornecimentoprodutos', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'acordosfornecimentoprodutositens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'acordosfornecimentoprodutositens', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'apuracoescmv', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'apuracoescmvitens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'apuracoescmvitens', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'beneficiosfiscaisproduto', 'estoque', 'beneficios_fiscais', 'beneficiofiscal');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'beneficiosfiscaisproduto', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'categoriasdeprodutos', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'certificadosdigitais', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'colecoes', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'colecoesprodutos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'complementositensfornecedores', 'scritta', 'itensfor', 'id_itemfor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'config_fracao_estabelecimentos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'config_fracao_estabelecimentos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'config_fracao_estabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'config_saldos_enderecos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'config_saldos_enderecos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'configuracoes_enderecos', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'configuracoes_enderecos', 'estoque', 'locaisdeestoquesenderecos', 'localdeestoqueendereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'configuracoes_enderecos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'configuracoesmdfeempresa', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_emp_quantidade', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_emp_quantidade', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_emp_quantidade', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_emp_valor', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_emp_valor', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_emp_valor', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_est_quantidade', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_est_quantidade', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_est_quantidade', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_est_valor', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_est_valor', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_est_valor', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'curva_abc_proc_local_de_estoque', 'estoque', 'locaisdeestoques', 'id_local_de_estoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'custosintermediarios', 'estoque', 'unidades', 'unidadepadrao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'custosintermediarios', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'devolucoesalmoxarifado', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'devolucoesalmoxarifadoitens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'devolucoesalmoxarifadoitens', 'estoque', 'locaisdeestoques', 'localdeestoque_destino');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'devolucoesalmoxarifadoitens', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'dimensoesgrade', 'estoque', 'produtos', 'id_owner');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'embalagens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'embalagens', 'estoque', 'unidades', 'unidadepadrao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'endereco_niveis', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'entregadores', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'estoque_minimo_proc', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'estoque_minimo_proc_itens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'estoque_minimo_proc_itens', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'fechamentosdeestoque', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'figurastributarias', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'figurastributariastemplates', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'fracoes', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'fracoes', 'estoque', 'locaisdeestoquesenderecos', 'localdeestoqueendereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'fracoes', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'fracoes_movimentacoes', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'fracoes_movimentacoes', 'estoque', 'itens_mov', 'movimentoentrada');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'fracoes_movimentacoes', 'estoque', 'itens_mov', 'movimentosaida');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'fracoes_movimentacoes', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'fracoes_movimentacoes', 'estoque', 'locaisdeestoquesenderecos', 'localdeestoqueendereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'fracoes_movimentacoes', 'ns', 'df_docfis', 'df_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'historicospadroes', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_ajustes', 'estoque', 'inv_contagens', 'inv_contagem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_ajustes', 'estoque', 'inventario', 'inventario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_ajustes', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_ajustes', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_contagens', 'estoque', 'inventario', 'inventario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_contagens', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_contagensitens', 'estoque', 'inv_contagens', 'inv_contagem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_contagensitens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_contagensitenslotes', 'estoque', 'inv_contagensitens', 'inv_contagemitem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_contagensitensnumerosdeserie', 'estoque', 'inv_contagensitens', 'inv_contagemitem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_itens', 'estoque', 'inventario', 'inventario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_itens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_itens', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inv_itens', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'inventario', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens', 'estoque', 'itens', 'id_prodacabado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens', 'estoque', 'unidades', 'unidadetrib');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens', 'ns', 'pessoas', 'id_fabricante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens', 'ns', 'pessoas', 'id_ultimofornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_alteracoes', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_classificacoes_curva_empresa', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_classificacoes_curva_estabelecimento', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_estabelecimentos', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_estabelecimentos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov', 'estoque', 'inventario', 'id_inventario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov', 'estoque', 'ordproducao', 'id_ordpro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov', 'ns', 'df_itens', 'id_itemdocfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov', 'ns', 'pessoas', 'id_proprietario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov', 'scritta', 'ecf_rzitens', 'id_itemrzcf');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov', 'scritta', 'lf_itens', 'id_itemlanfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov_enderecos', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov_enderecos', 'estoque', 'itens_mov', 'itens_mov');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov_enderecos', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov_enderecos', 'estoque', 'locaisdeestoquesenderecos', 'endereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov_enderecos', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itens_mov_enderecos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itensauditorias', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itensauditorias', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itenscodigosdebarras', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itenscodigosdebarras', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itensparacalculosaldo', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itensparacalculosaldo', 'estoque', 'locaisdeestoques', 'id_localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itensparacalculosaldo', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itensparacalculosaldo', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itenstransferencias', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'itenstransferenciasfracoes', 'estoque', 'locaisdeestoquesenderecos', 'endereco_destino_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'limitessaldosprodutos', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'limitessaldosprodutos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'limitessaldosprodutos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'locaisdeestoques', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'locaisdeestoquesenderecos', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'locaisdeestoquesenderecos', 'estoque', 'locaisdeestoquesenderecos', 'localdeestoqueendereco_pai');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'locaisdeestoquesenderecos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'locaisdeestoquesoperacoes', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'locaisdeestoquesoperacoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'mdfes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'metas_bonificacoes', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'metas_produtos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'metas_vendas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'modelostransformacao', 'estoque', 'locaisdeestoques', 'localdeestoque_destino');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'modelostransformacao', 'estoque', 'locaisdeestoques', 'localdeestoque_origem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'modelostransformacaoitens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'motoristas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'operacoes', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ordprod_itens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ordprod_itens', 'estoque', 'ordproducao', 'id_ordem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ordprod_itens', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ordproducao', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'pedidos_bloqueados', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'perfil_importacao', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'perfiltrib_est', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'perfiltrib_fed', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'perfiltrib_fed_unidades_tributarias', 'estoque', 'unidades', 'id_unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'perfiltrib_fed_unidades_tributarias', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'perfiltrib_fed_validades_impostos', 'estoque', 'unidades', 'unidadetributavel_unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'perfiltrib_fed_validades_impostos', 'scritta', 'sped_pc', 'piscofins_sped');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'precos_praticados', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'precos_praticados', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'precos_praticados', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'previsoes_demandas_proc', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'previsoes_demandas_proc_emp_mes', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'previsoes_demandas_proc_emp_mes', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'previsoes_demandas_proc_emp_semana', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'previsoes_demandas_proc_emp_semana', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'previsoes_demandas_proc_local_de_estoque', 'estoque', 'locaisdeestoques', 'id_local_de_estoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_associacao_itens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_associacao_itens', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_enviosrcpe', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_locaisdeestoques_perdasganhos', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_locaisdeestoques_perdasganhos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_locaisdeestoques_producao', 'estoque', 'locaisdeestoques', 'localdeestoqueinsumos');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_locaisdeestoques_producao', 'estoque', 'locaisdeestoques', 'localdeestoqueresultante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_locaisdeestoques_producao', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_modelos_estabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_modelos_itens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_modelos_itens', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_modelos_itens', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_modelos_itens_embalagens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_modelos_processos_estabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_ordensdeproducoes', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_ordensdeproducoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_ordensdeproducoes', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_ordensdeproducoes_itens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_ordensdeproducoes_itens', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_ordensdeproducoes_itens', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_ordensdeproducoes_itens_embalagens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_ordensdeproducoes_itens_embalagens', 'estoque', 'locaisdeestoques', 'id_localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_ordensdeproducoes_itens_relacao_ganhoperda', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_ordensdeproducoes_itens_retirados', 'ns', 'pessoas', 'id_funcionario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_ordensdeproducoes_itens_retirados_detalhes', 'estoque', 'itens', 'item_retirado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'producao_processos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtos', 'estoque', 'unidades', 'unidadedemedida');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtos', 'ns', 'pessoas', 'id_fabricante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtos_precos_custos_estabelecimentos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtos_precos_custos_estabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtoscodigofabricante', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtoscomposicao', 'estoque', 'produtos', 'produtopai');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtoscomposicao', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosconvunidades', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosconvunidades', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosconvunidades', 'estoque', 'unidades', 'unidadepadrao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosembalagens', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosembalagens', 'estoque', 'unidades', 'unidadepadrao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosenderecos', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosenderecos', 'estoque', 'locaisdeestoquesenderecos', 'localdeestoqueendereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosenderecos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosgenericos', 'estoque', 'unidades', 'unidadedemedida');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosgenericosprodutos', 'estoque', 'produtos', 'produtofilho');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosipienquadramentos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtoslotes', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtoslotes', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtoslotes', 'ns', 'df_itens', 'df_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtoslotes', 'ns', 'pessoas', 'fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtoslotesmovimentacoes', 'estoque', 'itens_mov', 'itens_mov');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosnumerosdeserie', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosnumerosdeserie', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'produtosnumerosdeseriedocumentos', 'estoque', 'itens_mov', 'itens_mov');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra', 'ns', 'pessoas', 'id_tecnico');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_itens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_itens', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_itens', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_itens', 'ns', 'df_linhas', 'df_linha');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_itens_enderecos', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_itens_enderecos', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_itens_enderecos', 'estoque', 'locaisdeestoquesenderecos', 'localdeestoqueendereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_itens_fracoes', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_itenslotes', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_itenslotes', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_itenslotes', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'ra_movimentos', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'reajustesprecos', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'romaneios', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'romaneios_entregas', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'romaneios_notas', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'romaneios_notas', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'romaneios_notas_itens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'romaneios_notas_itens', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'romaneios_notas_itens', 'ns', 'df_linhas', 'id_linha');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'rotas_pessoas', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldosempresas', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldosempresas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldosestabelecimentos', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldosestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldoslocaisdeestoques', 'estoque', 'inventario', 'inventario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldoslocaisdeestoques', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldoslocaisdeestoques', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldoslocaisdeestoques', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldoslocaisdeestoquesenderecos', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldoslocaisdeestoquesenderecos', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldoslocaisdeestoquesenderecos', 'estoque', 'locaisdeestoquesenderecos', 'endereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldoslocaisdeestoquesenderecos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldoslotes', 'estoque', 'inventario', 'inventario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldoslotes', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldosloteslocaisdeestoques', 'estoque', 'inventario', 'inventario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldosloteslocaisdeestoques', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldosloteslocaisdeestoques', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldosterceiros', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldosterceiros', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'saldosterceiros', 'ns', 'pessoas', 'terceiro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sugestao_compras_proc', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sugestao_compras_proc_emp_mes', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sugestao_compras_proc_emp_mes', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sugestao_compras_proc_emp_semana', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sugestao_compras_proc_emp_semana', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_mes_quantidade', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_mes_quantidade', 'estoque', 'locaisdeestoques', 'id_local_de_estoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_mes_quantidade', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_mes_quantidade', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_mes_valor', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_mes_valor', 'estoque', 'locaisdeestoques', 'id_local_de_estoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_mes_valor', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_mes_valor', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_semana_quantidade', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_semana_quantidade', 'estoque', 'locaisdeestoques', 'id_local_de_estoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_semana_quantidade', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_semana_quantidade', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_semana_valor', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_semana_valor', 'estoque', 'locaisdeestoques', 'id_local_de_estoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_semana_valor', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'sumario_saida_semana_valor', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'tabelasdefretes', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'tabelasdefretesentidades', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'tabelasdeprecos', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'tabelasdeprecos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'tabelasdeprecos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'tabelasdeprecosdescontosadicionais', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'tabelasdeprecosentidades', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'tabelasdeprecosestabelecimentos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'transferencias', 'estoque', 'locaisdeestoques', 'localdeestoquedestino');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'transferencias', 'estoque', 'locaisdeestoques', 'localdeestoqueorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'transformacoesordensdeproducoesitens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'veiculos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('estoque', 'vinculosipienquadramentos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'adiantamentosbaixaspagar', 'financas', 'baixas', 'baixapagar');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'adiantamentosbaixaspagar', 'financas', 'lancamentoscontas', 'lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'adiantamentosbaixasreceber', 'financas', 'baixas', 'baixareceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'adiantamentosbaixasreceber', 'financas', 'lancamentoscontas', 'lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'adiantamentossaldos', 'financas', 'titulos', 'tituloadiantamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'adiantamentossaldos', 'financas', 'titulos', 'titulonotafiscal');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'administradoreslegais', 'ns', 'pessoas', 'responsavelpf');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'administradoreslegais', 'ns', 'pessoas', 'responsavelpj');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'alteracoescontratos', 'ns', 'df_servicos', 'itemnotacobranca');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'aplicacoes', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'aplicacoes', 'financas', 'lancamentoscontas', 'lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'arquivoremessacheques', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'arquivoremessacheques', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'arquivosremessacredinfar', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'arquivosremessaserasa', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'arquivosretornosbancarios', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'arquivosretornosbancarios', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'arquivosretornosborderos', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'arquivosretornosborderos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'arquivosretornoscustodiascheques', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'arquivosretornoscustodiascheques', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'avisoslancamentos', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'avisoslancamentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'avisostitulos', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'avisostitulos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'baixas', 'financas', 'lancamentoscontas', 'lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'baixas', 'financas', 'titulos', 'id_titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'baixas', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'beneficiarios', 'ns', 'estabelecimentos', 'membrobeneficiario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'beneficiarios', 'ns', 'estabelecimentos', 'membrotitular');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'benspatrimoniais', 'ns', 'estabelecimentos', 'proprietario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'benspatrimoniaisproprietarios', 'ns', 'estabelecimentos', 'proprietario_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'benspatrimoniaisproprietarios', 'ns', 'pessoas', 'proprietario_participante_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'borderoseletronicos', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'borderoseletronicos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'cancelamentosparciaistitulos', 'financas', 'titulos', 'id_titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'cenariosorcamentarios', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'centroscustoslancamentosexternos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'centroscustoslancamentosexternos', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'chequescustodias', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'chequescustodias', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'chequescustodias', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'chequespagamentos', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'chequespagamentos', 'financas', 'contas', 'id_contaexcedente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'chequespagamentos', 'financas', 'lancamentoscontas', 'id_lancamentoexcedente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'chequespagamentos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'classfin_classificacoeslancamentosexternos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'clientesenviadosserasa', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'clienteslotesfaturas', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'conciliacoeslancamentos', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'configuracoescontasinvestimentos', 'financas', 'contas', 'contafinanceira');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'configuracoescontasinvestimentos', 'financas', 'contas', 'containvestimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'configuracoesrateiosinvestimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'configuracoesterceirizacao', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'configuracoesterceirizacao', 'ns', 'pessoas', 'id_fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contas', 'ns', 'estabelecimentos', 'id_estabelecimento_emprestimo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contas', 'ns', 'pessoas', 'id_pessoa_emprestimo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contas', 'persona', 'trabalhadores', 'id_funcionario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contasfornecedores', 'ns', 'pessoas', 'id_fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contasintegracaobancariaapi', 'financas', 'contas', 'idconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contasperfisusuario', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contasperfisusuario', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contratos', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contratos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contratos', 'ns', 'pessoas', 'detentor_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contratos', 'ns', 'pessoas', 'fiador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contratos', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contratos', 'ns', 'pessoas', 'participantecomissao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contratos', 'scritta', 'od_tipout', 'id_tipo_outras_recdesp');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contratos', 'scritta', 'od_tipout', 'id_tipo_outras_recdesplocacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contratoscartoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contratosclientespartilhas', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'contratosvendedores', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'dadosanaliticosfluxocaixa', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'dadosanaliticosfluxocaixa', 'financas', 'lancamentoscontas', 'lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'dadosanaliticosfluxocaixa', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'dadosanaliticosfluxocaixa', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'descontosduplicatas', 'financas', 'lancamentoscontas', 'id_lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'descontosduplicatasitens', 'financas', 'lancamentoscontas', 'id_lancamentoestorno');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'descontosduplicatasitens', 'financas', 'titulos', 'id_tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'descontostitulosreceber', 'financas', 'lancamentoscontas', 'lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'descontostitulosreceber', 'financas', 'titulos', 'tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'despesasmedicas', 'ns', 'estabelecimentos', 'membrofamilia');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'despesasmedicas', 'ns', 'pessoas', 'prestador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'documentosajustesrateios', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'faturas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'faturas', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'formaspagamentoporcontasfinanceiras', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'formaspagamentoporcontasfinanceiras', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'historicoatualizacoesboletobordero', 'financas', 'titulos', 'idtitulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'historicointegracaotitulosapi', 'financas', 'titulos', 'idtitulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'historicostitulos', 'financas', 'titulos', 'id_titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'inadimplenciasexcecoesclientes', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'informacoescartoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'irregularidadesbancarias', 'financas', 'lancamentoscontas', 'lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'irregularidadesbancarias', 'financas', 'titulos', 'tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'irregularidadesportitulos', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itensavisoslancamentos', 'financas', 'lancamentoscontas', 'lancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itensavisostitulos', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itensborderoseletronicos', 'financas', 'contasfornecedores', 'contafornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itensborderoseletronicos', 'financas', 'titulos', 'titulopagar');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itenscenariosorcamentarios', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itenschequescustodiasendossos', 'financas', 'baixas', 'id_baixa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itenschequescustodiasendossos', 'financas', 'titulos', 'id_titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itenschequescustodiasrecebimentos', 'financas', 'baixas', 'id_baixa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itenschequescustodiasrecebimentos', 'financas', 'titulos', 'id_titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itenschequespagamentos', 'financas', 'titulos', 'id_titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itenscobrancas', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itenscobrancas', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itenscobrancasprocessadas', 'financas', 'titulos', 'tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itenscobrancasprocessadas', 'ns', 'df_docfis', 'rps_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itenscontratos', 'scritta', 'od_tipout', 'id_tipo_outras_recdesp');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itensemprestimoprestacoesdecontas', 'financas', 'titulos', 'id_tituloemprestimo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itensfaturas', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itensprestacoesdecontas', 'financas', 'titulos', 'id_titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itensrenegociacoescontratostitulosgerados', 'financas', 'titulos', 'id_tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itensrenegociadoscontratos', 'financas', 'titulos', 'id_tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'itensresgates', 'financas', 'lancamentoscontas', 'lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lancamentosbancarios', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lancamentosconciliados', 'financas', 'lancamentoscontas', 'lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lancamentoscontas', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lancamentoscontas', 'financas', 'lancamentoscontas', 'vinculado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lancamentoscontas', 'financas', 'titulos', 'id_titulo_reembolso');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lancamentoscontas', 'ns', 'estabelecimentos', 'idestabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lancamentoscontas', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lancamentostituloscoberturascontas', 'financas', 'lancamentoscontas', 'idlancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lancamentostituloscoberturascontas', 'financas', 'titulos', 'idtitulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lotesboletosintegracoes', 'financas', 'contas', 'idconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lotesboletosintegracoes', 'ns', 'estabelecimentos', 'idestabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'lotesfaturas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'periodos', 'ns', 'estabelecimentos', 'membrofamilia');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'pix', 'financas', 'contas', 'idconvenio');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'pix', 'financas', 'titulos', 'idtitulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'pix', 'ns', 'pessoas', 'idpessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'prestacoesdecontas', 'financas', 'contas', 'id_contaemprestimo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'prestacoesdecontas', 'financas', 'contas', 'id_contaespecie');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'prestacoesdecontas', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'prestacoesdecontas', 'ns', 'pessoas', 'id_fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'previsoespagar', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'previsoespagar', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'previsoespagar', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'previsoesreceber', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'previsoesreceber', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'previsoesreceber', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'projetos', 'estoque', 'locaisdeestoques', 'localdeestoque_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'projetos', 'ns', 'enderecos', 'endereco_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'projetos', 'ns', 'estabelecimentos', 'estabelecimento_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'projetos', 'ns', 'pessoas', 'cliente_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'projetosclientes', 'ns', 'pessoas', 'cliente_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'projetosfornecedores', 'ns', 'pessoas', 'fornecedor_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'projetosvendedores', 'ns', 'pessoas', 'vendedor_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'rateiosfinanceiros', 'ns', 'estabelecimentos', 'id_estabelecimento_reembolso');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsos', 'financas', 'lancamentoscontas', 'id_lancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsos', 'financas', 'titulos', 'id_titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsos', 'financas', 'titulos', 'id_titulo_reembolsos_pagar');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsos', 'financas', 'titulos', 'id_titulo_reembolsos_receber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsos', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsos', 'persona', 'trabalhadores', 'id_funcionario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsospessoas', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsospessoas', 'financas', 'titulos', 'titulogerado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsospessoas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsospessoas', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsospessoasitens', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'reembolsossolucionados', 'financas', 'lancamentoscontas', 'id_lancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'renegociacoescontratos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'renegociacoescontratos', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'renegociacoestitulos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'renegociacoestitulos', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'resgates', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'retencoestitulosreceber', 'financas', 'titulos', 'tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'retencoestitulosreceber', 'financas', 'titulos', 'tituloreceberretido');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'retencoestitulosreceber', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'saldosreaiscontas', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'taloescheques', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'terceirizacaocobrancas', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'terceirizacaocobrancas', 'ns', 'pessoas', 'id_fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'terceirizacaocobrancasitens', 'financas', 'titulos', 'id_tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'terceirizacaocobrancasitens', 'financas', 'titulos', 'id_tituloreceberadiantamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'financas', 'baixas', 'id_baixaorigem_dimob');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'financas', 'contas', 'id_contaemprestimo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'financas', 'contasfornecedores', 'contafornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'financas', 'titulos', 'id_titulovinculo_previsao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'ns', 'df_docfis', 'id_rps');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'ns', 'pessoas', 'id_pessoa_reembolso');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'scritta', 'grec_darf', 'id_darf');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'scritta', 'grec_gnre', 'id_gnre');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'scritta', 'grec_icms_iss', 'id_icmsiss');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulos', 'scritta', 'od_outdoc', 'id_outdoc');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'tituloscancelados', 'financas', 'baixas', 'id_baixaorigem_dimob');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'tituloscancelados', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'tituloscancelados', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'tituloscancelados', 'ns', 'df_docfis', 'id_rps');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'tituloscancelados', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'tituloscancelados', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'tituloscancelados', 'ns', 'pessoas', 'id_pessoa_reembolso');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'tituloscancelados', 'scritta', 'grec_darf', 'id_darf');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'tituloscancelados', 'scritta', 'grec_icms_iss', 'id_icmsiss');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'tituloscancelados', 'scritta', 'od_outdoc', 'id_outdoc');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulospagarapuradosporguia', 'financas', 'titulos', 'titulopagarapurado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulospagarapuradosporguia', 'financas', 'titulos', 'titulopagargeradoguia');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulospagarapuradosporguia', 'scritta', 'grec_darf', 'id_guia_darf');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulospagarapuradosporguia', 'scritta', 'grec_icms_iss', 'id_guia_iss');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulosreceberestornoscartoes', 'financas', 'lancamentoscontas', 'lancamentoconta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulosreceberestornoscartoes', 'financas', 'titulos', 'tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulosreceberporvendedores', 'financas', 'titulos', 'tituloreceber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'titulosreceberporvendedores', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'transferenciasinvestimentos', 'financas', 'lancamentoscontas', 'lanctoinvestoriginal');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'transferenciasinvestimentos', 'financas', 'lancamentoscontas', 'lanctoinvesttransferencia');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'vendedoresrenegociacoestitulos', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'vinculosestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimentoorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('financas', 'vinculosestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimentovinculado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('integracoes', 'fila_integracao_mm', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('integracoes', 'inventarios_enderecos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('integracoes', 'inventarios_enderecos_itens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('integracoes', 'inventarios_enderecos_itens', 'estoque', 'locaisdeestoquesenderecos', 'endereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('integracoes', 'inventarios_fracoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('integracoes', 'inventarios_fracoes_itens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('integracoes', 'inventarios_fracoes_itens', 'estoque', 'locaisdeestoquesenderecos', 'endereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('locacoes', 'clientesareasnegocios', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('locacoes', 'enviosprodutos', 'estoque', 'produtos', 'produto_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('locacoes', 'grupo_ativos_estabelecimentos_itens', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('locacoes', 'lancamentomultiploativos', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('locacoes', 'lancamentomultiploativos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('locacoes', 'lancamentomultiploativos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('locacoes', 'retornoproduto', 'estoque', 'locaisdeestoques', 'estoque_destino_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('locacoes', 'retornoproduto', 'estoque', 'produtos', 'produto_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('locacoes', 'retornoprodutotrocapeca', 'estoque', 'produtos', 'produto_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoes', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesadiantamentosavulsos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesadiantamentosavulsos', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesadmissoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesadmissoes', 'persona', 'cargos', 'cargo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesadmissoes', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesadmissoes', 'persona', 'horarios', 'horario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesadmissoes', 'persona', 'niveiscargos', 'nivelcargo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesadmissoes', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesalteracoesdadoscadastrais', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesalteracoesdadoscadastrais', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesalteracoesenderecos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesalteracoesenderecos', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesfaltas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesfaltas', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesferias', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesferias', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesrescisoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesrescisoes', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesvtsadicionais', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('meurh', 'solicitacoesvtsadicionais', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'aberturas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'associacoesitensdis', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'associacoesitensdis', 'ns', 'df_docfis', 'id_docorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'associacoesitensdis', 'ns', 'df_linhas', 'id_linhadocorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'contabil', 'centrosdecusto', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'contabil', 'contas', 'contaaquisicao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'contabil', 'contas', 'contacofins');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'contabil', 'contas', 'contapis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'ns', 'bens', 'bemagregador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'ns', 'bens', 'principal');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'ns', 'df_docfis', 'nota');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'ns', 'df_itens', 'itemnota');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'ns', 'pessoas', 'fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'bens', 'scritta', 'bens_grupos', 'grupobem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'cartasdecorrecoes', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'centrosderesultadoestabelecimento', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'configuracoes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'configuracoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'configuracoesemails', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'configuracoesordenspagamentos', 'financas', 'contas', 'id_contacorrente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'configuracoesordenspagamentos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'configuracoesordenspagamentos', 'ns', 'pessoas', 'id_fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'configuracoestrabalhadoresporcentroscustos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'configuracoestrabalhadoresporcentroscustos', 'persona', 'trabalhadores', 'id_trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'configuracoestrabalhadoresporprojetos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'configuracoestrabalhadoresporprojetos', 'persona', 'trabalhadores', 'id_trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'conjuntosclientes', 'ns', 'pessoas', 'registro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'conjuntosfichas', 'ns', 'pessoas', 'registro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'conjuntosfornecedores', 'ns', 'pessoas', 'registro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'conjuntosrepresentantescomerciais', 'ns', 'pessoas', 'registro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'conjuntosrepresentantestecnicos', 'ns', 'pessoas', 'registro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'conjuntosrubricas', 'persona', 'eventos', 'registro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'conjuntostecnicos', 'ns', 'pessoas', 'registro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'conjuntostransportadoras', 'ns', 'pessoas', 'registro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'conjuntosunidades', 'estoque', 'unidades', 'registro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'conjuntosvendedores', 'ns', 'pessoas', 'registro');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contabilizacoesagrupamentos', 'ns', 'contabilizacoesgrupos', 'contabilizacaogrupo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contabilizacoescampos', 'ns', 'contabilizacoesfatos', 'contabilizacaofato');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contabilizacoescampos', 'ns', 'contabilizacoesgrupos', 'contabilizacaogrupo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contabilizacoescamposvalores', 'ns', 'contabilizacoescampos', 'contabilizacaocampo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contabilizacoesfatos', 'ns', 'contabilizacoesgrupos', 'contabilizacaogrupo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contabilizacoeslancamentos', 'ns', 'contabilizacoesfatos', 'contabilizacaofato');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contabilizacoeslancamentos', 'ns', 'contabilizacoesgrupos', 'contabilizacaogrupo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contaspadroes', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contaspadroes', 'financas', 'contas', 'id_contamanutencao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contaspadroes', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contatos', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'contatosemails', 'ns', 'pessoas', 'pessoa_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'convunidades', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'convunidades', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'convunidades', 'estoque', 'unidades', 'unidadepadrao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_ativos', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_autorizados', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_custosextra', 'ns', 'df_docfis', 'cte');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_custosextra', 'ns', 'df_docfis', 'documento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_custosextra_itens', 'ns', 'df_itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_custosextramultinotas', 'ns', 'df_docfis', 'id_documento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'estoque', 'itens', 'id_itemntr');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'estoque', 'locaisdeestoques', 'id_localdeestoquedestino');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'estoque', 'locaisdeestoques', 'id_localdeestoqueorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'df_docfis', 'id_conhectransp');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'df_docfis', 'id_pedidoservico');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'df_docfis', 'rps_original');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'pessoas', 'id_coleta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'pessoas', 'id_consignatario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'pessoas', 'id_entrega');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'pessoas', 'id_motorista');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'pessoas', 'id_operador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'pessoas', 'id_orgao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'pessoas', 'id_redespachador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'pessoas', 'id_remetente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'pessoas', 'id_transportadora');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'ns', 'series', 'id_serie');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_docfis', 'scritta', 'od_tipout', 'id_grupodiferenciado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_enderecos_retiradasentregas', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_enderecos_retiradasentregas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_enderecos_retiradasentregas', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_financeiros', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_formapagamentos', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_formapagamentos_troco', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_fretes', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_fretes', 'ns', 'pessoas', 'id_transportadora');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_fretes_reboques', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_fretes_volumes', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens', 'ns', 'pessoas', 'id_proprietario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens', 'ns', 'pessoas', 'id_receptor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens', 'ns', 'pessoas', 'id_vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens_enderecos', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens_enderecos', 'estoque', 'locaisdeestoquesenderecos', 'localdeestoqueendereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens_enderecos', 'ns', 'df_linhas', 'df_linha');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens_fracoes', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens_fracoes', 'estoque', 'locaisdeestoquesenderecos', 'localdeestoqueendereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens_fracoes', 'ns', 'df_linhas', 'df_linha');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens_producao', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens_producao', 'ns', 'df_docfis', 'docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itens_producao', 'ns', 'df_linhas', 'linha');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itensdrawback', 'ns', 'df_linhas', 'id_linha');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itenslotes', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_itensnumerosdeseries', 'ns', 'df_itens', 'df_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_linhas', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_linhas', 'estoque', 'locaisdeestoques', 'id_localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_linhas', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_linhas', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_linhas', 'ns', 'df_linhas', 'df_linha_origem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_linhas', 'ns', 'df_linhas', 'id_linha_docfis_origem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_linhas', 'REFERENCES', 'ns', 'KEY');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_linhas_impostos', 'ns', 'df_linhas', 'df_linha');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_pagamentos', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_parcelas', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_referencias', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_servicos', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_servicos', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_servicos', 'ns', 'df_docfis', 'id_notadeducao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_servicos', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_vendedores', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'df_vendedores', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'di', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'di', 'ns', 'pessoas', 'fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'di_adicoes_itens', 'estoque', 'produtos', 'id_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'di_adicoes_itens', 'estoque', 'unidades', 'id_unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'di_docfis', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'dipjempresas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'dipjformulas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'documentosgeddetalhes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'documentosgeddetalhes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'emailsalternativos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'empresasacessosusuarios', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'empresascadastros', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'empresascarteirasclientes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'enderecos', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentos', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentos', 'persona', 'processos', 'processoaprendiz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentos', 'persona', 'processos', 'processocontratacaopcd');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentos', 'persona', 'processos', 'processofap');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentos', 'persona', 'processos', 'processorat');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentos', 'persona', 'trabalhadores', 'gestor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentosacessosusuarios', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentosassociados', 'ns', 'estabelecimentos', 'associado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentosassociados', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentoscadastros', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentoscfops', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentosconjuntos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentospessoas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentospessoas', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'estabelecimentoterceiros_lcdpr', 'ns', 'estabelecimentos', 'idestabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'fechamentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'fechamentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'feriados', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'feriados', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'feriados', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'filaemails', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'followups', 'ns', 'df_docfis', 'ordemservico');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'followups', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'formaspagamentoscontas', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'formaspagamentoscontas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'importacaoatividadesconferenciasentradas', 'ns', 'df_linhas', 'id_linha_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'importacaonotas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'importacaonotas', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'importacaonotas', 'scritta', 'od_tipout', 'id_grupodiferenciado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'importacoes_dados_lcdpr', 'ns', 'empresas', 'idempresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'importacoes_dados_lcdpr', 'ns', 'estabelecimentos', 'idestabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'incidenciaimpostosestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'inscricoesestaduais', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'inscricoesestaduaisestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'limitesdecreditoshistoricos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'limitesdecreditoshistoricos', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'locaisdeuso', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'locaisdeuso', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'numeros_docfis', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'obras', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'obras', 'ns', 'pessoas', 'id_agente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'obras', 'ns', 'pessoas', 'id_orgao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'obras', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'obras', 'persona', 'processos', 'processoaprendiz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'obras', 'persona', 'processos', 'processofap');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'obras', 'persona', 'processos', 'processorat');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pendencias', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pendencias', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pendencias', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pendencias', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pendencias_administrativas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoas', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoas', 'financas', 'contas', 'id_conta_receber');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoas', 'ns', 'pessoas', 'captador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoas', 'ns', 'pessoas', 'id_cliente_fatura');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoas', 'ns', 'pessoas', 'representante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoas', 'ns', 'pessoas', 'representante_tecnico');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoas', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoas', 'scritta', 'od_tipout', 'id_despesadiferenciada');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoas', 'scritta', 'od_tipout', 'id_receitadiferenciada');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoas_autorizados', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoascategoriasprodutos', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoascomissoes', 'ns', 'pessoas', 'idpessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoasformaspagamentos', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoasmunicipios', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'pessoasparcelamentos', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'qualificacoespj', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'regrasvencimentosclientes', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'relacoespessoas', 'ns', 'pessoas', 'pessoadireita');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'relacoespessoas', 'ns', 'pessoas', 'pessoaesquerda');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'relatoriosgerados', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'relatoriosgerados', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'relatoriosgerados', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'relatoriospath', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'scp', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'scp', 'ns', 'empresas', 'id_empresascp');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'series', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'socios', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'sociosparticipacoes', 'ns', 'socios', 'socio');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'tabelas_precos_de_entregas', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'telefones', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'templatesemails', 'ns', 'estabelecimentos', 'estabelecimento_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'usuarios', 'ns', 'empresas', 'ultimaempresapersona');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'usuarios', 'ns', 'estabelecimentos', 'ultimaempresascritta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'usuarios', 'ns', 'estabelecimentos', 'ultimoestabelecimentocontabil');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'usuarios', 'ns', 'estabelecimentos', 'ultimoestabelecimentopersonaweb');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'usuarios', 'ns', 'pessoas', 'id_entregador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'usuarios', 'ns', 'pessoas', 'representante_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'usuarios', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'valoresdefaultcontabilizacoes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ns', 'valoresdefaultcontabilizacoes', 'persona', 'eventos', 'rubrica');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'atividades', 'estoque', 'unidades', 'unidadeproduto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'atividadesprodutos', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'ordensdeinspecoes', 'estoque', 'locaisdeestoques', 'localdeestoquedestino');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'ordensdeinspecoes', 'estoque', 'locaisdeestoques', 'localdeestoqueorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'ordensdeinspecoes', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'ordensdeinspecoes', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'ordensdeinspecoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'ordensdeproducoesetapasbeneficiamentosnotas', 'ns', 'df_docfis', 'nota');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'ordensdeproducoesetapasitens', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'planosdeinspecoes', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'planosdeproducoes', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'planosdeproducoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'projetosescopo', 'estoque', 'produtos', 'atividade_produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'projetosescopo', 'estoque', 'produtos', 'produtoid');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'projetosescopo', 'estoque', 'unidades', 'atividade_unidadeproduto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'projetosescopo', 'estoque', 'unidades', 'produtounidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'projetosescopoestoque', 'estoque', 'locaisdeestoques', 'localestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'roteiros', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'roteiros', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'roteirosetapas', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'roteirosetapasfornecedores', 'ns', 'pessoas', 'fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'roteirosmateriais', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'roteirosmateriais', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'tarefas', 'estoque', 'produtosenderecos', 'produtoendereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'tarefasmateriaisutilizados', 'estoque', 'itens', 'atividadeproduto_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pcp', 'tarefasmateriaisutilizados', 'estoque', 'produtosenderecos', 'produtoendereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'devolucoes', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'devolucoes', 'ns', 'pessoas', 'id_vendedor_origem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'devolucoesitem', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'devolucoesitem', 'ns', 'pessoas', 'id_vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'itenspedido', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'itenspedido', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'itenspedido', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'itensprevenda', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'itensprevenda', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'itensprevenda', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'notasinutilizadas', 'ns', 'series', 'serie');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'ocorrenciasnfce', 'ns', 'df_docfis', 'nfce');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'ocorrenciassat', 'ns', 'df_docfis', 'sat');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'pagamentos', 'ns', 'df_docfis', 'venda');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'pedidos', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'pedidos', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pdv', 'pontosdevenda', 'estoque', 'locaisdeestoques', 'localestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('pedidos', 'operacoesestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'acordosdeprorrogacoes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'acordosdeprorrogacoesfaixas', 'persona', 'acordosdeprorrogacoes', 'acordodeprorrogacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'acordosdeprorrogacoesfaixas', 'persona', 'acordosdeprorrogacoes', 'acordodeprorrogacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'acordosmp9362020', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'acordosmp9362020', 'persona', 'acordosmp9362020', 'acordomp9362020anterior');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'acordosmp9362020trabalhadores', 'persona', 'acordosmp9362020', 'acordomp9362020');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'acordosmp9362020trabalhadores', 'persona', 'afastamentostrabalhadores', 'afastamentotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'acordosmp9362020trabalhadores', 'persona', 'reajustestrabalhadores', 'reajustetrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'acordosmp9362020trabalhadores', 'persona', 'reajustestrabalhadores', 'reajustetrabalhadorfimacordo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'acordosmp9362020trabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'adiantamentosavulsos', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'admissoespreliminares', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'admissoespreliminares', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'admissoespreliminares', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'afastamentostrabalhadores', 'persona', 'afastamentostrabalhadores', 'afastamentointerrupcao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'afastamentostrabalhadores', 'persona', 'afastamentostrabalhadores', 'afastamentotrabalhadorpai');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'afastamentostrabalhadores', 'persona', 'processos', 'processo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'afastamentostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'agentescausadorescatstrabalhadores', 'persona', 'catstrabalhadores', 'cattrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'ambientes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'ambientes', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'ambientestrabalhadores', 'persona', 'ambientes', 'ambiente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'ambientestrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'anexosajustes', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'apontamentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'apontamentostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'aquisicaoproducao', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'aquisicaoproducao', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'aquisicaoproducao', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'asostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'atividades', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'atividadescondicoesambientestrabalho', 'persona', 'condicoesambientestrabalho', 'condicaoambientetrabalho');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'atividadestrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'atualizacoessaldofgtstrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'avisosferiastrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'avisospreviostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'beneficios', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'beneficios', 'persona', 'eventos', 'eventodesconto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'beneficiostrabalhadores', 'persona', 'dependentestrabalhadores', 'dependentetrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'beneficiostrabalhadores', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'beneficiostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculosbeneficiostrabalhadores', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculosbeneficiostrabalhadores', 'persona', 'convocacoestrabalhadores', 'convocacaotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculosbeneficiostrabalhadores', 'persona', 'dependentestrabalhadores', 'dependentetrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculosbeneficiostrabalhadores', 'persona', 'eventos', 'evento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculosbeneficiostrabalhadores', 'persona', 'eventos', 'rubricacredito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculosbeneficiostrabalhadores', 'persona', 'eventos', 'rubricadesconto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculosbeneficiostrabalhadores', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculosbeneficiostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'ns', 'estabelecimentos', 'estabelecimentomovimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'persona', 'afastamentostrabalhadores', 'afastamentotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'persona', 'avisosferiastrabalhadores', 'avisoferiastrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'persona', 'avisospreviostrabalhadores', 'avisopreviotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'persona', 'convocacoestrabalhadores', 'convocacaotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'persona', 'departamentos', 'departamentomovimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'persona', 'dependentestrabalhadores', 'dependentetrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'persona', 'eventos', 'evento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'calculostrabalhadores', 'ponto', 'lancamentos', 'lancamentoponto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'camposespeciais', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'camposespeciaistrabalhadores', 'persona', 'camposespeciais', 'campoespecial');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'camposespeciaistrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'camposlayoutsimportacoes', 'persona', 'layoutsimportacoes', 'layoutimportacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'cargos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'cargos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'cargos', 'persona', 'condicoesambientestrabalho', 'condicaoambientetrabalho');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'cargos', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'cargos', 'persona', 'horarios', 'horario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'cargos', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'catstrabalhadores', 'persona', 'ambientes', 'ambiente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'catstrabalhadores', 'persona', 'catstrabalhadores', 'catorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'catstrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'codigosexternosempresas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'codigosexternosevento', 'ns', 'empresas', 'empresaassociada');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'codigosexternosevento', 'persona', 'eventos', 'evento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'codigosexternosevento', 'persona', 'eventos', 'eventoassociado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'codigosexternostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'codigossefipgpsestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'codigossefipgpstomadores', 'ns', 'pessoas', 'tomador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'comercializacaoproducao', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'comercializacaoproducao', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'comercializacaoproducao', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'compromissostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'condicoesambientestrabalho', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'condicoesambientestrabalho', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'condicoesambientestrabalho', 'persona', 'ambientes', 'ambiente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'condicoesambientestrabalho', 'persona', 'ambientes', 'ambiente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'configuracoesordemcalculomovimentos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'configuracoesordemcalculomovimentosponto', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'configuracoessalariosliquidos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'consolidacao', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'consolidacao', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'contascorrentespagadoras', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'contascorrentespagadoras', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'contratosbeneficiosempresas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'contratosfaturamentoservicos', 'ns', 'pessoas', 'beneficiariotitulocredito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'contratosfaturamentoservicostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'contribuicoessindicaispatronais', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'convocacoestrabalhadores', 'persona', 'horarios', 'horario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'convocacoestrabalhadores', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'convocacoestrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'darftrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'darftrabalhadores', 'scritta', 'grec_darf', 'darf');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'departamentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'departamentos', 'persona', 'trabalhadores', 'gestor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'dependentestrabalhadores', 'persona', 'dependentestrabalhadores', 'dependentetrabalhadorpensao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'dependentestrabalhadores', 'persona', 'eventos', 'eventopensao13');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'dependentestrabalhadores', 'persona', 'eventos', 'eventopensaoferias');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'dependentestrabalhadores', 'persona', 'eventos', 'eventopensaofolha');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'dependentestrabalhadores', 'persona', 'eventos', 'eventopensaopplr');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'dependentestrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'detalhamentoscalculostrabalhadores', 'persona', 'calculostrabalhadores', 'calculotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'detalhamentoscalculostrabalhadores', 'persona', 'eventos', 'evento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'detalhamentospedidosvalestransportestrabalhadores', 'persona', 'valestransportespersonalizadostrabalhadores', 'valetransportepersonalizadotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'dispensavalestransportestrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'documentosadmissoespreliminares', 'persona', 'admissoespreliminares', 'admissaopreliminar');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'documentoscolaboradores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'documentosdependentescolaboradores', 'persona', 'dependentestrabalhadores', 'dependentetrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'documentosregrascolaboradores', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'emprestimostrabalhadores', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'emprestimostrabalhadores', 'persona', 'eventos', 'evento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'emprestimostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'episfatoresriscoscondicoesambientestrabalho', 'persona', 'fatoresriscoscondicoesambientestrabalho', 'fatorriscocondicaoambientetrabalho');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'escalasfolgastrabalhadores', 'persona', 'horarios', 'horario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'escalasfolgastrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'eventos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'eventos', 'persona', 'eventos', 'eventofaixa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'examesasostrabalhadores', 'persona', 'asostrabalhadores', 'asotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'examestoxicologicostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'faltastrabalhadores', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'faltastrabalhadores', 'persona', 'trabalhadores', 'solicitante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'faltastrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'fatoresriscoscondicoesambientestrabalho', 'persona', 'condicoesambientestrabalho', 'condicaoambientetrabalho');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'fatoresriscostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'fechamentosfolhas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'fechamentosfolhasestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'fechamentosfolhasestabelecimentos', 'persona', 'fechamentosfolhas', 'fechamentofolha');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'funcoes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'gestorestrabalhadores', 'persona', 'trabalhadores', 'gestor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'gestorestrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'grcsfuncionarios', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'grcsfuncionarios', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'grcspatronais', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'grcspatronais', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'grcstrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'grrftrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasiss', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasiss', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasiss', 'ns', 'pessoas', 'tomador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasisstrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasprevidenciasocialdepartamentos', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasprevidenciasocialdepartamentos', 'persona', 'guiasprevidenciasocialempresas', 'guiaprevidenciasocialempresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasprevidenciasocialempresas', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasprevidenciasocialempresas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasprevidenciasocialempresas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasprevidenciasocialempresas', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasprevidenciasocialempresastrabalhadores', 'persona', 'guiasprevidenciasocialempresas', 'guiaprevidenciasocialempresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasprevidenciasocialempresastrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiasprevidenciasocialtrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiassefip', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiassefip', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiassefip', 'ns', 'pessoas', 'tomador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiassefiptrabalhadores', 'persona', 'guiassefip', 'guiasefip');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'guiassefiptrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosdadosfatorr', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosgps', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosgpsestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosgpsestabelecimentos', 'persona', 'processos', 'processofap');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosgpsestabelecimentos', 'persona', 'processos', 'processorat');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosgpsobrasestabelecimentos', 'persona', 'processos', 'processofap');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosgpsobrasestabelecimentos', 'persona', 'processos', 'processorat');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosgpsobraspessoas', 'persona', 'processos', 'processofap');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosgpsobraspessoas', 'persona', 'processos', 'processorat');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosgpspessoas', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosgpspessoas', 'persona', 'processos', 'processofap');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicosgpspessoas', 'persona', 'processos', 'processorat');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'historicostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horarios', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horarios', 'persona', 'jornadas', 'jornadadomingo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horarios', 'persona', 'jornadas', 'jornadaoutros');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horarios', 'persona', 'jornadas', 'jornadaquarta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horarios', 'persona', 'jornadas', 'jornadaquinta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horarios', 'persona', 'jornadas', 'jornadasabado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horarios', 'persona', 'jornadas', 'jornadasegunda');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horarios', 'persona', 'jornadas', 'jornadasexta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horarios', 'persona', 'jornadas', 'jornadaterca');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horariosalternativostrabalhadores', 'persona', 'horarios', 'horario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horariosalternativostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horariosespeciais', 'persona', 'horarios', 'horario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'horariosespeciais', 'persona', 'jornadas', 'jornada');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'instituicoesestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'intervalosjornadas', 'persona', 'jornadas', 'jornada');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'jornadas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'layoutsimportacoes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'layoutsrelatoriosempresa', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'layoutsrelatoriosempresa', 'persona', 'acordosmp9362020', 'acordomp9362020');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'locados', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'locados', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'locados', 'ns', 'pessoas', 'prestadorservico');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'locados', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'locados', 'persona', 'horarios', 'horario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'locados', 'persona', 'niveiscargos', 'nivelcargo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'lotacoes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'lotacoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'lotacoes', 'ns', 'pessoas', 'tomador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'lotacoes', 'persona', 'processos', 'processo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'lotacoesprojetos', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'membroscipa', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'membroscipa', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'modelosemailsconvocacoes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentos', 'persona', 'convocacoestrabalhadores', 'convocacaotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentos', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentos', 'persona', 'dependentestrabalhadores', 'dependentetrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentos', 'persona', 'eventos', 'evento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentos', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentos', 'persona', 'lotacoes', 'lotacaofuncionario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentos', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentos', 'ponto', 'lancamentos', 'lancamentoponto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentosponto', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentosponto', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentosponto', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentosponto', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'movimentosponto', 'persona', 'rubricasponto', 'rubricaponto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'mudancastrabalhadores', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'mudancastrabalhadores', 'persona', 'cargos', 'cargo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'mudancastrabalhadores', 'persona', 'condicoesambientestrabalho', 'condicaoambientetrabalho');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'mudancastrabalhadores', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'mudancastrabalhadores', 'persona', 'horarios', 'horario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'mudancastrabalhadores', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'mudancastrabalhadores', 'persona', 'niveiscargos', 'nivelcargo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'mudancastrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'niveiscargos', 'persona', 'cargos', 'cargo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'observacoesregistrosambientaistrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'outrasdespesastrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'outrosrecebimentostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'pagamentostrabalhadoresavulsosnaoportuarioslotacoes', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'parcelasemprestimostrabalhadores', 'persona', 'emprestimostrabalhadores', 'emprestimotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'partesatingidascatstrabalhadores', 'persona', 'catstrabalhadores', 'cattrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'patestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'pedidosbeneficiosalelosodexo', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'pedidosbeneficiosalelosodexotrabalhador', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'pedidosvalestransportes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'pedidosvalestransportestrabalhadores', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'pedidosvalestransportestrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'pendenciaspagamentos', 'persona', 'avisosferiastrabalhadores', 'avisoferiastrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'pendenciaspagamentos', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'planosaudedependentesvaloresmensais', 'persona', 'planossaudedependentestrabalhadores', 'planosaudedependentetrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'planossaude', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'planossaudedependentestrabalhadores', 'persona', 'dependentestrabalhadores', 'dependentetrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'planossaudedependentestrabalhadores', 'persona', 'dependentestrabalhadores', 'dependentetrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'planossaudedependentestrabalhadores', 'persona', 'planossaudetrabalhadores', 'planosaudetrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'planossaudedependentestrabalhadores', 'persona', 'planossaudetrabalhadores', 'planosaudetrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'planossauderubricas', 'persona', 'eventos', 'rubrica');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'planossauderubricas', 'persona', 'planossaude', 'planosaude');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'planossaudetrabalhadores', 'persona', 'planossaude', 'planosaude');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'planossaudetrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'pontotrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'previdenciasprivadas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'previdenciasprivadas', 'persona', 'eventos', 'rubricabaseempresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'previdenciasprivadas', 'persona', 'eventos', 'rubricabaseparticipante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'previdenciasprivadas', 'persona', 'eventos', 'rubricacontribuicaoempresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'previdenciasprivadas', 'persona', 'eventos', 'rubricacontribuicaoparticipante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'previdenciasprivadasrubricas', 'persona', 'eventos', 'rubrica');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'previdenciasprivadastrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processos', 'ns', 'pessoas', 'prestador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processoscodigosterceiros', 'persona', 'processos', 'processo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processoslotacoes', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processoslotacoes', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processoslotacoes', 'persona', 'processos', 'processo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processoslotacoes', 'persona', 'processos', 'processo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processosrubricas', 'persona', 'eventos', 'rubrica');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processosrubricas', 'persona', 'eventos', 'rubrica');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processosrubricas', 'persona', 'processos', 'processo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processosrubricas', 'persona', 'processos', 'processo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'processossuspensoes', 'persona', 'processos', 'processo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'projetostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoes13', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoes13trabalhadores', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoes13trabalhadores', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoes13trabalhadores', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoes13trabalhadores', 'persona', 'provisoes13', 'provisao13');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoes13trabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoesferias', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoesferiastrabalhadores', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoesferiastrabalhadores', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoesferiastrabalhadores', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoesferiastrabalhadores', 'persona', 'provisoesferias', 'provisaoferias');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoesferiastrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoesrescisoes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoesrescisoes', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'provisoesrescisoes', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'rateioterceiros', 'persona', 'historicosgpsestabelecimentos', 'historicogpsestabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'rateioterceiros', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'reajustestrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'receitasdesportivas', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'relatoriosgravadosempresas', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'relatoriosliberados', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'relatoriosliberados', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'relatoriosliberados', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'responsaveisregistrocondicoesambientestrabalho', 'persona', 'condicoesambientestrabalho', 'condicaoambientetrabalho');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'responsaveisregistrosambientaistrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'responsaveisregistrosambientaistrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'riscosocupacionaisasostrabalhadores', 'persona', 'asostrabalhadores', 'asotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'rubricasconfiguracoescontabilidade', 'contabil', 'centrosdecusto', 'centrodecusto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'rubricasconfiguracoescontabilidade', 'contabil', 'contas', 'contacredito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'rubricasconfiguracoescontabilidade', 'contabil', 'contas', 'contadebito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'rubricasconfiguracoescontabilidade', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'rubricasconfiguracoescontabilidade', 'persona', 'eventos', 'rubrica');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'rubricasconfiguracoescontabilidade', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'rubricasponto', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'rubricasponto', 'persona', 'eventos', 'evento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'rubricasponto', 'persona', 'eventos', 'eventobancohoras');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'salariosliquidos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'salariosliquidos', 'persona', 'salariosliquidostotais', 'salarioliquidototal');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'salariosliquidostotais', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'salariosliquidostotaistrabalhadores', 'persona', 'salariosliquidostotais', 'salarioliquidototal');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'salariosliquidostotaistrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'salariosliquidostrabalhadores', 'persona', 'salariosliquidos', 'salarioliquido');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'salariosliquidostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'selic', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'solicitacoesalteracoesdadoscadastrais', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'solicitacoesalteracoesdadoscadastrais', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'solicitacoesalteracoesdadoscadastrais', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'solicitacoesalteracoesvt', 'ns', 'empresas', 'solicitante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'solicitacoesalteracoesvt', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'solicitacoesrescisoes', 'persona', 'avisospreviostrabalhadores', 'avisopreviotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'solicitacoesrescisoes', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'tarifasconcessionariasvtstrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'testemunhascatstrabalhadores', 'persona', 'catstrabalhadores', 'cattrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'tiposfuncionarios', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'acordosdeprorrogacoes', 'acordodeprorrogacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'condicoesambientestrabalho', 'condicaoambientetrabalho');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'horarios', 'horario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'niveiscargos', 'nivelcargo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'processos', 'processoadmissao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'processos', 'processocontribuicaosindical');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'processos', 'processodemissao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'processos', 'processofgts');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'processos', 'processoinss');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'processos', 'processoirrf');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'processos', 'processomenoraprendiz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'processos', 'processoreintegracao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'tiposfuncionarios', 'tipofuncionario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'trabalhadores', 'matriculaoutracategoria');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'trabalhadores', 'matriculaoutrovinculo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'trabalhadores', 'persona', 'trabalhadores', 'trabalhadorsubstituido');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'transacoescalculostrabalhadorescomcalculos', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'transacoescalculostrabalhadoresfiltrados', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'transacoescalculostrabalhadoresremovidos', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'transacoescalculostrabalhadoressemcalculos', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'treinamentoscapacitacoestrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'treinamentoscapacitacoestrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'treinamentoscapacitacoestrabalhadoresdetalhes', 'persona', 'treinamentoscapacitacoestrabalhadores', 'treinamentocapacitacaotrabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'treinamentoscapacitacoestrabalhadoresdetalhesprofissionais', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'treinamentoscapacitacoestrabalhadoresdetalhesprofissionais', 'persona', 'treinamentoscapacitacoestrabalhadoresdetalhes', 'treinamentocapacitacaotrabalhadordetalhe');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'treinamentoscapacitacoestrabalhadoresdetalhesresponsaveis', 'persona', 'treinamentoscapacitacoestrabalhadoresdetalhes', 'iddetalhe');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'tributacoesexclusivastrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'valestransportespersonalizadostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'valoresparafaturamentos', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'valoresparafaturamentos', 'ns', 'df_docfis', 'rps');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'valoresparafaturamentos', 'ns', 'pessoas', 'pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'valoresparafaturamentosdetalhados', 'persona', 'eventos', 'evento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'valoresparafaturamentosdetalhados', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'valorespontosindicatos', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('persona', 'valorespontosindicatos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'ajustes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'ajustes', 'persona', 'trabalhadores', 'solicitante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'ajustes', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'ajustes', 'ponto', 'marcacoes', 'marcacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'ajustes', 'ponto', 'marcacoes', 'marcacaoantiga');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'apuracoesponto', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'apuracoesponto', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'apuracoesponto', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'atrasosentradascompensaveistrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'compensacoeslancamentos', 'ponto', 'lancamentos', 'lancamentoapuracaodestino');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'compensacoeslancamentos', 'ponto', 'lancamentos', 'lancamentoapuracaoorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'diascompensacoestrabalhadores', 'persona', 'horarios', 'horario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'diascompensacoestrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'historicos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'historicos', 'ns', 'pessoas', 'tomador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'historicos', 'persona', 'departamentos', 'departamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'historicos', 'persona', 'horarios', 'horario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'historicos', 'persona', 'jornadas', 'jornada');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'historicos', 'persona', 'jornadas', 'jornadafolga');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'historicos', 'persona', 'lotacoes', 'lotacao');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'historicos', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'historicos', 'ponto', 'apuracoesponto', 'apuracaoponto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'inconsistenciaspontotrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'lancamentos', 'persona', 'rubricasponto', 'rubricaponto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'lancamentos', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'lancamentos', 'ponto', 'apuracoesponto', 'apuracaoponto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'marcacoes', 'ns', 'empresas', 'empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'marcacoes', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'pagamentoslancamentos', 'ponto', 'lancamentos', 'lancamento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'pendenciascalculostrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'pendenciascalculostrabalhadores', 'ponto', 'apuracoesponto', 'apuracaoponto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('ponto', 'saidasantecipadascompensaveistrabalhadores', 'persona', 'trabalhadores', 'trabalhador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'agenda', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'agenda_usu', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'aidf', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'aidf', 'ns', 'pessoas', 'id_grafica');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ajuste_va', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'am_dia_itens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'am_dia_nfe', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'am_dia_nfe', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'apuracao', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'apuracao_sped', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'apuracao_va', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'bens_ciap', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'bens_evento', 'ns', 'bens', 'id_bem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'bens_grupos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'bens_movimentos', 'ns', 'bens', 'id_bem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'bens_movimentos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cancelamento', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cfg_bases', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cfg_cfop', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cfg_cfop', 'scritta', 'od_tipout', 'id_tipout');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cfg_imposto', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cfgempresa', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cfgestab', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cmb_bombas', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cmb_bombas', 'ns', 'pessoas', 'id_conservadora');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cmb_bombas', 'ns', 'pessoas', 'id_fabricante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cmb_combustiveis', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cmb_combustiveis', 'ns', 'pessoas', 'id_distribuidora');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cmb_lacres', 'ns', 'pessoas', 'id_interventor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cmb_movimentos', 'ns', 'df_docfis', 'id_nota');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cmb_observacoes', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'consorciados', 'ns', 'estabelecimentos', 'id_consorciado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'consorcio', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'consorcio', 'ns', 'estabelecimentos', 'id_lider');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'contas_contabeis_sped', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'cprb_contab', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'dde', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'dde_notas', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'dde_notas', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'dde_notas', 'scritta', 'lf_itens', 'chaveitem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'dde_notas', 'scritta', 'lf_lanfis', 'chavelanc');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'dependentes', 'ns', 'pessoas', 'id_dependente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'dependentes', 'ns', 'pessoas', 'id_titular');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_bilhetes', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_campos', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_deducoes', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_deducoes', 'scritta', 'processo', 'id_processo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_docref', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_guias', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_lancpc', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_modais', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_modais', 'ns', 'pessoas', 'id_emitente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_modais', 'ns', 'pessoas', 'id_tomador');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_nottra', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_nottra', 'ns', 'pessoas', 'id_coleta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_nottra', 'ns', 'pessoas', 'id_destinatario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_nottra', 'ns', 'pessoas', 'id_entrega');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_nottra', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_nottra', 'ns', 'pessoas', 'id_remetente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_outros', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_outros', 'scritta', 'od_tipout', 'id_tipout');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_ressarcimento', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_ressarcimento', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_ressarcimento', 'ns', 'df_docfis', 'id_ent_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_ressarcimento', 'ns', 'df_docfis', 'id_orig_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_ressarcimento', 'ns', 'df_itens', 'id_itedoc');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_ressarcimento', 'ns', 'pessoas', 'id_origpessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_ressarcimento', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_sertra', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_sertra', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_tracomb', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_tracomb', 'ns', 'pessoas', 'id_motorista');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'df_tracomb', 'ns', 'pessoas', 'id_transportadora');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf', 'ns', 'pessoas', 'id_fabricante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_cro', 'scritta', 'ecf', 'id_ecf');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_mr', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_notas', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_notas', 'scritta', 'ecf_rz', 'id_reducaoz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_notas', 'scritta', 'ecf_rzcf', 'id_cupom');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_pg', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_rz', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_rz', 'scritta', 'ecf', 'id_ecf');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_rz_contabil', 'scritta', 'ecf_rz', 'id_reducaoz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_rzbp', 'scritta', 'ecf_rz', 'id_reducaoz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_rzcf', 'scritta', 'ecf_rz', 'id_reducaoz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_rzitens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_rzitens', 'scritta', 'ecf_rz', 'id_reducaoz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_rzitens', 'scritta', 'ecf_rzcf', 'id_cupom');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_rzpg', 'scritta', 'ecf_rz', 'id_reducaoz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_rztp', 'scritta', 'ecf_rz', 'id_reducaoz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'ecf_tp', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'feef', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'gnre_dados', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_cfg', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_cfg', 'ns', 'pessoas', 'id_fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_darf', 'financas', 'titulos', 'titulo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_darf', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_darf', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_darf', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_darf', 'scritta', 'grec_darf', 'id_mestre');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_darf', 'scritta', 'grec_darf', 'id_mestre_parc');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_gnre', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_gnre', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_gps', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_gps', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_icms_iss', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_icms_iss', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_resumo', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_resumo', 'scritta', 'grec_darf', 'id_guiadarf');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'grec_resumo', 'scritta', 'grec_icms_iss', 'id_guiaicms');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'imovel_contrato', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'imovel_contrato', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'imovel_contrato', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'imovel_contrato', 'ns', 'pessoas', 'id_proprietario');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'imovel_contrato', 'scritta', 'imovel_empreendimento', 'id_empreendimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'imovel_empreendimento', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'imovel_empreendimento', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'imovel_movimento', 'scritta', 'imovel_contrato', 'id_contrato');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'imovel_reajuste', 'scritta', 'imovel_contrato', 'id_contrato');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'inv_contas', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'item_pc', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'itensclientes', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'itensclientes', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'itensfor', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'itensfor', 'ns', 'pessoas', 'id_fornecedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lanaju', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lanaju', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lanaju', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lanaju', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lanaju', 'scritta', 'grec_icms_iss', 'id_grec');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lanaju', 'scritta', 'lf_lanfis', 'id_lanfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lf_itens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lf_itens', 'scritta', 'lf_lanfis', 'id_lanfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lf_lanfis', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lf_lanfis', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lf_lanfis', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lf_lanfis', 'scritta', 'ecf', 'id_ecf');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lf_lanfis', 'scritta', 'ecf_rz', 'id_redz');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lf_lanfis', 'scritta', 'od_tipout', 'id_grupodiferenciado');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lf_servicos', 'scritta', 'lf_lanfis', 'id_lanfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'lotedigital', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'od_gruout', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'od_outdoc', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'od_outdoc', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'od_outdoc', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'od_outdoc', 'scritta', 'od_gruout', 'id_gruout');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'od_outdoc', 'scritta', 'od_tipout', 'id_tipo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'od_tipout', 'contabil', 'contas', 'id_conta_credito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'od_tipout', 'contabil', 'contas', 'id_conta_debito');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'od_tipout', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'pc_cred_lanc', 'scritta', 'pc_credito', 'id_cred');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'pc_credito', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'pc_diferimento', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'pendencias', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'perfilimp_config_estoque', 'estoque', 'locaisdeestoques', 'id_localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'perfilimp_config_estoque', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'processo', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'processo', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_cp', 'estoque', 'itens', 'id_itemproduzido');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_cp', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_direto', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_direto', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_direto', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_insumos', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_insumos', 'estoque', 'itens', 'id_itemsubst');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_movimento', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_movimento', 'estoque', 'itens', 'id_substituido');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_movint', 'estoque', 'itens', 'id_itemfinal');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_movint', 'estoque', 'itens', 'id_itemorigem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_movint', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_ordem', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_outros', 'estoque', 'itens', 'id_itemdest');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_outros', 'estoque', 'itens', 'id_itemorig');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_outros', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_produto', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_subitens', 'estoque', 'itens', 'id_pai');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'rcpe_subitens', 'estoque', 'itens', 'id_subitem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'redarf', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'regesp', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'regesp_ajuste', 'scritta', 'regesp', 'id_regime');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'regesp_cfop', 'scritta', 'regesp', 'id_regime');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'regesp_doc', 'scritta', 'regesp', 'id_regime');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'regesp_lanc', 'scritta', 'regesp', 'id_regime');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'reinf', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'revenda_bens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'revenda_bens', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'revenda_mov', 'estoque', 'itens_mov', 'id_movest');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'revenda_mov', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'revenda_mov', 'ns', 'df_itens', 'id_itedoc');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'revenda_mov', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'saldocredor', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'scp', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'scp', 'ns', 'empresas', 'id_empresascp');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sn_cfg', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sn_creditos', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sn_exclusoes', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sp_cat_itens', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sped_custo', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sped_defcontas', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sped_ecf_receitas', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sped_ecf_retencoes', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sped_pc_c100', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sped_pc_c100', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sped_pc_c175', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sped_pc_c175', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'sped_planocontas', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'susp_tributos', 'ns', 'empresas', 'id_empresa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'susp_tributos', 'scritta', 'processo', 'id_processo');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'uniprofissionais', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('scritta', 'uniprofissionais', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'atendimentos', 'ns', 'enderecos', 'endereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'atendimentos', 'ns', 'estabelecimentos', 'estabelecimento_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'atendimentos', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'atendimentosnegociacoesitens', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'boletinsmedicao', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'boletinsmedicao', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'cartasdecorrecoesservicos', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'cfopsestabelecimentos', 'ns', 'estabelecimentos', 'estabelecimento_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'componentes', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'composicoesmercadorias', 'estoque', 'produtos', 'id_mercadoria');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'configuracoesrecorrenciadocumentos', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'docpedidosvendasservicos', 'financas', 'contas', 'id_conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'docpedidosvendasservicos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'docpedidosvendasservicos', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'emailsrps', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'enderecoclienteprefeitura', 'ns', 'pessoas', 'id_participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'faturalocacaorelacionamentos', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'faturalocacaorelacionamentos', 'ns', 'df_docfis', 'id_docfispai');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'faturasordensservicos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'faturasordensservicos', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'funcoescustosmateriais', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'funcoescustosmateriais', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'lotescobrancasordensservicos', 'ns', 'estabelecimentos', 'estabelecimento_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'lotescobrancasordensservicos', 'ns', 'pessoas', 'cliente_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'lotesrpss', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'lotesrpssporrpss', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'modelosobjetosservicos', 'ns', 'pessoas', 'fabricante_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'movimentos', 'estoque', 'locaisdeestoques', 'localdeestoque_destino');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'movimentos', 'estoque', 'locaisdeestoques', 'localdeestoque_origem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'movimentos', 'ns', 'estabelecimentos', 'estabelecimento_destino');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'movimentos', 'ns', 'estabelecimentos', 'estabelecimento_origem');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'movimentositens', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'notasaseremcanceladas', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'objetosservicos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'objetosservicos', 'ns', 'enderecos', 'endereco_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'objetosservicos', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'objetosservicosbase', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'objetosservicosbase', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'objetosservicosbase', 'ns', 'enderecos', 'endereco_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'objetosservicosbase', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'operacoesordensservicos_locaisestoques', 'estoque', 'locaisdeestoques', 'localdeestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'operacoesordensservicos_locaisestoques', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'orcamentos', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'orcamentoscustosmateriais', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'orcamentoscustosmateriais', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'orcamentosenderecos', 'ns', 'enderecos', 'endereco');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'orcamentositensfaturamento', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'orcamentostecnicos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'orcamentostecnicos', 'ns', 'pessoas', 'cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'orcamentostecnicos', 'ns', 'pessoas', 'tecnico');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'ordensexpedicoes', 'estoque', 'produtos', 'produto_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'ordensservicos', 'ns', 'enderecos', 'enderecocliente_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'ordensservicos', 'ns', 'estabelecimentos', 'estabelecimento_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'ordensservicos', 'ns', 'pessoas', 'cliente_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'ordensservicos_produtosmovimentos', 'estoque', 'itens', 'item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'ordensservicos_produtosmovimentos', 'estoque', 'locaisdeestoques', 'localestoque');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'ordensservicosobjetosservicos', 'estoque', 'produtos', 'produto_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'ordensservicosprodutos', 'estoque', 'itens', 'item_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'ordensservicosprodutos', 'estoque', 'locaisdeestoques', 'localdeestoque_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'ordensservicosprodutos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'pedidosdeservicos', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'pedidosdeservicos', 'ns', 'pessoas', 'id_cliente');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'pedidosservicosnotasservicos', 'ns', 'df_docfis', 'notaservico_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'pedidosservicosnotasservicos', 'ns', 'df_docfis', 'pedidoservico_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'pedidosvendasservicos', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'pedidosvendasservicos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'pedidosvendasservicos', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'pedidosvendasservicosporvendedores', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'prenfseitupeva', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'prenfseitupeva', 'ns', 'estabelecimentos', 'id_estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'rps_simplificada', 'ns', 'df_docfis', 'id_docfis');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'rps_simplificada', 'ns', 'pessoas', 'id_pessoa');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'rps_simplificada_modelos', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'rps_simplificada_modelos_formapagamento', 'financas', 'contas', 'conta');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'rpss', 'ns', 'estabelecimentos', 'estabelecimento');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'rpss', 'ns', 'pessoas', 'participante');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'rpss', 'ns', 'series', 'serie');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'rpss', 'ns', 'series', 'serierpssubstituido');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'servicos', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'servicos', 'estoque', 'unidades', 'unidade');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'servicos', 'scritta', 'sped_pc', 'sped_pc');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'servicoscatalogo', 'estoque', 'itens', 'id_item');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'servicoscatalogo', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'vendedoresatendimento', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'vendedoresfatura', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'vendedoresordemservico', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'vendedoresrps', 'ns', 'pessoas', 'vendedor');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'viagensequipe', 'ns', 'pessoas', 'pessoa_id');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('servicos', 'viagensobjetosservicosbase', 'estoque', 'produtos', 'produto');
INSERT INTO exclusao.entidades_dependencias
(schema_name_origem, table_name_origem, schema_name_destino, table_name_destino, fk_column)
VALUES('util', 'notasimportacao', 'ns', 'estabelecimentos', 'estabelecimento');
"""


class MelhoriasModelagemStep(Step):
    """
    Aplica melhorias e ajustes na modelagem original do BD, para dar suporte a exclusão.

    Também cria a estrutura básica de controle do processo (schema exclusao,
    e tabelas; entidades e entidades_dependencias).
    """

    def verifica_entidades_exists(self):
        sql = f"""
        select 1 from exclusao.entidades limit 1
        """

        try:
            self.db_adapter.execute_query(sql)
            return True
        except Exception as e:
            return False

    def verifica_entidades_dependencias_exists(self):
        sql = f"""
        select 1 from exclusao.entidades_dependencias limit 1
        """

        try:
            self.db_adapter.execute_query(sql)
            return True
        except Exception as e:
            return False

    def main(self, data: str, invert_selecao: bool):
        self.log(
            "Aplicando ajustes no BD, e criando estrutura básica de controle do processo de exclusão..."
        )

        try:
            self.db_adapter.execute(MELHORIAS_MODELAGEM_SCRITTA)
        except:
            self.log("Não conseguiu criar as colunas de ID UUID em tabelas do scritta")

        if not self.verifica_entidades_exists():
            self.db_adapter.execute(CRIAR_TABELA_ENTIDADES)

        if not self.verifica_entidades_dependencias_exists():
            self.db_adapter.execute(CRIAR_TABELA_ENTIDADES_DEPENDENCIAS)
