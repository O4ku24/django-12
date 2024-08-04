from django.shortcuts import render
from core.utilits import trans, open_text, day_week
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request=request, template_name='core/home.html')

def music(request):
    if request.method == 'GET':
        return render(request=request, template_name='core/music.html', context=open_text())
    
    
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
@csrf_exempt
def week(request):
    if request.method == 'GET':
        return render(request=request, template_name='core/week.html')
    if request.method == 'POST':
        day = request.POST.get("Week")
        if day == None:
            print('day - None')
            return render(request=request, template_name='core/week.html')
        else:
            print(f'DAY - {day}')
            color = day_week(day)
            print(f'color - {color}')
            data = {'color':color}
        
        return render(request=request, template_name='core/week.html', context=data)
    
def headphones(request):
    if request.method == 'GET':
        return render(request=request, template_name='core/headphones.html')