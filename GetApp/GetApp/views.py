from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import NameForm


def get_app(request):
    values = []
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            keys, values = zip(*data.items())


            return HttpResponseRedirect(f"?name={values[0]}&message={values[1]}")


    else:
        form = NameForm()
    args = {"form": form,
            "name":request.GET.get("name"),
            "message": request.GET.get("message")
            }

    return render(request, "index.html", args)


