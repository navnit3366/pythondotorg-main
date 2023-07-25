# Generated by Django 2.0.13 on 2020-10-15 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sponsors", "0004_auto_20201014_1622"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sponsorshipbenefit", old_name="value", new_name="internal_value"
        ),
        migrations.AddField(
            model_name="sponsorshipbenefit",
            name="capacity",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="For benefits with limited capacity, set it here.",
                null=True,
                verbose_name="Capacity",
            ),
        ),
        migrations.AddField(
            model_name="sponsorshipbenefit",
            name="internal_description",
            field=models.TextField(
                blank=True,
                help_text="Any description or notes for internal use.",
                null=True,
                verbose_name="Internal Description or Notes",
            ),
        ),
        migrations.AlterField(
            model_name="sponsorshipbenefit",
            name="internal_value",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Value used internally to calculate sponsorship level when applicants construct their own sponsorship packages.",
                null=True,
                verbose_name="Internal Value",
            ),
        ),
        migrations.AlterField(
            model_name="sponsorshipbenefit",
            name="conflicts",
            field=models.ManyToManyField(
                blank=True,
                help_text="For benefits that conflict with one another,",
                related_name="_sponsorshipbenefit_conflicts_+",
                to="sponsors.SponsorshipBenefit",
                verbose_name="Conflicts",
            ),
        ),
        migrations.AlterField(
            model_name="sponsorshipbenefit",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="For display on generated prospectuses and the website.",
                null=True,
                verbose_name="Benefit Description",
            ),
        ),
        migrations.AlterField(
            model_name="sponsorshipbenefit",
            name="levels",
            field=models.ManyToManyField(
                help_text="What sponsorship levels this benefit is included in.",
                related_name="benefits",
                to="sponsors.SponsorshipLevel",
                verbose_name="Sponsorship Levels",
            ),
        ),
        migrations.AlterField(
            model_name="sponsorshipbenefit",
            name="minimum_level",
            field=models.ForeignKey(
                blank=True,
                help_text="The minimum sponsorship level required to receive this benefit.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sponsors.SponsorshipLevel",
                verbose_name="Minimum Sponsorship Level",
            ),
        ),
        migrations.AlterField(
            model_name="sponsorshipbenefit",
            name="name",
            field=models.CharField(
                help_text="For display in the application form, statement of work, and sponsor dashboard.",
                max_length=1024,
                verbose_name="Benefit Name",
            ),
        ),
        migrations.AlterField(
            model_name="sponsorshipbenefit",
            name="program",
            field=models.ForeignKey(
                help_text="Which sponsorship program the benefit is associated with.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sponsors.SponsorshipProgram",
                verbose_name="Sponsorship Program",
            ),
        ),
    ]
