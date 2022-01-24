from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import PersonForm
from .models import Person
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages




# Create your views here.

def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")


def get_name(request):
    all = Person.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New Data Has Been Inserted Successfully..!")
            return HttpResponseRedirect('/')
    else:
        form = PersonForm()

    return render(request, 'bookeep/index.html', {'form': form, "all": all})

def update(request, id):
    all = Person.objects.all()
    if request.method == 'POST':
        instance = Person.objects.get(id=id)
        form = PersonForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Has Been Updated Successfully..!")
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect('/')

    else:
        instance = Person.objects.get(id=id)
        form = PersonForm(instance=instance)
        # return render(request, 'bookeep/index.html', {'form': form, "all": all})
        return render(request, 'bookeep/update.html', {'form': form})


def post_data(request):

    if request.method == 'POST':
        if request.POST["operation"] == "Delete" and request.POST.get("item") != None:
            obj = Person.objects.get(id=request.POST["item"])
            obj.delete()
            messages.warning(request, "Data Has Been Deleted Successfully..!")
            return HttpResponseRedirect('/')
        elif request.POST["operation"] == "Update" and request.POST.get("item") != None:
            return redirect(reverse('update', kwargs={'id': request.POST["item"]}))

        else:
            return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/')
