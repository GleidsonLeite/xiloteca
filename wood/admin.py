from django.contrib import admin

# Register your models here.
from .models import familia, cor, madeira, parenquima,textHome, feedDeNoticias, colaboradores

admin.site.register(familia)
admin.site.register(cor)
admin.site.register(madeira)
admin.site.register(parenquima)
admin.site.register(textHome)
admin.site.register(feedDeNoticias)
admin.site.register(colaboradores)