from marshmallow import Schema, fields


# Código organizado em Plain__Schema e Schema.
# Motivo: como vamos incorporar dados das packs na tabela de items e dados de items na tabela de packs,
# precisamos ter schemas de items sem as packs e schemas de packs sem os items. Caso contrário,
# entraríamos em um loop de o item ter pack --> a pack do item ter item e assim
# por diante.

class PlainItemSchema(Schema):

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    quantity = fields.Int(required=True)
    category = fields.Str(required=True)
    is_packed = fields.Bool(required=True)


class PlainPackSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    quantity = fields.Int()
    category = fields.Str()
    is_packed = fields.Bool()


class ItemSchema(PlainItemSchema):
    pack_id = fields.Int(required=True, load_only=True)
    pack = fields.Nested(PlainPackSchema(), dump_only=True)


class PackSchema(PlainPackSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
