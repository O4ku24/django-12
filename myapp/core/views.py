from django.shortcuts import render
from core.utilits import trans, open_text, day_week


def home(request):
    return render(request=request, template_name='core/home.html')

def music(request):
    if request.method == 'GET':
        return render(request=request, template_name='core/music.html', context=open_text())
    if request.methot == 'POST':
        print(request)
    
def musicEn(request):
    if request.method == 'GET':
        return render(request=request, template_name='core/music.html', context=trans('en'))

def musicFr(request):
    if request.method == 'GET':
        return render(request=request, template_name='core/music.html', context=trans('fr'))
    
def musicDe(request):
    if request.method == 'GET':
        return render(request=request, template_name='core/music.html', context=trans('de'))
    
def carhome(request):
    if request.method == 'GET':
        return render(request=request, template_name='core/car.html')

def car_toyota(request):
    if request.method == 'GET':
        car = 'Toyota'
        data = {'data':car}
        return render(request=request, template_name='core/car.html', context=data)

def car_honda(request):
    if request.method == 'GET':
        car = 'Honda'
        data = {'data':car}
        return render(request=request, template_name='core/car.html', context=data)
    
def car_renault(request):
    if request.method == 'GET':
        car = 'Renault'
        data = {'data':car}
        return render(request=request, template_name='core/car.html', context=data)
    
def week(request):
    if request.method == 'GET':
        return render(request=request, template_name='core/week.html')
    if request.method == 'POST':
        color = day_week(request)
        return render(request=request, template_name='core/week.html', context=color)