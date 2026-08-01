from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance
from .forms import AttendanceForm

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.student = request.user
            attendance.save()
            return redirect('mark_attendance')
    else:
        form = AttendanceForm()

    records = Attendance.objects.filter(student=request.user)
    context = {
        'form': form,
        'records': records,
    }
    return render(request, 'attendance/attendance.html', context)