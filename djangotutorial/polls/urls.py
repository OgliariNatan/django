from django.urls import path
from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("detalhe<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("resultado<int:question_id>", views.results, name="results"),
    # ex: /polls/5/vote/
    path("votação<int:question_id>.asp", views.vote, name="vote"),
]