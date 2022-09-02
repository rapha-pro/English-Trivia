from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Quiz, Category, Question, Choice
from datetime import datetime, date
import calendar
from calendar import HTMLCalendar
import time
from django.contrib.auth.decorators import login_required


def home(request):
  return render(request, 'home.html')
  

def selection(request): 
  
  if request.GET.get('search') is None:
    search = "";
    all_quizzes = Quiz.objects.all
  else:
    search = request.GET['search'];
    all_quizzes = Quiz.objects.filter(topic__icontains=search)

  categories = Category.objects.all
  template = loader.get_template('all_quizzes.html')
  context = {
        'all_quizzes': all_quizzes,
        'search': search,
        'categories': categories
  }
  
  return HttpResponse(template.render(context, request))


def category(request, cat):
  all_quizzes = Quiz.objects.filter(category__category=cat.lower())
  categories = Category.objects.all
  template = loader.get_template('all_quizzes.html')
  context = {
      'all_quizzes': all_quizzes,
      'categories': categories
  }
  return HttpResponse(template.render(context, request))

def quiz_start(request, qn):
  request.session['current_q'] = 0
  request.session['score'] = 0
  request.session['user_answers'] = []
  return redirect(f"/quiz/{qn}")

@login_required  
def quiz_page(request, qn):
  
  quiz = get_object_or_404(Quiz, pk=qn)

  if request.session.has_key('c_quiz') == False:
    request.session['c_quiz'] = []

  request.session['c_quiz'] = str(quiz.topic)

  current_quiz = request.session.get('c_quiz')

  quiz_questions = Question.objects.filter(quiz_id = qn)
  category = Category.objects.get(pk=quiz.category_id)

  currentQuestion = quiz_questions[request.session['current_q']]
  choices = Choice.objects.filter(question_id=currentQuestion.id)

    
  template = loader.get_template('quiz_page.html')
  context = {
      'quiz': quiz,
      'category' : category,
      'currentQuestion': currentQuestion,
      'current_quiz': current_quiz,
      'choices': choices
  }
  return HttpResponse(template.render(context, request))

def check_answer(request, question, answer):
  
  # try:
  #   choice = Choice.objects.get(question_id=question, is_answer=True, choice_text=answer)
  #   request.session.get['score'] += 1
  #   return HttpResponse('true') 
  # except Choice.DoesNotExist:
  #     return HttpResponse('false')
    

  choices = Choice.objects.filter(question_id=question)
  for c in choices:
    if (c.is_answer and (c.choice_text == answer)):
      #request.session['score']+= 1
      return HttpResponse('true') 

  return HttpResponse('false')

def validate(request, qn, answer, valid):
  print(qn, answer)

  if request.session.has_key('user_answers') == False:
    request.session['user_answers'] = []

  request.session['user_answers'].append(answer)
  
  quiz_questions = Question.objects.filter(quiz_id = qn)

  if valid == 1:
    request.session['score']+=1
    
  if request.session['current_q']+1 < len(quiz_questions) :
    request.session['current_q']+=1
  else:
    return HttpResponse(1)
   
  return HttpResponse("Request succesful")
  

def countdown(t=60):
  while t:
    print(t)
    time.sleep(1)
    t -=1

  
# Calendar
def calend(request, year, month):
  year = int(year)
  month = int(month)
  
  if 1000 > year > 2099:
    t = datetime.now()
    year = t.year
    month = t.month

  month_name = calendar.month_name[month]
  title = "WELCOME TO CALENDAR - %s %s" %(month_name, year)
  cal = HTMLCalendar().formatmonth(year, month)
  return HttpResponse("<h1>%s</h2><p>%s</p>" %(title, cal))

t = datetime.now()
print(datetime.strftime(t, '%B'))

def scoreboard(request):
  scoring = (request.session['score']/len(request.session['user_answers'])) * 100
  scoring = float("{0:.1f}".format(scoring))

  current_quiz = request.session.get('c_quiz')

  if scoring < 50:
    bcolor = "danger"
  elif scoring < 100:
    bcolor = "primary"
  else:
    bcolor = "success"
  
  return render(request, 'result.html', {'scoring': scoring, 'quiz': current_quiz, 'bcolor':bcolor})

