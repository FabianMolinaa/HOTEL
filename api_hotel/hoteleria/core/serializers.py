from rest_framework import serializers
from .models import Cliente, Habitacion, Reserva, Servicio, ServicioReserva, Evento, ReservaEvento

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class ServicioReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioReserva
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class ReservaEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaEvento
        fields = '__all__'
