from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from family.models import Family

def create_family(request, name: str, last_name: str, dni: int, age: str):

    template = loader.get_template("template_family.html")
    age = datetime.strptime(age, "%Y-%m-%d")

    family = Family(
        name=name, last_name=last_name, dni=dni, age=age
    )
    family.save()  # save into the DB

    context_dict = {"family": family}
    render = template.render(context_dict)
    return HttpResponse(render)


def relatives(request):
    relatives = Family.objects.all()

    context_dict = {"relatives": relatives}

    return render(
        request=request,
        context=context_dict,
        template_name="family/family_list.html",
    )
