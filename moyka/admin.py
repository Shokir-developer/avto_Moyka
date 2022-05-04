from django.contrib import admin
from .models import Mijoz

class MijozAdmin(admin.ModelAdmin):
	list_display = ['nomer', 'date']
	search_fields = ['nomer']

admin.site.register(Mijoz, MijozAdmin)
# Register your models here.
