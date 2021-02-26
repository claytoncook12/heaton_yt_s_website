from django.contrib import admin
from .models import tune_type, tune, session, played_tune_group
from .models import key, played_tune, name_yer_tune, tune_of_the_month

# Create Ordering For Admin Panel
class tune_admin(admin.ModelAdmin):
    ordering = ['name1']
class session_admin(admin.ModelAdmin):
    ordering = ['-date']
class played_tune_group_admin(admin.ModelAdmin):
    ordering = ['-session__date','-session_order_num']
class played_tune_admin(admin.ModelAdmin):
    ordering = ['-played_tune_group__session__date','-played_tune_group__session_order_num','-group_order_num']

# Register your models here.
admin.site.register(tune_type)
admin.site.register(tune, tune_admin)
admin.site.register(session, session_admin)
admin.site.register(played_tune_group, played_tune_group_admin)
admin.site.register(key)
admin.site.register(played_tune, played_tune_admin)
admin.site.register(name_yer_tune)
admin.site.register(tune_of_the_month)