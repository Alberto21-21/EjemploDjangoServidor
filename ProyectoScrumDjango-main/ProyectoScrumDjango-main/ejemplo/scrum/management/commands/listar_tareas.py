from django.core.management import BaseCommand
from ...models import Tarea

class Command(BaseCommand):
    help = ""

    def handle(self,*args,**options):
        tareas = Tarea.objects.all()

        for tarea in tareas:
            print(f"{tarea.id} {tarea.nombre}")
        self.stdout.write(self.style.SUCCESS("ESTE COMANDO LISTA TODAS LAS TAREAS"))