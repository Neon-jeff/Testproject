from django.shortcuts import render
from django.http import JsonResponse

def Res(request):
    return JsonResponse({'Hi':'Did u get the response'})