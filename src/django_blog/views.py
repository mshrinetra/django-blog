from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ExampleForm


def example_form(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ExampleForm()

    # context = {"header": "Example Form"}
    # return render(request, "exampleform.html", context)

    context = {
        "header": "Example Form",
        "form": form
    }

    return render(request, "exampleform.html", context)


def home_page(request):
    context = {"header": "Home Page"}
    return render(request, "home.html", context)


def example_contextprocessor(request):
    context = {"header": "Context Processor Page"}
    return render(request, "examplecontextprocessor.html", context)


def example_contexttemplate(request):
    context = {"header": "Context Template Example"}
    template_name = "exampletemplate.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)


def example_planetemplate(request):
    return render(request, "exampletemplate.html", {"header": "Plane Template Example"})


def example_render(request):
    return render(request, "exampletemplate.html", {"header": "Render Example"})


def example_regexurl(request):
    return HttpResponse("<h1>Regex URL Example</h1>")


def example_httpresponse(request):
    return HttpResponse("<h1>Http Response Example</h1>")
