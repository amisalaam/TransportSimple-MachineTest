from django.db import models
from Authentication.models import Account

# Create your models here.



class Question(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000)
    posted_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text