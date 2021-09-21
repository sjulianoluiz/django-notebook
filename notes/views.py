from django.urls import reverse_lazy
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView
)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Note

class NoteListView(ListView):
  model = Note
  queryset = Note.objects.all().order_by('-date_created')

class NoteDetailView(DetailView):
  model = Note

class NoteCreateView(SuccessMessageMixin, CreateView):
  model = Note
  fields = ['title', 'content']
  success_url = reverse_lazy('note-list')
  success_message = 'Your new note was created!'

class NoteUpdateView(SuccessMessageMixin, UpdateView):
  model = Note
  fields = ['title', 'content']
  success_message = 'Your note was updated!'

  def get_success_url(self):
    return reverse_lazy(
      'note-detail',
      kwargs={'pk': self.object.pk}
    )

class NoteDeleteView(DeleteView):
  model = Note
  success_url = reverse_lazy('note-list')
  success_message = 'Your note was deleted!'

  def delete(self, request, *args, **kwargs):
    messages.success(self.request, self.success_message)
    return super().delete(request, *args, **kwargs)
