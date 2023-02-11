from django.db import models

# Create your models here.




GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)

class Materials(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class SubDistrict(models.Model):
    name = models.CharField(max_length=100, unique=True)
    district = models.ForeignKey(District, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class AccountApplication(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    district = models.ForeignKey(District, null=True, blank=True, on_delete=models.PROTECT)
    branch = models.ForeignKey(SubDistrict, null=True, blank=True, on_delete=models.PROTECT)
    account_type = models.ForeignKey(AccountType, null=True, blank=True, on_delete=models.PROTECT)
    materials_provide = models.ManyToManyField(Materials, null=True, blank=True)

    def __str__(self):
        return self.name
