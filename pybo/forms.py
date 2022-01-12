from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm): #forms에서 ModelForm이라는 class 상속받음. 우리가 만들어둔 모델에 관해 폼을 만들어 줌
    class Meta: #ModelForm을 상속받았을 때 반드시 필요한 것
        model = Question #내가 만든 Question 모델을 model에 넘겨줌
        fields = ['subject', 'content'] #그 모델에서 이 두 속성을 사용
        labels = {
            'subject' : '제목',
            'content' : '내용'
        }

class AnswerForm(forms.ModelForm):  # forms에서 ModelForm이라는 class 상속받음. 우리가 만들어둔 모델에 관해 폼을 만들어 줌
    class Meta:  # ModelForm을 상속받았을 때 반드시 필요한 것
        model = Answer  # 내가 만든 Answer 모델을 model에 넘겨줌
        fields = ['content']  # 그 모델에서 이 속성을 사용
        labels = {
            'content': '답변내용'
        }