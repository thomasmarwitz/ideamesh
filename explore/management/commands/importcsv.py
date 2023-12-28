import csv
import datetime
from explore.models import Work, LlamaConcept, OpenAlexConcept, Element
from ast import literal_eval
from tqdm import tqdm

from django.core.management.base import BaseCommand

from django.db import transaction

class Command(BaseCommand):
    help = 'Import data from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
        parser.add_argument('--n-rows', type=int, default=None, required=False)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        n_rows = options['n_rows']
        self._import_csv_to_db(csv_file_path, n_rows)
        self.stdout.write(self.style.SUCCESS('Successfully imported data from "%s"' % csv_file_path))

    def _import_csv_to_db(self, csv_file_path, n_rows=None, batch_size=30_000):
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            with transaction.atomic():
                works = []
                llama_concepts = []
                openalex_concepts = []
                elements = []

                for row_number, row in tqdm(enumerate(reader)):
                    if n_rows is not None and row_number >= n_rows:
                        break

                    work = Work(
                        id=row['id'],
                        doi=row['doi'],
                        display_name=row['display_name'],
                        publication_date=datetime.datetime.strptime(row['publication_date'], '%Y-%m-%d').date(),
                        abstract=row['abstract']
                    )
                    works.append(work)

                    for concept in literal_eval(row['llama_concepts']):
                        llama_concepts.append(LlamaConcept(work=work, name=concept))

                    for concept, level, score in literal_eval(row['concepts']):
                        openalex_concepts.append(OpenAlexConcept(work=work, name=concept, level=level, score=score))

                    for element in row['elements'].split(','):
                        elements.append(Element(work=work, name=element))
                
                    if row_number % batch_size == 0:
                        Work.objects.bulk_create(works)
                        LlamaConcept.objects.bulk_create(llama_concepts)
                        OpenAlexConcept.objects.bulk_create(openalex_concepts)
                        Element.objects.bulk_create(elements)

                        works = []
                        llama_concepts = []
                        openalex_concepts = []
                        elements = []

                # Insert the remaining rows
                Work.objects.bulk_create(works)
                LlamaConcept.objects.bulk_create(llama_concepts)
                OpenAlexConcept.objects.bulk_create(openalex_concepts)
                Element.objects.bulk_create(elements)
