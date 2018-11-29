from django.shortcuts import render
from django.template.context_processors import csrf

# Create your views here.
from django.http import HttpResponse
from app_test0.models import Character

def first_page(request):
    return HttpResponse("<p>This is app0. Hello world! </p>")

def all(request):
    all_list = Character.objects.all()
    all_str =map(str,all_list)
    return HttpResponse("<p>" + ' '.join(all_str) + "</p>")

def templay(request):
    context = {}
    templay_list = Character.objects.all()
    templay_str = map(str, templay_list)
    context = {
        'label': 'Hello, world!',
        'label1': ' '.join(templay_str),
        'label2': templay_list,

    }
    return render(request, 'app_test0/templay1.html', context)

def form(request):
    return render(request, 'app_test0/form.html')

def investigate(request):
     rlt = request.GET['templay2']
     return HttpResponse(rlt)

def post_investigate(request):
    if request.POST:
        submitted = request.POST['templay1']
        new_record = Character(name=submitted)
        new_record.save()

    ctx = {}
    ctx.update(csrf(request))
    all_record = Character.objects.all()
    ctx['rlt1'] = all_record
    return render(request, 'app_test0/investigate.html', ctx)