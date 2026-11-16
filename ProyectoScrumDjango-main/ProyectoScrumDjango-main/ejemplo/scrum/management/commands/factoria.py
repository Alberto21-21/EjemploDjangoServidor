from faker import Faker
from datetime import date
from django.core.management.base import BaseCommand
from ...models import *

class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        faker = Faker('es_ES')
        # Creacion Programadores
        for i in range(10):
            programador = Programador(nombre=faker.name(), apellido=faker.first_name())
            programador.save()

