from django.http import JsonResponse
from .models import Fallen
from django.shortcuts import render

def fallen_list(request):
    search = request.GET.get("search")

    qs = Fallen.objects.all()

    if search:
        qs = qs.filter(name__icontains=search)

    data = list(qs.values())
    return JsonResponse(data, safe=False)

def memory_page(request):
    return render(request, "memory/index.html")