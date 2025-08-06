# Projeto de Banco de Dados - CIn/UFPE

Este projeto foi desenvolvido como parte da disciplina de **Banco de Dados** do Centro de Informática (CIn) da Universidade Federal de Pernambuco (UFPE).

## 💡 Descrição

O sistema simula um ambiente prisional, permitindo interações com o banco de dados por meio de uma interface em linha de comando (CLI). A base de dados utilizada é um arquivo SQLite já incluso no repositório (`prisional.db`).

O projeto permite executar operações como inserção, atualização e consulta de dados relacionados ao sistema prisional, seguindo o modelo lógico e relacional descrito nos documentos PDF anexos.

## 🚀 Como executar

> ⚠️ O projeto não possui dependências externas. Apenas Python 3 é necessário.

1. Clone o repositório:

   ```bash
   git clone https://github.com/ausikek/projeto-bd.git
   cd projeto-bd
   ```

2. Execute o sistema:

   ```bash
   python run.py
   ```

## 📁 Estrutura do projeto

- `run.py`: ponto de entrada principal do sistema.
- `cli/`: contém os comandos de linha de comando (interface do usuário).
- `database/`: scripts de conexão e manipulação do banco de dados SQLite.
- `scripts/`: scripts auxiliares, possivelmente para popular o banco ou testes.
- `prisional.db`: banco de dados SQLite com dados de exemplo.
- `Projeto Lógico BD.pdf`: diagrama de modelagem lógica do banco.

## 🧩 Funcionalidades

- Consultas.
- Interface em terminal.
- Banco de dados pronto para uso (SQLite).

## 📚 Requisitos

- Python 3.x
- Sistema operacional com suporte a execução de scripts `.py` no terminal.

## 🧑‍💻 Autores

- Arthur Rocha
- Breno Filho
- Danilo Barrote
- Guilherme Siqueira
- João Pedro Pontes

## 📄 Licença

Este projeto é de uso acadêmico e não possui licença definida.
