from django.db import models
from datetime import datetime


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=100)
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/ingredients/'


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/menu/'

    def available(self):
        return all(n.enough() for n in self.reciperequirement_set.all())


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f'{self.menu_item.name} - {self.ingredient.name}'

    def get_absolute_url(self):
        return '/recipes/'

    def enough(self):
        return self.quantity <= self.ingredient.quantity


class Purchase(models.Model):
    purchased_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.today())
    # date = models.DateField(default=datetime.today().date())
    # time = models.TimeField(default=datetime.today().time())

    def __str__(self):
        # return f'{self.date} {self.time}'
        return f'{self.timestamp}'

    def get_absolute_url(self):
        return '/purchases/'

    # def total_cost(self):
    #     return sum([n.price for n in self.purchased_items.all()])


