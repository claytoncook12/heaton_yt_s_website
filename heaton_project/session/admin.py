from django.contrib import admin
from .models import tune_type, tune, session, played_tune_group
from .models import key, played_tune, name_yer_tune, tune_of_the_month

# Create Ordering For Admin Panel
class tune_admin(admin.ModelAdmin):
    ordering = ['name1']

# Register your models here.
admin.site.register(tune_type)
admin.site.register(tune, tune_admin)
admin.site.register(session)
admin.site.register(played_tune_group)
admin.site.register(key)
admin.site.register(played_tune)
admin.site.register(name_yer_tune)
admin.site.register(tune_of_the_month)