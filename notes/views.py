from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView
)
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Note

class NoteListView(ListView):
  model = Note
  queryset = Note.objects.all().order_by('-date_created')

class NoteDetailView(DetailView):
  model = Note

class NoteCreateView(CreateView):
  model = Note
  fields = ['title', 'content']
  success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView):
  model = Note
  fields = ['title', 'content']

  def get_success_url(self):
    return reverse_lazy(
      'note-detail',
      kwargs={'pk': self.note.id}
    )

class NoteDeleteView(DeleteView):
  model = Note
  success_url = reverse_lazy('note-list')
