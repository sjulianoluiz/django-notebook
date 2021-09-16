from django.views.generic import (
  ListView,
  DetailView
)
from .models import Note

class NoteListView(ListView):
  model = Note
  queryset = Note.objects.all().order_by('-date_created')

class NoteDetailView(DetailView):
  model = Note
