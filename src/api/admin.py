from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext, gettext_lazy as _

from .models import (
    Predication
)


class PredicationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('user', 'file', 'pitch')}),
    )
    list_display = ['pk', 'user', 'is_active', 'created_on']
    list_filter = ['is_active']


admin.site.register(Predication, PredicationAdmin)
