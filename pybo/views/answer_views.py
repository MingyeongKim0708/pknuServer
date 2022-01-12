from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Question, Answer


@login_required(login_url = 'common:login')
def answer_create(request, question_id):
    """답변 등록"""
    # question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, pk = question_id) #어떤 질문에 대한 답변인지 연결되어야함(종속)

    if request.method == "POST": #자기자신의 페이지가 이미 있는 상황일 때 저장 버튼을 누르면 post방식
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit = False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id = question_id) #답변 등록하는 페이지로 이동(현재 화면 유지)

    else:
        form = AnswerForm()

    context = {'question' : question, 'form' : form}
    return render(request, 'pybo/question_detail.html', context) #답변 등록하는 페이지로 이동

    # answer = Answer(question = question, content = request.POST.get('content'), create_date = timezone.now())
    # answer.save()
    # return redirect('pybo:detail', question_id = question.id) #상세화면을 보여주기 위한 페이지로 리다이렉트함.
#detail 은 view.detail의 별칭 -> 즉 def detail을 실행
#redirect : 호출

@login_required(login_url = 'common:login')
def answer_modify(request, answer_id):
    """답변 수정"""
    answer = get_object_or_404(Answer, pk = answer_id)
    if request.user != answer.author: #request.user = 로그인한 유저.
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('pybo:detail', question_id = answer.question.id)

    if request.method == "POST": #자기자신의 페이지가 이미 있는 상황일 때 저장 버튼을 누르면 post방식
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit = False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id = answer.question_id)

    else:
        form = AnswerForm(instance = answer)

    context = {'answer' : answer, 'form' : form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url = 'common:login')
def answer_delete(request, answer_id):
    """답변 삭제"""
    answer = get_object_or_404(Answer, pk = answer_id)
    if request.user != answer.author: #request.user = 로그인한 유저.
        messages.error(request, '삭제 권한이 없습니다.')

    else:
        answer.delete()
    return redirect('pybo:detail', question_id = answer.question.id)