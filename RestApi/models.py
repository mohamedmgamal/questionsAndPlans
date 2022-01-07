from django.contrib.auth.models import AbstractUser


from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    name=models.CharField(blank=False,null=False,max_length=64)
    section=models.IntegerField(blank=False,null=False)
    choose=models.BooleanField(default=True)
    text=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Choices(models.Model):
    name=models.CharField(blank=False,null=False,max_length=64)
    question=models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    class Meta:
        unique_together = (("id", "question",))
        ordering = (['id', ])
    def __str__(self):
        return f"{self.name} "

class Attempts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username}  At:{str(self.started_at)}"

class Answers(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice = models.ForeignKey(Choices, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    AttemptId=models.ForeignKey(Attempts,related_name='answers',on_delete=models.CASCADE,null=True)
    other=models.TextField(null=True,blank=True)

    class Meta:
        unique_together = (("question", "AttemptId",))

    def __str__(self):
        return f"{self.question}  A:{self.choice.name} user:{self.user}"