from django.db import models
from django.contrib.auth.models import AbstractUser
import random


class User(AbstractUser):
    pass


class Deck(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="decks",
    )

    subject = models.CharField(
        verbose_name="Subject Name",
        max_length=50,
        blank=False,
        null=True,
    )
    title = models.CharField(
        verbose_name="Deck Title",
        max_length=50,
        blank=False,
    )
    description = models.TextField(
        verbose_name="Deck Description",
        max_length=255,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.subject

    def __str__(self):
        return self.title

    def __str__(self):
        return self.description

    def number_of_cards(self):
        return self.cards.count()
        
    def get_random_card(self):
        random_number = random.randint(0, self.cards.count() - 1)
        random_card = self.cards.all() [random_number]
        return random_card


class Card(models.Model):
    deck = models.ForeignKey(
        to=Deck,
        on_delete=models.CASCADE,
        related_name="cards"
    )
    question = models.TextField(
        verbose_name="Question:",
        max_length=255,
        blank=True,
        null=True,
    )
    answer = models.TextField(
        verbose_name="Answer:",
        max_length=255,
        blank=True,
        null=True,
    )
    total_guesses = models.IntegerField(
        default=0,
    )
    total_correct_guesses = models.IntegerField(
        default=0,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    def __str__(self):
        return self.question

    def __str__(self):
        return self.answer

    def has_previous_card(self):
        first_card_in_deck = self.deck.cards.first()
        if self == first_card_in_deck:
            return False
        return True

    def previous_card(self):
        return self.deck.cards.filter(id__lt=self.pk).last()
    
    def has_next_card(self):
        last_card_in_deck = self.deck.cards.last()
        if self == last_card_in_deck:
            return False
        return True

    def get_next_card(self):
        return self.deck.cards.filter(id__gt=self.pk).first()
