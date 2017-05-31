from django.contrib import admin
from .models import Post, Comment
# Register your models here.

# Para hacer nuestro modelo visible en la página del
# administrador, tenemos que registrar el modelo con
admin.site.register(Post)
admin.site.register(Comment)
