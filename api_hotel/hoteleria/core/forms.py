from django import forms
from .models import Cliente, Habitacion, Reserva, Servicio, ServicioReserva, Evento, ReservaEvento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['numero_habitacion', 'tipo_habitacion', 'precio_por_noche', 'descripcion']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'habitacion', 'fecha_reserva', 'fecha_inicio', 'fecha_fin', 'estado']

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre_servicio', 'descripcion', 'precio']

class ServicioReservaForm(forms.ModelForm):
    class Meta:
        model = ServicioReserva
        fields = ['reserva', 'servicio', 'cantidad']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre_evento', 'capacidad', 'precio', 'descripcion']

class ReservaEventoForm(forms.ModelForm):
    class Meta:
        model = ReservaEvento
        fields = ['evento', 'cliente', 'fecha_reserva', 'fecha_evento', 'estado']