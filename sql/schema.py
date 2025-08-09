# database/schema.py

schema_statements = [
    
    ##ENTIDADES
    """
    CREATE TABLE IF NOT EXISTS FUNCIONARIO (
        cpf TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        data_nasc DATE,
        genero TEXT,
        presidio_cod INTEGER,
        FOREIGN KEY(presidio_cod) REFERENCES PRESIDIO(cod)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS DIRETOR (
        cpf TEXT PRIMARY KEY,
        cod_pf TEXT UNIQUE,
        FOREIGN KEY(cpf) REFERENCES FUNCIONARIO(cpf) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS AGENTE (
        cpf TEXT PRIMARY KEY,
        FOREIGN KEY(cpf) REFERENCES FUNCIONARIO(cpf) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS MEDICO (
        cpf TEXT PRIMARY KEY,
        cod_crm TEXT UNIQUE,
        FOREIGN KEY(cpf) REFERENCES FUNCIONARIO(cpf) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS ADVOGADO (
        cpf TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        data_nasc DATE,
        cod_oab TEXT UNIQUE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS PRESIDIO (
        cod INTEGER PRIMARY KEY,
        cidade TEXT,
        nivel_seguranca TEXT,
        lotacao_max INTEGER,
        lotacao_atual INTEGER,
        diretor_cpf TEXT NOT NULL UNIQUE,
        FOREIGN KEY(diretor_cpf) REFERENCES DIRETOR(cpf)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS CELA (
        num INTEGER NOT NULL,
        presidio_cod INTEGER NOT NULL,
        lotacao_max INTEGER,
        lotacao_atual INTEGER,
        PRIMARY KEY(num, presidio_cod),
        FOREIGN KEY(presidio_cod) REFERENCES PRESIDIO(cod) ON DELETE CASCADE
    );
    """,
    #not null em nome pela integridade do sistema, nao faz sentido ser vazio
    """
    CREATE TABLE IF NOT EXISTS PRESO (
        cpf TEXT PRIMARY KEY,
        nome TEXT NOT NULL, 
        data_nasc DATE,
        cela_num INTEGER,
        presidio_cod INTEGER,
        FOREIGN KEY(cela_num, presidio_cod)
            REFERENCES CELA(num, presidio_cod)
            ON DELETE SET NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS PROCESSO (
        cod INTEGER PRIMARY KEY,
        descricao TEXT,
        sentenca TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS CRIMES (
        processo_cod INTEGER NOT NULL,
        crime TEXT NOT NULL,
        PRIMARY KEY(processo_cod, crime),
        FOREIGN KEY(processo_cod) REFERENCES PROCESSO(cod) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS OCORRENCIA (
        cod INTEGER PRIMARY KEY,
        agente_cpf TEXT NOT NULL,
        descricao TEXT,
        FOREIGN KEY(agente_cpf) REFERENCES AGENTE(cpf) ON DELETE SET NULL
    );
    """,

    #RELACIONAMENTOS
    """
    CREATE TABLE IF NOT EXISTS POSSUI (
        processo_cod INTEGER NOT NULL,
        preso_cpf TEXT NOT NULL,
        advogado_cpf TEXT NOT NULL,
        PRIMARY KEY(processo_cod, advogado_cpf),
        FOREIGN KEY(processo_cod) REFERENCES PROCESSO(cod) ON DELETE CASCADE,
        FOREIGN KEY(preso_cpf) REFERENCES PRESO(cpf) ON DELETE CASCADE,
        FOREIGN KEY(advogado_cpf) REFERENCES ADVOGADO(cpf)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS RIVAL (
        preso1_cpf TEXT NOT NULL,
        preso2_cpf TEXT NOT NULL,
        PRIMARY KEY(preso1_cpf, preso2_cpf),
        FOREIGN KEY(preso1_cpf) REFERENCES PRESO(cpf) ON DELETE CASCADE,
        FOREIGN KEY(preso2_cpf) REFERENCES PRESO(cpf) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS CONSULTA (
        preso_cpf TEXT NOT NULL,
        medico_cpf TEXT NOT NULL,
        data DATE NOT NULL,
        prontuario TEXT,
        ocorrencia_cod INTEGER,
        PRIMARY KEY(preso_cpf, medico_cpf, data),
        FOREIGN KEY(preso_cpf) REFERENCES PRESO(cpf),
        FOREIGN KEY(medico_cpf) REFERENCES MEDICO(cpf),
        FOREIGN KEY(ocorrencia_cod) REFERENCES OCORRENCIA(cod)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS ENVOLVIDO (
        preso_cpf TEXT NOT NULL,
        ocorrencia_cod INTEGER NOT NULL,
        PRIMARY KEY(preso_cpf, ocorrencia_cod),
        FOREIGN KEY(preso_cpf) REFERENCES PRESO(cpf),
        FOREIGN KEY(ocorrencia_cod) REFERENCES OCORRENCIA(cod)
    );
    """
]
