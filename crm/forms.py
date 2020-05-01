from django import forms
from .models import GolfCourse, Score
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'

class GolfCourseForm(forms.ModelForm):
    class Meta:
        model = GolfCourse
        fields = ( 'course_name',
    'hole_one_par',
    'hole_two_par',
    'hole_three_par',
    'hole_four_par',
    'hole_five_par',
    'hole_six_par',
    'hole_seven_par',
    'hole_eight_par',
    'hole_nine_par',
    'hole_ten_par',
    'hole_eleven_par',
    'hole_twelve_par',
    'hole_thirteen_par',
    'hole_fourteen_par',
    'hole_fifteen_par',
    'hole_sixteen_par',
    'hole_seventeen_par',
    'hole_eighteen_par',
    'total_par')

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ( 'course_name', 'user',
    'hole_one',
    'hole_two',
    'hole_three',
    'hole_four',
    'hole_five',
    'hole_six',
    'hole_seven',
    'hole_eight',
    'hole_nine',
    'hole_ten',
    'hole_eleven',
    'hole_twelve',
    'hole_thirteen',
    'hole_fourteen',
    'hole_fifteen',
    'hole_sixteen',
    'hole_seventeen',
    'hole_eighteen',
    'total_score',
    'golf_date' ,)
        widgets = { 'golf_date': DateInput()}

