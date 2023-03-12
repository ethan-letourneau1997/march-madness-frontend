from django.contrib import admin
from django.apps import apps

from draft.forms import PeopleAdminForm


from .models import Player, Group, People
# Register your models here.

app_config = apps.get_app_config('draft')
models = app_config.get_models()


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    form = PeopleAdminForm


for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
