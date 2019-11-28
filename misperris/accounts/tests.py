from django.test import TestCase
from blog.models import Mascotas, Usuario , Region, Ciudad
from django.contrib.auth.models import User

# Create your tests here.

class TesteoMascotas(TestCase):

    def setUp(self):
        Mascotas.objects.create(nombre= "fabritzio", raza = "hash puppys", descripcion = "bonito", estado= "ADOPTADO")
        Mascotas.objects.create(nombre= "ANABELLO", raza = "hash puppys", descripcion = "FEO", estado = "RESCATADO")

    def test_mascota_nombre(self):
        mascota = Mascotas.objects.get(nombre ="fabritzio")
        self.assertEqual(mascota.nombre, "fabritzio")

class TesteoUsuarios(TestCase):
    def setUp(self):
        region = Region.objects.create(nombre= "Valparaiso")
        ciudad = Ciudad.objects.create(region=region,nombre="Nogales")
        user = User.objects.create(username="over")
        Usuario.objects.create(rut ="19338450-2", nombre_completo = "anaz zaurio", fecha_nacimiento="1990-01-01", telefono="9888323", email ="anacleto@gmail.com", tipo_vivienda="PATIO_GRANDE",author=user)

    def test_usuario_fk(self):
        usuario = Usuario.objects.get(rut="19338450-2")
        self.assertEqual(usuario.author.username,"over")

    
