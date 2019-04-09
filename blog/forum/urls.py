from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('^questions/$', views.QuestionList.as_view(), name='questions'),
    re_path('^questions/(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name='detail'),
    re_path('^questions/(?P<pk>\d+)/answer/(?P<answer_pk>\d+)/$', views.AnswerDetail.as_view(), name='answer')
]