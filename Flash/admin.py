from django.contrib import admin
from Flash.models import Deck, Card, User


class CardInline(admin.TabularInline):
    model = Card
    extra = 0

class DeckInLine(admin.TabularInline):
    model = Deck


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

class UserAdmin(admin.ModelAdmin):
    inlines = [
        DeckInLine,
    ]

admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(User,UserAdmin)
