from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

def signup(request):
    """
    계정생성
    """
    if request.method == "POST": #자기자신의 페이지가 이미 있는 상황일 때 저장 버튼을 누르면 post방식
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('index') #index함수로 이동
    else:
        form = UserForm()  # GET방식으로 폼을 받았을 때.
    return render(request, 'common/signup.html', {'form' : form})