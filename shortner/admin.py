from django.contrib import admin
from .models import URL
class URLAdmin(admin.ModelAdmin):
    fields = ['full_url', 'short_url', 'clicks']
    list_display = ('full_url','short_url','clicks')
admin.site.register(URL)