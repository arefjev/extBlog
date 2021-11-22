from django.contrib import admin

from blog.models import Post, PostBody


admin.site.register(Post)
admin.site.register(PostBody)
