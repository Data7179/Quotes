from django.contrib import admin
from .models import Quote

# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
    list_display = ("quote", "id",  "user")
    search_fields = ("user", )
    list_filter = ("user", )
    
admin.site.register(Quote, QuoteAdmin)
