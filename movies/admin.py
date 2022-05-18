from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Country,OBT, Plane,Ship, Rocket,Weapon, Ammunition, Artillery, Request


admin.site.register(Country)
admin.site.register(OBT)
admin.site.register(Plane)
admin.site.register(Ship)
admin.site.register(Rocket)
admin.site.register(Weapon)
admin.site.register(Ammunition)
admin.site.register(Artillery)
admin.site.register(Request)




