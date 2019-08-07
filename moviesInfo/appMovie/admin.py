from django.contrib import admin
from .models import Genre, Movie
# Register your models here.
 
admin.site.register(Genre)
admin.site.register(Movie)
# user.has_perm(blog.can_publish_blog)