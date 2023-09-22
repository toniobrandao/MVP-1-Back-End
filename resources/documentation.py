from flask import redirect

from flask_smorest import Blueprint

blp = Blueprint("Documentation", "documentation",
                description="Documentação da API")


@blp.route("/")
def home():
    """Redireciona para /swagger-ui, com a documentação da API em Swagger.
    """
    return redirect("/swagger-ui")
