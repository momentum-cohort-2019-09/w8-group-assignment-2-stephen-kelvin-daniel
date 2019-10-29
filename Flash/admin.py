from django.contrib import admin
from Flash.models import Deck, Card


class CardInline(admin.TabularInline):
    model = Card
    extra = 0


class DeckAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'title',
        'description',
        'number_of_cards',
        'updated_at',
        'created_at',
    )
    list_filter = (
        'subject',
    )

    inlines = [CardInline]


class CardAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'updated_at',
        'created_at',
    )


admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
