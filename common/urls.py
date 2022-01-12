from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#auth내부의 views함수를 auth_views라는 이름으로 사용

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'common/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'), #ui가 필요없으므로 굳이 ()안의 템플릿을 지정할 필요가 없다
    path('signup/', views.signup, name = 'signup'),
]