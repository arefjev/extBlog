from django.contrib.auth.models import User
from django.db import models
from django.db.models import AutoField, BigAutoField, CharField, TextField, ForeignKey, CASCADE, ManyToManyField
from django.utils.lorem_ipsum import paragraph


class Article(models.Model):
    """
        Stores a single Article entry, related to `auth.User` Model.
    """
    id = BigAutoField(primary_key=True, unique=True)
    title = CharField(max_length=140)
    lead_paragraph = TextField(max_length=1000)
    owner = ForeignKey(User, on_delete=CASCADE, to_field='id')

    class Meta:
        db_table = 'articles'
        verbose_name = 'Blog Article'
        verbose_name_plural = 'Blog Articles'

    def __str__(self):
        return self.title


class ArticleParagraph(models.Model):
    """
        Stores a Article paragraphs, related to `blog.Article` Model.
    """
    id = BigAutoField(primary_key=True, unique=True)
    article = ForeignKey(Article, on_delete=CASCADE, to_field='id')
    paragraph = TextField(max_length=1000)

    class Meta:
        db_table = 'article_paragraphs'
        verbose_name = 'Article Paragraph'
        verbose_name_plural = 'Articles Paragraphs'

    def __str__(self):
        return self.article.title


class Tag(models.Model):
    """
        Stores a Article Tags, related to `blog.Article` Model by M2M relations.
    """
    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=50)
    article = ManyToManyField(Article, blank=True)

    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class ParagraphType(models.Model):
    """
        Stores a Type of paragraph (describes a type of article paragraph, name of template in 'templates' directory).
    """
    id = AutoField(primary_key=True, unique=True)
    paragraph_type = CharField(max_length=50)
    paragraph = ManyToManyField(ArticleParagraph, blank=True)

    class Meta:
        db_table = 'paragraph_types'
        verbose_name = 'Paragraph Type'
        verbose_name_plural = 'Paragraph Types'

    def __str__(self):
        return self.paragraph_type
