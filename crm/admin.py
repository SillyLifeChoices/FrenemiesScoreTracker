from django.contrib import admin

from .models import GolfCourse, Score

class GolfCourseList(admin.ModelAdmin):
    list_display = ( 'course_name')
    list_filter = ( 'course_name')
    search_fields = ('course_name')
    ordering = ['course_name']

admin.site.register(GolfCourse)

class ScoreList(admin.ModelAdmin):
    list_display = ( 'course_name', 'user', 'golf_date')
    list_filter = ( 'course_name', 'user')
    search_fields = ('course_name',)
    ordering = ['course_name']

admin.site.register(Score, ScoreList)