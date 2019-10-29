from django.contrib import admin
from Flash.models import Deck, Card


class CardInline(admin.TabularInline):
    model = Card
    extra = 0


class DeckAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'number_of_cards',
        'created_at',
    )

    inlines = [CardInline]


class CardAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'created_at',
    )


admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
