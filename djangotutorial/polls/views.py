#from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {"latest_question_list": latest_question_list,}
    return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#         #return HttpResponse("Você está olhando para a pergunta %s." % question_id)
#     except Question.DoesNotExist:
#         raise Http404("Esta questão não existe")
#     return render(request, "polls/detail.html", {'question': question})
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})



def results(request, question_id):
    response = "Você está vendo os resultados da pergunta %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s." % question_id)