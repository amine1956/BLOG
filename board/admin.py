from django.contrib import admin
from .models import Board
from .models import Post
from .models import Topic
admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)

# Register your models here.
