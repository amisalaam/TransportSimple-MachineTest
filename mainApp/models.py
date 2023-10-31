from django.db import models
from Authentication.models import Account

# Create your models here.


#QUESTION MODEL
class Question(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000)
    posted_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
    

#ANSWER MODEL
class Answer(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(Account, related_name='liked_answers')

    def __str__(self):
        return self.answer_text
    
    def like(self, user):
        if user not in self.likes.all():
            self.likes.add(user)
            self.save()

    def unlike(self, user):
        if user in self.likes.all():
            self.likes.remove(user)
            self.save()