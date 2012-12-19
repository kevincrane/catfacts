from django.db import models


# Contains info about the lucky CatFact email recipient
class Email_User(models.Model):
    name = models.CharField(max_length=50)
    date_joined = models.DateTimeField('date joined')
    email = models.CharField(max_length=50)
    valid = models.BooleanField()

    class Meta:
        verbose_name = 'User (Email)'
        verbose_name_plural = 'Users (Email)'

    def __unicode__(self):
        return self.name + " (" + self.email + ")"


# Contains info about the lucky CatFact SMS recipient
class Phone_User(models.Model):
    name = models.CharField(max_length=50)
    date_joined = models.DateTimeField('date joined')
    phone = models.CharField(max_length=30)
    valid = models.BooleanField()

    class Meta:
        verbose_name = 'User (Phone)'
        verbose_name_plural = 'Users (Phone)'

    def __unicode__(self):
        return self.name + " (" + self.phone + ")"


# Contains a list of all entered CatFacts
class Fact(models.Model):
    fact = models.CharField(max_length=300)
    date_created = models.DateTimeField('date created')
    used = models.BooleanField(default=False)
    date_used = models.DateTimeField('date used')

    def __unicode__(self):
        return self.fact