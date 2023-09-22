from models.db import db
from models import PackModel


def create_initial_packs():

    # Checa se a tabela está vazia, caso esteja, carrega os dados iniciais das stores (categorias).
    pack_count = db.session.query(PackModel).count()
    if pack_count == 0:
        initial_pack_data = [
            {"name": "Acampamento"},
            {"name": "AirBnb"},
            {"name": "Casa de Amigo"},
            {"name": "Casa de Campo"},
            {"name": "Casa de Praia"},
            {"name": "Hostel"},
            {"name": "Hotel"},
            {"name": "Resort"}
        ]

        try:
            for pack_data in initial_pack_data:
                pack = PackModel(**pack_data)
                db.session.add(pack)

            db.session.commit()
            print("Initial packs added successfully.")
        except Exception as e:
            db.session.rollback()
            print("Error adding initial packs:", e)
