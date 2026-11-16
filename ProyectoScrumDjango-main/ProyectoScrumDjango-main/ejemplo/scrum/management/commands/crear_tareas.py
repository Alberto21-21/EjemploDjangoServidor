from django.core.management import BaseCommand
from ...models import Tarea, Etiqueta,Programador

class Command(BaseCommand):
    help = 'Crear tareas de ejemplo'

    def handle(self, *args, **options):


        try:
            etiqueta = Etiqueta(nombre='Etiqueta de ejemplo')
            etiqueta.save()
            self.stdout.write(self.style.SUCCESS(f"Se ha guardado correctamente la etiqueta: {etiqueta.nombre}"))

            programador = Programador(nombre='Programador de ejemplo')
            programador.save()
            tarea = Tarea(nombre='Tarea de ejemplo')
            tarea.save()
            tarea.etiquetas.add(etiqueta)
            tarea.save()
            self.stdout.write(self.style.SUCCESS(f"Tarea creada: {tarea.nombre} con etiqueta: {etiqueta.nombre}"))
        except Exception:
            self.stdout.write(self.style.ERROR("Error al crear la tarea y la etiqueta"))