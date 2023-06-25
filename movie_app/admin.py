from django.contrib import admin, messages
from .models import *
from django.db.models import QuerySet



class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'currency', 'rating', 'budget', 'year', 'test', 'rating_status']
    list_editable = ['budget', 'rating', 'currency']
    ordering = ['-rating', 'name']
    list_per_page = 9
    actions = ['set_dollars']

    @admin.display(ordering='rating', description='Рейтинг')
    def rating_status(self, movie):
        if movie.rating:
            if movie.rating < 50:
                return 'Зачем это смотреть?'
            elif movie.rating < 80:
                return 'Разок можно глянуть.'
            elif movie.rating >= 80:
                return 'Топчик'
        else:
            return 'Пока непонятно...'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs:QuerySet):
        count_updated = qs.update(currency=Movie.D)
        self.message_user(request,
                          f'Количество обновленных записей - {count_updated}',
                          level=messages.WARNING,)


admin.site.register(Movie, MovieAdmin)