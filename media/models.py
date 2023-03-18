from django.db import models
from django.contrib.auth.models import User
import datetime

now = datetime.datetime.now()

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_user')
    following_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Following_user')


class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now)


class Like(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500) 


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
