from django.contrib import admin

from blog.models import Article, ArticleParagraph, Tag, ParagraphType


admin.site.register(Article)
admin.site.register(ArticleParagraph)
admin.site.register(Tag)
admin.site.register(ParagraphType)
