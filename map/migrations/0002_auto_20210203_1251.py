# Generated by Django 3.1.6 on 2021-02-03 12:51

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=mapbox_location_field.models.LocationField(map_attrs={'center': [74.5698, 42.8746], 'cursor_style': 'hand', 'fullscreen_button': True, 'geocoder': True, 'id': 'unique_id_1', 'marker_color': 'red', 'navigation_buttons': True, 'placeholder': 'Pick a location on map below', 'readonly': True, 'rotate': False, 'style': 'mapbox://styles/mapbox/outdoors-v11', 'track_location_button': True, 'zoom': 10}),
        ),
    ]
