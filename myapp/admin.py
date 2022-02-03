from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats
from myapp.models import Area

class AreaResource(resources.ModelResource):
    class Meta:
        model = Area
        fields = ('number', 'area', 'cityname')
        import_id_fields = ['number']


class AreaAdmin(ImportExportActionModelAdmin):
    list_display = (
        'number',
        'area',
        'cityname'
    )

    resource_class = AreaResource
    formats = [base_formats.CSV]


admin.site.register(Area, AreaAdmin)
