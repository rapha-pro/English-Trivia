from django.db import models

class Category(models.Model):
  category = models.CharField(max_length=15)
  
  def __str__(self):
    return self.category

  def get_quizes(self):
    return self.quiz_set.all()

class Quiz(models.Model):
  topic = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
  description_text = models.CharField(max_length = 200, default='Description')
  Lesson = models.TextField(max_length = 1000, default="Enter a Text")

  def __str__(self):
    return self.topic

  def get_questions(self):
    return self.question_set.all()

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    duration = models.IntegerField(default=15)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
      return self.question_text

    def get_answers(self):
      return self.answer_set.all()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
      return self.choice_text


    # implement Binary search??
    '''while low <= high:
    search_quiz = low + (high - low)//2
    v = input(f"\nIs your right quiz: {l[mid]}?: ")
      
    if search_quiz=='quiz.id':
      return message_True
    elif v=='h':
      high = mid -1
    else:
      low = mid + 1

  return message_False'''
  