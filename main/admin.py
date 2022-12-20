from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Section
# Register your models here.
admin.site.register(Section, SingletonModelAdmin)