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
  ),
  path(
    'note/create',
    views.NoteCreateView.as_view(),
    name='note-create'
  ),
  path(
    'note/<int:pk>/update',
    views.NoteUpdateView.as_view(),
    name='note-update'
  ),
  path(
    'note/<int:pk>/delete',
    views.NoteDeleteView.as_view(),
    name='note-delete'
  )
]
