from django.urls import path
from . import views

urlpatterns = [
  path(
    '',
    views.NoteListView.as_view(),
    name='note-list'
  ),
  path(
    'note/<int:pk>',
    views.NoteDetailView.as_view(),
    name='note-detail'
  )
]
