from django.urls import path
from accountapp.views import hello_world

app_name = "accountapp" # 앱 이름 명시 -> 나중에 긴 주소를 치지 않고서도 접근 가능

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]