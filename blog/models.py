from django.db import models
from django.db.models import BigAutoField, CharField, TextField, ForeignKey, CASCADE


class Post(models.Model):
    id = BigAutoField(primary_key=True, unique=True)
    title = CharField(max_length=120)
    lead = TextField(max_length=500)


class PostBody(models.Model):
    id = BigAutoField(primary_key=True, unique=True)
    post = ForeignKey(Post, on_delete=CASCADE, to_field='id')
    paragraph_body = TextField(max_length=500)
