from django.db import models


class Components(models.Model):
    """модель всех компонентов с UI"""
    name = models.CharField("название", max_length=250, null=True)
    