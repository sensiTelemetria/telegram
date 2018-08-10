from django.contrib import admin

# Register your models here.

from alarmes.models import alarme
from tags.models import tag
from usuarios.models import usuario

class alarmeAdmin(admin.ModelAdmin):
    pass

class tagAdmin(admin.ModelAdmin):
    pass

class usuarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(alarme,alarmeAdmin)
admin.site.register(tag,tagAdmin)
admin.site.register(usuario,usuarioAdmin)