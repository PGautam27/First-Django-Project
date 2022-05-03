from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122, null=True, default="gautam")
    email = models.CharField(max_length=122, null=True, default="gautam@gmail.com")
    phone = models.CharField(max_length=10, null=True, default=1234567895)
    desc = models.TextField(null=True)
    date = models.DateField()
