from django.urls import path
from .views import CourseListView, CourseDetailView, LessonDetailView
from . import views

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='courses-home'),
    path('<slug>', CourseDetailView.as_view(), name='detail'),
    path('<course_slug>/<lesson_slug>', LessonDetailView.as_view(), name='lesson-detail')
]

