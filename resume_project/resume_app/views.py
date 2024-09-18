# resume_app/views.py
from django.shortcuts import render

def resume_view(request):
  return render(request, 'resume_app/cv.html')

