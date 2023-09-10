from django.db import models

# Create your models here.

class Question(models.Model):
    # Độ dài câu hỏi
    question_test = models.CharField(max_length=200)
    #Thời gian đưa ra
    time_pub = models.DateTimeField()

class Choice(models.Model):
    # Xóa câu trả lời
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    #Nội dung câu trả lời
    choice_text = models.CharField(max_length=100)
    # Điểm số của các câu trả lời
    vote = models.IntegerField(default=0)
