from tortoise import fields
from tortoise.models import Model


class UsersModel(Model):

    user_id = fields.BigIntField(unique=True)
    achieves = fields.ManyToManyField('models.AchievesModel')
    created_at = fields.DatetimeField(auto_now=True)
    premium = fields.ForeignKeyField('models.PremiumsModel')

    def __str__(self):
        return str(self.user_id)


class PremiumsPricesModel(Model):

    price = fields.FloatField()

    def __str__(self):
        return str(self.price)


class PremiumsModel(Model):

    price = fields.ForeignKeyField('models.PremiumsPricesModel')
    active = fields.BooleanField(default=False)
    active_at = fields.DatetimeField(default=None, null=True)
    deactivate_on = fields.DatetimeField(default=None, null=True)

    def __str__(self):
        return str(self.active_at)


class AchievesModel(Model):

    name = fields.CharField(max_length=256)
    descriptions = fields.TextField()

    short_name = fields.CharField(max_length=4, null=True)

    end_at = fields.DatetimeField()
    started_at = fields.DatetimeField(auto_now=True)

    daily_aim = fields.FloatField(null=True)
    total_aim = fields.FloatField(null=True)
    today_done = fields.FloatField(null=True)
    total_done = fields.FloatField(null=True)

    def __str__(self):
        return str(self.name)