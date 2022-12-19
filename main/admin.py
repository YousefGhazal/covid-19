from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .config import SiteConfiguration
from .models import Section
# Register your models here.
admin.site.register(SiteConfiguration, SingletonModelAdmin)
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_editable = ['published']
    list_display = ['title', 'published']
    search_fields = ['country']