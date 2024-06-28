from django.http import HttpResponse
from rest_framework import viewsets
from .models import Cliente, Habitacion, Reserva, Servicio, ServicioReserva, Evento, ReservaEvento
from .serializers import ClienteSerializer, HabitacionSerializer, ReservaSerializer, ServicioSerializer, ServicioReservaSerializer, EventoSerializer, ReservaEventoSerializer

def home(request):
    return HttpResponse("Bienvenido a la API de Hotelería. Navega a /core/api/clientes/ para ver la lista de clientes.") 

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioReservaViewSet(viewsets.ModelViewSet):
    queryset = ServicioReserva.objects.all()
    serializer_class = ServicioReservaSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class ReservaEventoViewSet(viewsets.ModelViewSet):
    queryset = ReservaEvento.objects.all()
    serializer_class = ReservaEventoSerializer
