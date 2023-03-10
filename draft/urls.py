
from django.urls import path

from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path('new_draft', views.new_draft, name='new_draft'),
    path('<int:group_id>', views.group, name='group'),
    path('draft/<int:group_id>', views.draft, name='draft')
]
