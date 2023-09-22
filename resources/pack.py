from models.db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from models import PackModel
from schemas.schemas import PackSchema

blp = Blueprint("Packs", "packs", description="Operações nos packs")


@blp.route("/pack/<int:pack_id>")
class Pack(MethodView):

    @blp.response(200, PackSchema)
    def get(self, pack_id):
        """Faz a busca do pack a partir do ID informado."""
        pack = PackModel.query.get_or_404(pack_id)
        return pack

    def delete(self, pack_id):
        """Deleta o pack a partir do ID informado."""
        pack = PackModel.query.get_or_404(pack_id)
        db.session.delete(pack)
        db.session.commit()
        return {"message": "Pack deleted."}


@blp.route("/pack")
class PackList(MethodView):
    @blp.response(200, PackSchema(many=True))
    def get(self):
        """Faz a busca de todos os packs cadastrados."""
        return PackModel.query.all()

    @blp.arguments(PackSchema)
    @blp.response(201, PackSchema)
    def post(self, pack_data):
        """Adiciona um novo pack à base de dados."""
        pack = PackModel(**pack_data)
        try:
            db.session.add(pack)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A pack with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the pack.")

        return pack
