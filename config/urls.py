"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Flash import views

urlpatterns = [


    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/add_deck/<int:pk>', views.add_deck, name='add_deck'),
    path('edit_deck/<int:pk>', views.edit_deck, name='edit_deck'),
    path('edit_deck/<int:pk>', views.edit_deck, name='edit_deck'),
    path('delete_deck/<int:pk>', views.delete_deck, name='delete_deck'),
    path('test/<int:pk>', views.test_deck, name="test_deck"),
    path('test/<int:pk>/correct_guess', views.correct_guess, name="correct_guess"),
    path('test/<int:pk>/total_guesses', views.total_guesses, name="total_guesses"),
    path('test_summary/<int:pk>', views.test_summary, name="test_summary"),
    path('', views.index_view),
]
