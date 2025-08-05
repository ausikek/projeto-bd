#inserção dos dados ficticios

inserts = {
    'funcionario': [
        ('11111111111', 'Robson Fidalgo', '1970-01-01', 'M', None),
        ('22222222222', 'Alex Marques', '1975-02-02', 'F', None),
        ('33333333333', 'Carlos Gomes', '1980-03-03', 'M', None),
        ('44444444444', 'Ana Oliveira', '1985-04-04', 'F', None),
        ('55555555555', 'Pedro Almeida', '1990-05-05', 'M', None),
        ('66666666666', 'Julia Costa', '1992-06-06', 'F', None),
    ],
    'diretor': [
        ('11111111111', 'DF-1'),
        ('22222222222', 'DF-2'),
    ],
    'presidio': [
        (1, 'Porto Alegre', 'Máxima', 500, 3, '11111111111'),
        (2, 'Charqueadas', 'Média', 800, 2, '22222222222'),
    ],
    'cela': [
        (101, 1, 2, 2),  # num, presidio_cod, lotacao_max, lotacao_atual
        (102, 1, 2, 1),
        (201, 2, 4, 1),
        (202, 2, 4, 1),
    ],
    'agente': [
        ('33333333333',),
        ('55555555555',),
    ],
    'medico': [
        ('44444444444', 'CRM-12345'),
    ],
    'advogado': [
        ('10101010101', 'Fernanda Lima', '1980-10-10', 'OAB-101'),
        ('12121212121', 'Gustavo Pires', '1975-12-12', 'OAB-121'),
    ],
    'preso': [
        ('77777777777', 'Breno Filho', '1995-07-07', 101, 1), # cpf, nome, data_nasc, cela_num, presidio_cod
        ('88888888888', 'Danilo Barrote', '1998-08-08', 101, 1),
        ('99999999999', 'Guilherme Siqueira', '2000-09-09', 201, 2),
        ('00000000000', 'João Pedro Pontes', '1993-05-10', 202, 2),
        ('01010101010', 'Arthur Rocha', '1999-08-12', 102, 1),
        ('01010101011', 'Vitor Forte', '1999-08-12', 102, 1),
        ('01010101012', 'Igor Monitor', '1999-08-12', 102, 1),
    ],
    'processo': [
        (1, 'Processo criminal de roubo', 'Condenação a 5 anos'),
        (2, 'Processo por furto', 'Absolvição'),
        (3, 'Processo por homicídio', 'Condenação a 20 anos'),
    ],
    'crimes': [
        (1, 'Roubo qualificado'), # processo_cod, crime
        (2, 'Furto simples'),
        (2, 'Tentativa de homicídio'),
        (3, 'Homicídio doloso'),
        (3, 'Associação criminosa'),
    ],
    'ocorrencia': [
        (1, '33333333333', 'Briga entre presos'),
        (2, '55555555555', 'Tentativa de fuga'),
    ],
    'possui': [
        (1, '77777777777', '10101010101'), # processo_cod, preso_cpf, advogado_cpf
        (3, '99999999999', '12121212121'),
    ],
    'rival': [
        ('77777777777', '88888888888'),
    ],
    'consulta': [
        ('77777777777', '44444444444', '2025-08-05', 'Paciente com lesões no corpo', 1),
    ],
    'envolvido': [
        ('77777777777', 1), # preso_cpf, ocorrencia_cod
        ('88888888888', 1),
        ('99999999999', 2),
    ],
}

insert_queries = {
    'funcionario': 'INSERT INTO FUNCIONARIO (cpf, nome, data_nasc, genero, presidio_cod) VALUES (?, ?, ?, ?, ?)',
    'diretor': 'INSERT INTO DIRETOR (cpf, cod_pf) VALUES (?, ?)',
    'presidio': 'INSERT INTO PRESIDIO (cod, cidade, nivel_seguranca, lotacao_max, lotacao_atual, diretor_cpf) VALUES (?, ?, ?, ?, ?, ?)',
    'cela': 'INSERT INTO CELA (num, presidio_cod, lotacao_max, lotacao_atual) VALUES (?, ?, ?, ?)',
    'agente': 'INSERT INTO AGENTE (cpf) VALUES (?)',
    'medico': 'INSERT INTO MEDICO (cpf, cod_crm) VALUES (?, ?)',
    'advogado': 'INSERT INTO ADVOGADO (cpf, nome, data_nasc, cod_oab) VALUES (?, ?, ?, ?)',
    'preso': 'INSERT INTO PRESO (cpf, nome, data_nasc, cela_num, presidio_cod) VALUES (?, ?, ?, ?, ?)',
    'processo': 'INSERT INTO PROCESSO (cod, descricao, sentenca) VALUES (?, ?, ?)',
    'crimes': 'INSERT INTO CRIMES (processo_cod, crime) VALUES (?, ?)',
    'ocorrencia': 'INSERT INTO OCORRENCIA (cod, agente_cpf, descricao) VALUES (?, ?, ?)',
    'possui': 'INSERT INTO POSSUI (processo_cod, preso_cpf, advogado_cpf) VALUES (?, ?, ?)',
    'rival': 'INSERT INTO RIVAL (preso1_cpf, preso2_cpf) VALUES (?, ?)',
    'consulta': 'INSERT INTO CONSULTA (preso_cpf, medico_cpf, data, prontuario, ocorrencia_cod) VALUES (?, ?, ?, ?, ?)',
    'envolvido': 'INSERT INTO ENVOLVIDO (preso_cpf, ocorrencia_cod) VALUES (?, ?)',
}

updates = [
    ("11111111111", 1),
    ("22222222222", 2),
    ("33333333333", 1),
    ("44444444444", 2),
    ("55555555555", 1),
    ("66666666666", 2),
]