from django.contrib import admin
from .models import Cliente, Habitacion, Reserva, Servicio, ServicioReserva, Evento, ReservaEvento

admin.site.register(Cliente)
admin.site.register(Habitacion)
admin.site.register(Reserva)
admin.site.register(Servicio)
admin.site.register(ServicioReserva)
admin.site.register(Evento)
admin.site.register(ReservaEvento)