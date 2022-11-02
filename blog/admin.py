from django.contrib import admin
from blog.models import Blog, Entry,Author

admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)