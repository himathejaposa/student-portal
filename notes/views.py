from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from .ai_helper import get_ai_answer

@login_required
def note_list(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.student = request.user
            note.save()

            if note.is_doubt:
                ai_answer = get_ai_answer(note.content)
                note.content = note.content + "\n\n[AI Answer]: " + ai_answer
                note.save()

            return redirect('note_list')
    else:
        form = NoteForm()

    notes = Note.objects.all()
    context = {
        'form': form,
        'notes': notes,
    }
    return render(request, 'notes/notes.html', context)