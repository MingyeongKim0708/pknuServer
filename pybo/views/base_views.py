from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from ..models import Question, Answer
from django.db.models import Q, Count

# Create your views here.
def index(request):  # request 위치에 다른 이름이 와도 상관은 없다
    """질문 목록 출력"""
    # 입력인자
    page = request.GET.get('page', '1')  # 1페이지 가져옴
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent') #정렬

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else: #recent
        question_list = Question.objects.order_by('-create_date')  # -내림차순

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | #제목 검색 #i 빼버리면 중복 필터링 X
            Q(content__icontains=kw) |  #내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) #답변 글쓴이 검색
        ).distinct()

    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 10개만 보여줌
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page':page, 'kw':kw, 'so':so}  # key-value 형태. 딕셔너리
    return render(request, 'pybo/question_list.html', context)

    # return HttpResponse("Hello World")


def detail(request, question_id):
    """질문 내용 출력"""
    # question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}  # key-value 형태. 딕셔너리
    return render(request, 'pybo/question_detail.html', context)
# render : 화면에 보여주는 것