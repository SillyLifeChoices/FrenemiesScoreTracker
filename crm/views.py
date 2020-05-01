from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import *
from .forms import *

now = timezone.now()
def home(request):
   return render(request, 'crm/home.html',
                 {'crm': home})

@login_required
def golf_course_list(request):
    course = GolfCourse.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/golf_course_list.html',
                 {'courses': course})

@login_required
def golf_course_edit(request, pk):
   course = get_object_or_404(GolfCourse, pk=pk)
   if request.method == "POST":
       # update
       form = GolfCourseForm(request.POST, instance=course)
       if form.is_valid():
           course = form.save(commit=False)
           course.updated_date = timezone.now()
           course.save()
           course = GolfCourse.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/golf_course_list.html',
                         {'courses': course})
   else:
        # edit
       form = GolfCourseForm(instance=course)
   return render(request, 'crm/golf_course_edit.html', {'form': form})

@login_required
def golf_course_delete(request, pk):
   course = get_object_or_404(GolfCourse, pk=pk)
   course.delete()
   return redirect('crm:golf_course_list')

@login_required
def golf_course_new(request):
    if request.method == "POST":
        form = GolfCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_date = timezone.now()
            course.save()
            courses = GolfCourse.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/golf_course_list.html',
                {'courses': courses})
    else:
        form = GolfCourseForm()
        # print("Else")
    return render(request, 'crm/golf_course_new.html', {'form': form})

@login_required
def score_list(request):
    score = Score.objects.filter(created_date__lte=timezone.now(), user__username=request.user)
    return render(request, 'crm/score_list.html',
                 {'scores': score})

@login_required
def score_edit(request, pk):
   score = get_object_or_404(Score, pk=pk)
   if request.method == "POST":
       # update
       form = ScoreForm(request.POST, instance=score)
       if form.is_valid():
           score = form.save(commit=False)
           score.updated_date = timezone.now()
           score.save()
           score = Score.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/score_list.html',
                         {'scores': score})
   else:
        # edit
       form = ScoreForm(instance=score)
   return render(request, 'crm/score_edit.html', {'form': form})

@login_required
def score_delete(request, pk):
   score = get_object_or_404(Score, pk=pk)
   score.delete()
   return redirect('crm:score_list')

@login_required
def score_new(request):
    if request.method == "POST":
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.created_date = timezone.now()
            score.save()
            scores = Score.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/score_list.html',
                {'scores': scores})
    else:
        form = ScoreForm()
        # print("Else")
    return render(request, 'crm/score_new.html', {'form': form})

@login_required
def score_compare(request, pk):
    course = get_object_or_404(GolfCourse, pk=pk)
    courses = GolfCourse.objects.filter(created_date__lte=timezone.now())
    #customer = get_object_or_404(Customer, pk=pk)
    #customers = Customer.objects.filter(created_date__lte=timezone.now())
    #services = Service.objects.filter(cust_name=pk)
    #products = Product.objects.filter(cust_name=pk)
    scores = Score.objects.filter(course_name = pk)
    #scores = Score.objects.filter(course_name__pk=pk)
    return render(request, 'crm/score_compare.html', {'scores': scores, 'courses':courses})