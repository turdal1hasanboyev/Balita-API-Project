from django.contrib import admin

from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    '''
    '__all__' ishlamaydi
    '''
    list_display = (
        'id',
        'name',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
    )
    ordering = ('id',)
    search_fields = (
        'name',
    )
