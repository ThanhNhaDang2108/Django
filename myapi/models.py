from django.db import models

# Create your models here.
class ThanhNha(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=150)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name
    # description = models.TextField()
    # cooking_instructions = models.TextField()
    # slug = models.SlugField()
    # preparation_time = models.IntegerField(help_text='Preparation time in minutes')
    # cooking_time = models.IntegerField(help_text='Cooking time in minutes')
    # created = models.DateTimeField()
    # modified = models.DateTimeField()