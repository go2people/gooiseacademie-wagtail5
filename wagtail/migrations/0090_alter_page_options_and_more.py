# Generated by Django 4.2.4 on 2023-08-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'permissions': [('bulk_delete_page', 'Delete pages with children'), ('view', 'View any page'), ('lock_page', "Lock/unlock pages you've locked"), ('publish_page', 'Publish any page'), ('unlock_page', 'Unlock any page')], 'verbose_name': 'page', 'verbose_name_plural': 'pages'},
        ),
        migrations.AlterField(
            model_name='grouppagepermission',
            name='permission_type',
            field=models.CharField(blank=True, choices=[('add', 'Add/edit pages you own'), ('bulk_delete', 'Delete pages with children'), ('change', 'Edit any page'), ('', 'View any page'), ('lock', "Lock/unlock pages you've locked"), ('publish', 'Publish any page'), ('unlock', 'Unlock any page')], max_length=20, null=True, verbose_name='permission type'),
        ),
    ]
