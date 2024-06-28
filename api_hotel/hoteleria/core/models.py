from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Habitacion(models.Model):
    numero_habitacion = models.CharField(max_length=10)
    tipo_habitacion = models.CharField(max_length=50)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.numero_habitacion

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=50, default='pendiente')

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente}"

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_servicio

class ServicioReserva(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.servicio.nombre_servicio}"

class Evento(models.Model):
    nombre_evento = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_evento

class ReservaEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    fecha_evento = models.DateField()
    estado = models.CharField(max_length=50, default='pendiente')

    def __str__(self):
        return f"Reserva de Evento {self.id} - {self.evento.nombre_evento}"