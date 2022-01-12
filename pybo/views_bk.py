from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from django.http import HttpResponse

# Create your views here.
def index(request): #request 위치에 다른 이름이 와도 상관은 없다
    """질문 목록 출력"""
    page = request.GET.get('page', '1') #1페이지 가져옴

    question_list = Question.objects.order_by('-create_date') #-내림차순

    #페이징 처리
    paginator =Paginator(question_list, 10) #10개만 보여줌
    page_obj = paginator.get_page(page)


    context = {'question_list' : page_obj} #key-value 형태. 딕셔너리
    return render(request, 'pybo/question_list.html', context)
    
    # return HttpResponse("Hello World")

def detail(request, question_id):
    """질문 내용 출력"""
    # question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}  # key-value 형태. 딕셔너리
    return render(request, 'pybo/question_detail.html', context)
#render : 화면에 보여주는 것

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
def question_create(request):
    """pybo 질문 등록"""
    if request.method == "POST": #자기자신의 페이지가 이미 있는 상황일 때 저장 버튼을 누르면 post방식
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit = False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index') #index함수로 이동

    else:
        form = QuestionForm()  # GET방식으로 폼을 받았을 때. 제일 처음에 question/create페이지에 들어왔을 때 이 폼을 보여준다

    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url = 'common:login')
def question_modify(request, question_id):
    """질문 수정"""
    question = get_object_or_404(Question, pk = question_id)
    if request.user != question.author: #request.user = 로그인한 유저. question.author = 질문 작성자
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('pybo:detail', question_id = question.id)

    if request.method == "POST": #자기자신의 페이지가 이미 있는 상황일 때 저장 버튼을 누르면 post방식
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit = False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id = question_id) #답변 등록하는 페이지로 이동(현재 화면 유지)

    else:
        form = QuestionForm(instance = question)

    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context) #답변 등록하는 페이지로 이동

@login_required(login_url = 'common:login')
def question_delete(request, question_id):
    """질문 삭제 """
    question = get_object_or_404(Question, pk = question_id)
    if request.user != question.author: #request.user = 로그인한 유저. question.author = 질문 작성자
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('pybo:detail', question_id = question.id)

    question.delete()
    return redirect('pybo:index')

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