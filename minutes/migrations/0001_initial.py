from django.db import models, migrations
import markupfield.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Minutes',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now, blank=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('date', models.DateField(db_index=True, verbose_name='Meeting Date')),
                ('content', markupfield.fields.MarkupField(rendered_field=True)),
                ('content_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('html', 'html'), ('plain', 'plain'), ('markdown', 'markdown'), ('restructuredtext', 'restructuredtext')], default='restructuredtext')),
                ('is_published', models.BooleanField(db_index=True, default=False)),
                ('_content_rendered', models.TextField(editable=False)),
                ('creator', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='minutes_minutes_creator', blank=True, on_delete=models.CASCADE)),
                ('last_modified_by', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='minutes_minutes_modified', blank=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'minutes',
                'verbose_name_plural': 'minutes',
            },
            bases=(models.Model,),
        ),
    ]
