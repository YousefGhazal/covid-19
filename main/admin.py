from django.contrib import admin
from solo.admin import SingletonModelAdmin
from ordered_model.admin import OrderedModelAdmin
from .models import Announcements, Heading
# Register your models here.
admin.site.register(Heading, SingletonModelAdmin)
class AnnouncementsAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')

admin.site.register(Announcements, AnnouncementsAdmin)