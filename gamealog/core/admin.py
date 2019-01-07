from django.contrib import admin
from core.models import Game, Console


class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'console')

admin.site.register(Game, GameAdmin)

class ConsoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'media_type', 'memory_type')

admin.site.register(Console, ConsoleAdmin)