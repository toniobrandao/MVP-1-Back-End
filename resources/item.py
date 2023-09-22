from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import ItemModel
from sqlalchemy.exc import SQLAlchemyError


from models.db import db
from schemas.schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", "items", description="Operações nos itens")


@blp.route("/item/<int:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        """Faz a busca de um item a partir do ID informado."""
        item = ItemModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        """Deleta um item a partir do ID informado."""
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}

    @blp.response(200, ItemSchema)
    @blp.arguments(ItemUpdateSchema)
    def put(self, item_data, item_id):
        """Edita um item a partir de seu ID informado."""
        item = ItemModel.query.get_or_404(item_id)
        if item:
            if "quantity" in item_data:
                item.quantity = item_data["quantity"]
            if "name" in item_data:
                item.name = item_data["name"]
            if "category" in item_data:
                item.category = item_data["category"]
            if "is_packed" in item_data:
                item.is_packed = item_data["is_packed"]
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        """Faz a busca de todos os items cadastrados"""
        return ItemModel.query.all()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        """Adiciona um novo item à base de dados"""
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error ocurred while inserting the item.")
        return item
