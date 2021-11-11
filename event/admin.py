from django.contrib import admin

from .models import EventUsersData


@admin.register(EventUsersData)
class EventUsersDataAdmin(admin.ModelAdmin):

    readonly_fields = ('date_time', 'total_user',)
    fields = (
        'date_time', 'weight_user', 'age_user', 'total_user',
        'text_a', 'text_b', 'description', 'status')
    list_display = (
        '__str__', 'date_time', 'weight_user', 'age_user', 'total_user',
        'text_a', 'text_b', 'description', 'status')
