from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, QueryDict

# Create your views here.
def tag_list(request):
    if request.method == "GET":
        return JsonResponse(response)

def tag_detail(request, pk):
    if request.method == "GET":  #post detail
        return JsonResponse(response)
