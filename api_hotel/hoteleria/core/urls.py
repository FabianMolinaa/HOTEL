from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, HabitacionViewSet, ReservaViewSet, ServicioViewSet, ServicioReservaViewSet, EventoViewSet, ReservaEventoViewSet


router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'servicios-reserva', ServicioReservaViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'reservas-eventos', ReservaEventoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]