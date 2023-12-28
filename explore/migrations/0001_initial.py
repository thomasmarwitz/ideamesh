# Generated by Django 4.2.8 on 2023-12-28 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('doi', models.CharField(max_length=100, unique=True)),
                ('display_name', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('abstract', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OAConcept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.CharField(max_length=255)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concepts', to='explore.work')),
            ],
        ),
        migrations.CreateModel(
            name='LlamaConcept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.CharField(max_length=255)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='llama_concepts', to='explore.work')),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element', models.CharField(max_length=255)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='explore.work')),
            ],
        ),
    ]