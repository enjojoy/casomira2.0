from django.contrib import admin

# Register your models here.

from .models import Person, Aircraft, Flight

admin.site.register(Person)
admin.site.register(Aircraft)
admin.site.register(Flight)
