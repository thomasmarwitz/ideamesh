# Generated by Django 4.2.8 on 2023-12-28 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenAlexConcept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concepts', to='explore.work')),
            ],
        ),
        migrations.RenameField(
            model_name='element',
            old_name='element',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='llamaconcept',
            old_name='concept',
            new_name='name',
        ),
        migrations.DeleteModel(
            name='OAConcept',
        ),
    ]
