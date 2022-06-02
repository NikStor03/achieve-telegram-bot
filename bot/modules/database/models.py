import tortoise
from tortoise import fields


class UsersModel:

    id = fields.BigIntField(pk=True)
    achieves = fields.ManyToManyField('models.AchievesModel')
    created_at = fields.DatetimeField(auto_now=True)
    premium = fields.ForeignKeyField('models.PremiumsModel')
    region = fields.ForeignKeyField('models.RegionsModel')

    def __str__(self):
        return str(self.id)


class RegionsModel:

    name = fields.CharField(max_length=256)

    def __str__(self):
        return str(self.name)


class PremiumsPricesModel:

    price = fields.FloatField()

    def __str__(self):
        return str(self.price)


class PremiumsModel:

    price = fields.ForeignKeyField('models.PremiumsPricesModel')
    active_at = fields.DatetimeField(auto_now=True)
    deactivate_on = fields.DatetimeField()

    def __str__(self):
        return str(self.active_at)


class AchievesModel:

    name = fields.CharField(max_length=256)
    descriptions = fields.TextField()
    end_at = fields.DatetimeField()
    started_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return str(self.name)