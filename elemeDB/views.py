from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.db import connection
from dbms.view_models import *
import json


# Create your views here.
@login_required(login_url='/admin/login')
def admin_login(request):
    return HttpResponseRedirect("/admin/login/?next=/admin/")


def check(request):
    # 返回信息
    msg = 0
    # 登录检查
    if request.method == 'POST':
        username = request.POST.get('userName', '')
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
    if request.method == 'POST':
        items = []
        user_dic, order_dic, rstrt_dic = [], [], []
        # 从request获取参数
        mode = request.POST.get('mode', '')
        user = request.POST.get('name', '')
        restaurant = request.POST.get('rstrtName', '')
        order_id = request.POST.get('orderID', '')
        # 对用户进行查询
        if user != '':
            # 查询用户信息
            if mode == '1':
                # 简便方法
                users = ElemedbViewUser.objects.filter(username=user)

                # 准备response信息
                for name in users:
                    items.append(name.username)
                for item in items:
                    target = ElemedbViewUser.objects.get(username=item)
                    op = {
                        'name': target.username,
                        'tel': target.userphone
                    }
                    # rawSQL方法 --- 分组嵌套查询
                    cursor = connection.cursor()
                    sql = 'SELECT COUNT(userName) FROM view_fav GROUP BY userName HAVING userName = %s'
                    cursor.execute(sql, [user])
                    fav_counts = cursor.fetchone()
                    for fav in fav_counts:
                        op['fav'] = fav
                    print(op)
                    user_dic.append(op)
            # 查询用户收藏
            if mode == '2':
                # rawSQL方法 --- 嵌套查询
                cursor = connection.cursor()
                sql = 'SELECT * FROM view_fav HAVING username = %s'
                cursor.execute(sql, [user])
                users = cursor.fetchall()
                # 准备response信息
                for name in users:
                    items.append(name[1])
                for item in items:
                    target = ElemedbViewFav.objects.get(username=user, rstrtname=item)
                    op = {
                        'name': target.username,
                        'rstrtName': target.rstrtname,
                        'delivLeast': target.deliveryleast,
                        'distance': target.distance,
                        'leastDeliv': target.leasttime
                    }
                    user_dic.append(op)
            # 查询用户地址簿
            if mode == '3':
                # # 简便方法
                # users = ElemedbViewUserAddr.objects.filter(user_username=user)
                # rawSQL方法 --- 连接查询
                cursor = connection.cursor()
                sql = 'select addressCode, contact, gender, address, phone, tag, user_username ' \
                      'from view_useraddress vua natural join view_user vu ' \
                      'where vua.user_userName = vu.userName and vu.userName = %s'
                cursor.execute(sql, [user])
                users = cursor.fetchall()  # 返回的是一个个tuple

                # 准备response信息
                for name in users:
                    items.append(name[0])
                for item in items:
                    target = ElemedbViewUserAddr.objects.get(user_username=user, addresscode=item)
                    op = {
                        'addressID': target.addresscode,
                        'contact': target.contact,
                        'gender': target.gender,
                        'phone': target.phone,
                        'address': target.address,
                        'tag': target.tag
                    }
                    user_dic.append(op)
            res = json.dumps(user_dic)
            return HttpResponse(res)

        # 对餐厅进行查询
        if restaurant != '':
            # 查询餐厅信息
            if mode == '4':
                # 简便方法
                restaurants = ElemedbViewRstrt.objects.filter(rstrtname=restaurant)
                # rawSQL方法
                # sql = ''
                # orders = ElemedbViewOrder.objects.raw(, [restaurant])

                # 准备response信息
                for owners in restaurants:
                    items.append(owners.rstrtname)
                for item in items:
                    target = ElemedbViewRstrt.objects.get(rstrtname=item)
                    op = {
                        'rstrtName': target.rstrtname,
                        'rstrtClass': target.rstrtclass,
                        'rstrtAddress': target.rstrtaddr,
                        'rstrtPhone': target.rstrtphone,
                        'workFrom': str(target.wrkinhrsfrom),
                        'workTo': str(target.wrkinhrsto),
                    }
                    rstrt_dic.append(op)
            # 查询餐厅菜单
            if mode == '5':
                # 简便方法
                dishes = ElemedbViewMenu.objects.filter(rstrtname=restaurant)

                for dish in dishes:
                    items.append(dish.dishname)
                for item in items:
                    target = ElemedbViewMenu.objects.get(dishname=item)
                    op = {
                        'rstrtName': target.rstrtname,
                        'dish': target.dishname,
                        'price': target.dishprice,
                        'sale': target.dishsaleamount
                    }
                    rstrt_dic.append(op)

            res = json.dumps(rstrt_dic)
            return HttpResponse(res)

        # 对订单进行查询
        if order_id != '':
            print(mode)
            # 简便方法
            # orders = ElemedbViewOrder.objects.filter(ordercode=order_id)

            # rawSQL方法
            sql = 'SELECT * FROM eleme.view_order WHERE ordercode = %s'
            orders = ElemedbViewOrder.objects.raw(sql, [order_id])

            # 准备response信息
            for order in orders:
                items.append(order.dishname)
            for item in items:
                target = ElemedbViewOrder.objects.get(dishname=item)
                op = {
                    'orderID': target.ordercode,
                    'name': target.username,
                    'rstrtName': target.rstrtname,
                    'dish': target.dishname,
                    'price': target.dishprice,
                    'sum': target.pay,
                    'orderTime': str(target.ordertime),
                    'contact': target.contact,
                    'address': target.address,
                    'phone': target.phone,
                    'delivPerson': target.deliveryPName,
                    'delivPersonTel': target.deliveryPPhone
                }
                order_dic.append(op)
        res = json.dumps(order_dic)
        return HttpResponse(res)
