#inserção dos dados ficticios

inserts = {
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
    'funcionario': [
        ('11111111111', 'Joao da Silva', '1970-01-01', 'M', 1),
        ('22222222222', 'Maria Souza', '1975-02-02', 'F', 2),
        ('33333333333', 'Carlos Gomes', '1980-03-03', 'M', 1),
        ('44444444444', 'Ana Oliveira', '1985-04-04', 'F', 2),
        ('55555555555', 'Pedro Almeida', '1990-05-05', 'M', 1),
        ('66666666666', 'Julia Costa', '1992-06-06', 'F', 2),
    ],
    'diretor': [
        ('11111111111', 'DF-1'),
        ('22222222222', 'DF-2'),
    ],
    'agente': [
        ('33333333333'),
        ('55555555555'),
    ],
    'medico': [
        ('44444444444', 'CRM-12345'),
    ],
    'preso': [
        ('77777777777', 'Fabio Pereira', '1995-07-07', 101, 1), # cpf, nome, data_nasc, cela_num, presidio_cod
        ('88888888888', 'Roberto Carlos', '1998-08-08', 101, 1),
        ('99999999999', 'Marcos Paulo', '2000-09-09', 201, 2),
        ('00000000000', 'Bernardo Vieira', '1993-05-10', 202, 2),
        ('01010101010', 'Gustavo Batista', '1999-08-12', 102, 1),
    ],
    'advogado': [
        ('10101010101', 'Fernanda Lima', '1980-10-10', 'OAB-101'),
        ('12121212121', 'Gustavo Pires', '1975-12-12', 'OAB-121'),
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
    'presidio': 'INSERT INTO PRESIDIO (cod, cidade, nivel_seguranca, lotacao_max, lotacao_atual, diretor_cpf) VALUES (?, ?, ?, ?, ?, ?)',
    'cela': 'INSERT INTO CELA (num, presidio_cod, lotacao_max, lotacao_atual) VALUES (?, ?, ?, ?)',
    'funcionario': 'INSERT INTO FUNCIONARIO (cpf, nome, data_nasc, genero, presidio_cod) VALUES (?, ?, ?, ?, ?)',
    'diretor': 'INSERT INTO DIRETOR (cpf, cod_pf) VALUES (?, ?)',
    'agente': 'INSERT INTO AGENTE (cpf) VALUES (?)',
    'medico': 'INSERT INTO MEDICO (cpf, cod_crm) VALUES (?, ?)',
    'preso': 'INSERT INTO PRESO (cpf, nome, data_nasc, cela_num, presidio_cod) VALUES (?, ?, ?, ?, ?)',
    'advogado': 'INSERT INTO ADVOGADO (cpf, nome, data_nasc, cod_oab) VALUES (?, ?, ?, ?)',
    'processo': 'INSERT INTO PROCESSO (cod, descricao, sentenca) VALUES (?, ?, ?)',
    'crimes': 'INSERT INTO CRIMES (processo_cod, crime) VALUES (?, ?)',
    'ocorrencia': 'INSERT INTO OCORRENCIA (cod, agente_cpf, descricao) VALUES (?, ?, ?)',
    'possui': 'INSERT INTO POSSUI (processo_cod, preso_cpf, advogado_cpf) VALUES (?, ?, ?)',
    'rival': 'INSERT INTO RIVAL (preso1_cpf, preso2_cpf) VALUES (?, ?)',
    'consulta': 'INSERT INTO CONSULTA (preso_cpf, medico_cpf, data, prontuario, ocorrencia_cod) VALUES (?, ?, ?, ?, ?)',
    'envolvido': 'INSERT INTO ENVOLVIDO (preso_cpf, ocorrencia_cod) VALUES (?, ?)',
}