from django.shortcuts import render
from .forms import GetAppForm
# Create your views here.
def get_app(request):
    if request == "POST":
        forms = GetAppForm(request)
    args = {forms: "forms"}
    return render(args, "index.html", request)