from django.db import models

class Work(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    doi = models.CharField(max_length=100)
    display_name = models.CharField(max_length=255)
    publication_date = models.DateField()
    abstract = models.TextField()

    def __str__(self):
        return self.display_name

class LlamaConcept(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='llama_concepts')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class OpenAlexConcept(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='concepts')
    name = models.CharField(max_length=255)
    score = models.FloatField()
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Element(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='elements')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
