from django.db import models

class CustomUser(models.Model):
    """
    Custom user model:
        - `type` [bool] - 0 for buyer, 1 for seller
    """
    type = models.BooleanField()
