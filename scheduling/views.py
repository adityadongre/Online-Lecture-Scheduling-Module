from django.shortcuts import render, redirect, get_object_or_404
from .models import Instructor, Course, Lecture
from .forms import CourseForm, LectureForm
from datetime import datetime

def home_panel(request):

    return render(request, 'home_panel.html')

def admin_panel(request):
    instructors = Instructor.objects.all()
    courses = Course.objects.all()
    lectures = Lecture.objects.all()
    
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        lecture_form = LectureForm(request.POST)
        
        if course_form.is_valid():
            course = course_form.save()
            return redirect('admin_panel')  
        
        if lecture_form.is_valid():
            lecture = lecture_form.save()
            return redirect('admin_panel')  
            
    else:
        course_form = CourseForm()
        lecture_form = LectureForm()
    
    context = {
        'instructors': instructors,
        'courses': courses,
        'lectures': lectures,
        'course_form': course_form,
        'lecture_form': lecture_form,
    }
    return render(request, 'admin_panel.html', context)

def instructor_panel(request):
    instructor_id = 1  # Replace with actual instructor ID (obtained after login)
    instructor = Instructor.objects.get(pk=instructor_id)
    lectures = Lecture.objects.filter(instructor=instructor_id)
    
    context = {
        'instructor': instructor,
        'lectures': lectures,
    }
    return render(request, 'instructor_panel.html', context)

def instructor_detail(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    # You can add more context data if needed
    return render(request, 'admin/instructor_detail.html', {'instructor': instructor})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # You can add more context data if needed
    return render(request, 'admin/course_detail.html', {'course': course})

def lecture_detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    # You can add more context data if needed
    return render(request, 'admin/lecture_detail.html', {'lecture': lecture})
