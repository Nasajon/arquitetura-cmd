# Variaveis de controle
REGISTROS_DICT = {
    0: 'produtos',
    1: 'unidades',
    2: 'combustiveis',
    3: 'servicos',
    4: 'classificacoesparticipantes',
    5: 'fichas',
    6: 'clientes',
    7: 'fornecedores',
    8: 'transportadoras',
    9: 'vendedores',
    10: 'servicosdecatalogos',
    11: 'modeloscontratos',
    12: 'tecnicos',
    13: 'rubricas',
    14: 'representantescomerciais',
    15: 'representantestecnicos',
    16: 'prospects'
    # 17: 'pessoasfisicas'
}

REGISTROS_DICT_REVERSE = {REGISTROS_DICT[k]: k for k in REGISTROS_DICT}

REGISTROS = [REGISTROS_DICT[k] for k in REGISTROS_DICT]
