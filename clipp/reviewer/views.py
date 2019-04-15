from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import(
    ListView
)
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Course
from .forms import CourseForm

# Create your views here.

def home(request ,*args, **kwargs):
    print(request.user)
    # return HttpResponse("<h1> Hello World </h1>")
    dict_new = {"guid":"121131313", "name":"Django and Python", "status":True, "html":"<i>Hifari<i>"}
    return render(request, "abc.html", {'dict':dict_new})

def course(request, *args, **kwargs):
    obj = Course.objects.all()
    return render(request, "new.html", {'dict':obj})

def createForm(request, *args, **kwargs):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CourseForm()

    context = {'form':form}
    return render(request, "form.html", context)

def oldForm(request, *args, **kwargs):
    print(request.POST)
    if request.method == "POST":
        guid = request.POST.get('guid')
        dict = {"guid":guid, "title":"Android", "description":"Learn IOS", "status":False}
        Course.objects.create(**dict)
    return render(request, "old_form.html", {})

def dynamic_view(request, guid):
    # a = get_object_or_404(Course, guid=guid)
    try:
        a = Course.objects.get(guid=guid)
    except Course.DoesNotExist:
        raise Http404
    context = {"item": a}
    return render(request, "individual.html", context)
    # return HttpResponse("Hello " + str(a) + "Aap buhat achi hou yaaaaaaaaaaar :)") 
    # return HttpResponseRedirect('https://google.com')  # "protocol relative" URL

def delete(request, guid):
    # obj = get_object_or_404(Course, guid=guid)
    obj = Course.objects.filter(guid=guid)
    if request.method=="POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object":obj
    }
    # print(context["object"].title)
    return render(request, "delete.html", context)

    # a = get_object_or_404(Course, guid=guid)
    # try:
    #     a = Course.objects.filter(guid=guid)
    #     a.delete()
    #     # a.destroy()
    # except Course.DoesNotExist:
    #     raise Http404
    # print(a)
    # return redirect('../../')
    # return HttpResponse("Object deleted") 
    # return HttpResponseRedirect('https://google.com')  # "protocol relative" URL


# class CourseView(ListView):
#     template_name = 'class_based.html'
#     context_object_name = 'my_book_list'   # your own name for the list as a template variable

#     queryset = Course.objects.get(guid='99')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/course/')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {
        'form':form
    })

@login_required(login_url='login')
def secret_page(request):
    return render(request, 'secret_page.html')

class SecretPage(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'secret_page.html'

