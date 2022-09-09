from django.contrib import admin
from .models import Clientes
from .models import TipoCalidad
from .models import PreguntasCalidad

# Register your models here.

admin.site.register(Clientes)
admin.site.register(TipoCalidad)
admin.site.register(PreguntasCalidad)