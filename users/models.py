from django.db import models

class theOffice(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    
class GOT(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class random_user(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name
