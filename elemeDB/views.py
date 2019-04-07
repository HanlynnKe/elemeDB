from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from dbms.view_models import *


# Create your views here.
@login_required(login_url='/admin/login')
def admin_login(request):
    return HttpResponseRedirect("/admin/login/?next=/admin/")


def check(request):
    # 返回信息
    msg = 0
    # 登录检查
    if request.method == 'POST':
        username =request.POST.get('userName', '')
        password = request.POST.get('password', '')
        # 如果用户名为空
        if username == '':
            return HttpResponse(msg)
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    msg = 1
            return HttpResponse(msg)


def handle(request):
    orders = ElemedbViewOrder.objects.all().values()
    return HttpResponse(orders)
