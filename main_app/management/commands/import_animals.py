import json
from django.core.management.base import BaseCommand, CommandError
from main_app.models import Animal

class Command(BaseCommand):
    help = 'Imports animals from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='../../../transformed_data_output.json')

    def handle(self, *args, **options):
        try:
            with open(options['json_file'], 'r') as file:
                animals_data = json.load(file)

            for item in animals_data:
                Animal.objects.create(
                    name=item["name"],
                    type=item["type"],
                    breed=item["breed"],
                    age=item["age"],
                    size=item["size"],
                    gender=item["gender"],
                    color=item["color"],
                    status=item["status"],
                    location=item["location"],
                    description=item.get("description", ""),
                    photos=item["photos"],
                    contact=item["contact"]
                )
            self.stdout.write(self.style.SUCCESS('Successfully imported animal data'))
        except FileNotFoundError:
            raise CommandError('File "%s" does not exist' % options['json_file'])
        except Exception as e:
            raise CommandError('Error importing animal data: %s' % str(e))
