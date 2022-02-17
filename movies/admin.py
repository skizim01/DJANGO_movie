from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Students, Techers, Specialty

admin.site.register(Category)
admin.site.register(Students)
admin.site.register(Techers)
admin.site.register(Specialty)




