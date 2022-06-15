# Desafio Engenheiro de Dados Jr. 


- [Desafio Engenheiro de Dados Jr](#desafio-engenheiro-de-dados-jr)
  - [Informação do Candidato](#informação-do-candidato)
- [Sobre o Desafio](#sobre-o-desafio)
  - [Considerações do Candidato](#considerações-do-candidato)
  - [Arquitetura da proposta](#arquitetura-da-proposta)
  - [Discussão de Arquitetura](#discussão-de-arquitetura)
   - [Modelagem de dados](#modelagem-de-dados)
   - [Arquivo JSON](#arquivo-json)
   - [Google Sheets](#google-sheets)

## Informação do Candidato

| Proprietária        | Contato de e-mail         |
|---------------------|---------------------------|
| Nayara Bernardo     | nayyarabernardo@gmail.com |

## Sobre o Desafio

### Considerações do Candidato 

Seguindo as diretrizes do desafio que foi solicitado no email

Foi criado uma solução para enviar estes dados para uma planilha no Google Sheets

Além disso, compartilhar o arquivo Git junto com o Sheets final e pôr no repositório os arquivos da automação;

### Arquitetura da proposta

IMAGEM DECOMO VOU FAZER

### Discussão de Arquitetura

#### Modelagem de dados

*O conjunto de dados é sobre viagens Uber. Ele contém a região, coordenadas de origem, coordenadas de destino, um campo de timestamp sobre quando aconteceu e qual carro compareceu a essa viagem.

Como as perguntas do desafio são orientadas ao tempo (por exemplo, quantas viagens semanais ocorreram para uma determinada região) e os registros não têm nenhum identificador de chave exclusivo, decidi modelar os dados de forma **série temporal**.*

#### Arquivo JSON

Postgres TimescaleDB é o banco de dados relacional de código aberto líder com suporte para dados de séries temporais. Ele oferece muitos benefícios, como:XXX

#### Google Sheets

Postgres TimescaleDB é o banco de dados relacional de código aberto líder

