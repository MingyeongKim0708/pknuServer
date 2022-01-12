
from django.urls import path
from .views import base_views, question_views, answer_views #views라는 폴더에서 각각의 파일 임포트

app_name = 'pybo'

urlpatterns = [
    path('', base_views.index, name = 'index'), #views의 index함수 호출
    path('<int:question_id>/', base_views.detail, name = 'detail'), #pybo/아이디번호. name = 별칭
    path('question/create/', question_views.question_create, name = 'question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name = 'question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name = 'question_delete'),
    path('answer/create/<int:question_id>/', answer_views.answer_create, name = 'answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name = 'answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name = 'answer_delete'),
]
