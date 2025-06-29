from django.db import models


# Create your models here.

class enquiry_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name








from django.core.serializers.json import DjangoJSONEncoder

class customplan(models.Model):
    contact_no = models.CharField(max_length=20,unique=True)
    chest = models.JSONField(encoder=DjangoJSONEncoder)
    triceps = models.JSONField(encoder=DjangoJSONEncoder)
    shoulder = models.JSONField(encoder=DjangoJSONEncoder)
    back = models.JSONField(encoder=DjangoJSONEncoder)
    biceps = models.JSONField(encoder=DjangoJSONEncoder)
    legs = models.JSONField(encoder=DjangoJSONEncoder)


    
    def __str__(self):
        return f"Order for {self.contact_no}"

class register_users(models.Model):
    # id = models.CharField(max_length=10, default='default_id', primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10,unique=True)
    password = models.EmailField(max_length=255)
    gender = models.EmailField(max_length=255)
    dob = models.EmailField(max_length=255)
    def __str__(self):
        return self.name

class verified_users(models.Model):
    # id = models.CharField(max_length=10, default='default_id', primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10,unique=True)
    password = models.EmailField(max_length=255)
    gender = models.EmailField(max_length=255)
    dob = models.EmailField(max_length=255)
    def __str__(self):
        return self.name