from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentsView.as_view()),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("add_student/", views.AddStudent.as_view(), name='add_student'),
    # path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    # path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail")

]