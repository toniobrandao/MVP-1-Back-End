import os

# Essa biblioteca seá usada para habilitar o uso da API por multiplas origens.
from flask_cors import CORS

from flask import Flask

# A classe Api é um componente fundamental do Flask-Smorest e é usada para criar e gerenciar sua aplicação API,
#  incluindo registro de recursos, tratamento de rotas e geração de documentação.
from flask_smorest import Api
from models.db import db

from resources.item import blp as ItemBlueprint
from resources.pack import blp as PackBlueprint
from resources.documentation import blp as DocumentationBlueprint

from app_setup import create_initial_packs


def create_app(db_url=None):
    app = Flask(__name__)

    CORS(app)
    CORS(app, origins="*")
    # Configurando a Documentação da API.
    # Se algo der errado na API, deixe o Flask lidar com o erro como costuma fazer.
    app.config["PROPAGATE_EXCEPTIONS"] = True

    # Dê um nome à sua API que aparecerá na documentação.
    app.config["API_TITLE"] = "Packs REST API"

    # Informe aos usuários qual versão da API eles estão usando.
    app.config["API_VERSION"] = "v1"

    # Descreva sua API usando uma versão específica de um formato padrão.
    app.config["OPENAPI_VERSION"] = "3.0.3"

    # Coloque a documentação da sua API no URL principal.
    app.config["OPENAPI_URL_PREFIX"] = "/"

    # Acesse a documentação interativa em um determinado URL.
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"

    # Obtenha o design e o layout da documentação de um local específico na internet.
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # Definindo o local e o tipo de banco de dados a ser usado pela aplicação.
    # A configuração da aplicação está sendo definida como o caminho para um banco de dados SQLite chamado "data.db".
    # os.getenv --> recupera o valor da variável de ambiente "DATABASE_URL" e, caso não seja encontrado,
    #  utiliza o valor padrão "sqlite://data.db".
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Conectando o Fask App ao SQLAlchemy
    db.init_app(app)

    # Conectando a classe API para configurar e gerenciar o comportamento,
    # endpoints, validação e documentação da API

    api = Api(app)

    # criando todas as tabelas definidas no banco de dados usando o contexto de aplicativo atual.
    with app.app_context():
        db.create_all()
        # iniciando os dados iniciais da tabela.
        create_initial_packs()

    api.register_blueprint(DocumentationBlueprint)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(PackBlueprint)

    return app
