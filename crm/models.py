from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class GolfCourse(models.Model):
    course_name = models.CharField(max_length=50)
    hole_one_par = models.IntegerField()
    hole_two_par = models.IntegerField()
    hole_three_par = models.IntegerField()
    hole_four_par = models.IntegerField()
    hole_five_par = models.IntegerField()
    hole_six_par = models.IntegerField()
    hole_seven_par = models.IntegerField()
    hole_eight_par = models.IntegerField()
    hole_nine_par = models.IntegerField()
    hole_ten_par = models.IntegerField()
    hole_eleven_par = models.IntegerField()
    hole_twelve_par = models.IntegerField()
    hole_thirteen_par = models.IntegerField()
    hole_fourteen_par = models.IntegerField()
    hole_fifteen_par = models.IntegerField()
    hole_sixteen_par = models.IntegerField()
    hole_seventeen_par = models.IntegerField()
    hole_eighteen_par = models.IntegerField()
    total_par = models.IntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
       return str(self.course_name)

class Score(models.Model):
    course_name = models.ForeignKey(GolfCourse, on_delete=models.CASCADE, related_name='score')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hole_one = models.IntegerField()
    hole_two = models.IntegerField()
    hole_three = models.IntegerField()
    hole_four = models.IntegerField()
    hole_five = models.IntegerField()
    hole_six = models.IntegerField()
    hole_seven = models.IntegerField()
    hole_eight = models.IntegerField()
    hole_nine = models.IntegerField()
    hole_ten = models.IntegerField()
    hole_eleven = models.IntegerField()
    hole_twelve = models.IntegerField()
    hole_thirteen = models.IntegerField()
    hole_fourteen = models.IntegerField()
    hole_fifteen = models.IntegerField()
    hole_sixteen = models.IntegerField()
    hole_seventeen = models.IntegerField()
    hole_eighteen = models.IntegerField()
    total_score = models.IntegerField()
    golf_date=models.DateField()
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.course_name)