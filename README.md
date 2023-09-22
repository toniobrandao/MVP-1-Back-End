# Minha API

Este projeto faz parte do MVP do Sprint **Desenvolvimento Full Stack Básico**

O objetivo aqui é elaborar uma API RESTful, implementada em Python e Flask, utilizando
a documentação Swagger.

---

# Organização do Projeto

Este projeto está organizado de acordo com as seguintes estruturas de pastas e arquivos:

# Organização do Projeto

## Pastas

- **models:**

  - Define o modelo do banco de dados e seus relacionamentos. Utilizando a biblioteca SQLAlchemy, classes Python são usadas para definir como o banco de dados será estruturado e organizado. Essas classes Python servem como um modelo para criar tabelas no banco de dados e especificar como elas estão relacionadas entre si.

- **schemas:**

  - Define a estrutura e as regras para converter dados entre dois formatos distintos. Nesse caso, tipos de dados complexos (como objetos Python) e formatos mais simples e transportáveis (objetos ou JSON), tornando a conversão e validação dos dados direta e consistente.

- **resources:**
  - Define as rotas e as views para realizar ações como obter (GET), deletar (DELETE), atualizar (PUT) e criar (POST) os dados. Ele utiliza Flask-Smorest e o SQLAlchemy para interagir com o banco de dados. Além disso, há também o arquivo `documentation.py`, responsável por redirecionar o usuário para a página da documentação da API.

## Arquivos fora de pastas

- **app.py:**

  - Arquivo em Python para criar a aplicação Flask que serve como uma REST API. O arquivo utiliza algumas extensões do Flask e configurações para configurar a API e sua documentação.

- **app_setup.py:**

  - Script em Python que carrega os dados iniciais da tabela packs utilizando o SQLAlchemy, para o caso da tabela estar vazia.

## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000](http://localhost:5000) no navegador para verificar o status da API em execução.
