from django.contrib import admin

from .models import Subscribe


admin.site.site_header = "Balita Admin Panel!"
admin.site.site_title = "Balita Admin Panel!"
admin.site.index_title = "Welcome to the Balita Admin Panel!"


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'email',
        'url',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'email',
        'url',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
    )
