from django.db import models
from django.contrib.auth.models import User #model이라는 라이브러리의 User클래스를 임포트


# Create your models here.
class Question(models.Model): #데이터베이스에 저장
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #User객체를 첫번째 전달인자로 전달. User가 삭제되면 author도 삭제.

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #질문과 연관된 필드인 경우 외래키 사용. 질문이 삭제되면 질문과 연결된 답변도 삭제됨
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)