from django.shortcuts import render
from online.models import File, User
from django.shortcuts import redirect
from django.http import HttpResponse
import traceback
import sys
import io
from datetime import datetime
import os
import json


def authreg(request):
    return render(request, 'authreg.html')
    
    
def api_auth(request):
    if request.POST:
        data = request.POST 
        login = data.get('login')
        password = data.get('password')
        if User.objects.filter(login=login, password=password)[0]:
            user = User.objects.get(login=login, password=password)
            request.session['user_id'] = user.id
            return redirect('home')
    return HttpResponse('error')


def api_reg(request):
    if request.POST:
        data = request.POST 
        login = data.get('login')
        password = data.get('password')
        if not User.objects.filter(login=login, password=password):
            user = User(login=login, password=password)
            user.save()
            request.session['user_id'] = user.id
            return redirect('home')
    return HttpResponse('error')


def home(request):
    if request.session.get('user_id'):
        context = {
            'files' : File.objects.filter(user_id=request.session.get('user_id')),
            'user' : User.objects.get(id=request.session.get('user_id'))
        }
        return render(request, 'home.html', context)
    return HttpResponse('error')


def compiler(request):
    context = {}
    if request.method == 'POST':
        code = request.POST.get('code')
        print(code)
        log_file = f'online/static/logs/{datetime.now().date()}.txt'
        with open(log_file, 'a+') as file:
            file.write(f'\n--------------------------------------------------')
            file.write(f"\nUser id: {request.session.get('user_id')}")
            file.write(f'\nCode: {code}')
            file.write(f'\nTime: {datetime.now()}')
            print('ok log')
        if 'os' in code or 'sys' in code:
            return HttpResponse('error')
        try:
            exec_result = {}
            old_stdout = sys.stdout
            redirected_output = sys.stdout = io.StringIO()
            exec(code, {}, exec_result)
            output = redirected_output.getvalue()
            sys.stdout = old_stdout
        except Exception as e:
            output = traceback.format_exc()
            print(output)
        
        context.update({'output':output, 'code':code})
        print(context)

    return render(request, 'compiler.html', context)


def save_file(request):
    print('got')
    if request.method == 'POST':
        data = json.loads(request.body)
        print('post')
        code = data.get('code')
        print(code)
        name = code[:10] + '...'
        user_id = request.session.get('user_id')
        file = File(name=name, user_id=user_id, code=code)
        file.save()
        print('created')
        dir = f'online/static/files/{file.id}.txt'
        with open(dir, 'w') as f:
            f.write(f'{code}')
        file.dir = dir
        file.save()
        return redirect('home')
    return HttpResponse('error')
        