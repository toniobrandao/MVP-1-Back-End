from models.db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    category = db.Column(db.String(80), unique=False, nullable=False)
    is_packed = db.Column(db.Boolean, unique=False, nullable=False)
    # A pack_id é usada como chave estrangeira da coluna id da tabela pack.
    pack_id = db.Column(db.Integer, db.ForeignKey("packs.id"), nullable=False)

    # Define um relacionamento entre a classe ItemModel e a PackModel.
    pack = db.relationship("PackModel", back_populates="items", uselist=False)
