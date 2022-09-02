from django.urls import path, re_path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('selection', views.selection, name='selection'),
  path('selection/<str:cat>', views.category, name='category'),
  #path('quiz_page', views.quiz_page, name='quiz_page'),
  #path('<int:year>/<str:month>/', views.calend, name='calend')
  re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.calend, name='calend'),
   path('quiz/<int:qn>/start', views.quiz_start, name='quiz_start'),
  path('quiz/<int:qn>', views.quiz_page, name='quiz_page'),
  path('validate/<int:qn>/<str:answer>/<int:valid>', views.validate, name='validate'),
  path('check/<int:question>/<str:answer>', views.check_answer, name='check_answer'),
 path('scoreboard', views.scoreboard, name='scoreboard'),
]