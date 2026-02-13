from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import FallenForm
from .models import Fallen


def fallen_list(request):
    search = request.GET.get("search")

    qs = Fallen.objects.all()
    if search:
        qs = qs.filter(name__icontains=search)

    data = list(qs.values())
    return JsonResponse(data, safe=False)


def memory_page(request):
    return render(request, "memory/index.html")


def is_superuser(user):
    return user.is_superuser


@login_required
@user_passes_test(is_superuser)
def add_fallen(request):
    if request.method == "POST":
        form = FallenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:profile")
    else:
        form = FallenForm()
    return render(request, "memory/add_falen.html", {"form": form})
