from django.db import models
from django.contrib.auth.models import User

class info(models.Model):
    email = models.EmailField('email',max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('name',max_length=250)
    age = models.IntegerField('age',default=0)
    mobile = models.CharField('mobile',max_length=10)
    reg = models.CharField('reg',max_length=250)

    def __str__(self):
        return self.user.username
class patient(models.Model):
    id = models.AutoField('id',primary_key=True)
    name = models.CharField('name',max_length=250)
    mobile = models.IntegerField('mob',max_length=10)
    userrname = models.CharField('user',max_length=250)
    age = models.IntegerField('age')
    city = models.CharField('city',max_length=10)

    def __int__(self):
        return self.id
class prescription(models.Model):
    id = models.AutoField('ID',primary_key=True)
    pid = models.ForeignKey(patient,on_delete=models.CASCADE)
    name = models.CharField('name',max_length=250)
    mobile = models.IntegerField('mob',max_length=10)
    date = models.DateField('date')
    dis = models.CharField('dis',max_length=250)
    med = models.CharField('med',max_length=2000)
    username = models.CharField('username',max_length=250)

    def __int__(self):
        return self.id


