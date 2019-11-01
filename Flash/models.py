from django.db import models
from django.contrib.auth.models import AbstractUser


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

    def __str__(self):
        return self.subject

    def __str__(self):
        return self.title

    def __str__(self):
        return self.description

    def number_of_cards(self):
        return self.cards.count()


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

    def __str__(self):
        return deck.subject
