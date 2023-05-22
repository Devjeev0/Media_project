from django.contrib import admin
from .models import *

admin.site.register(room_model)
admin.site.register(timing_model)
admin.site.register(team_model)