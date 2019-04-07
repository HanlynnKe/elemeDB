# 哈尔滨工业大学（深圳）- 数据库系统 - 实验3

根据手机上的饿了么软件设计数据库系统，采用 django + mysql + vue 的结构设计后台及DBMS

其中elemeDB/dbms文件夹中models用于存储仅管理员可视的数据库表，view_models用于存储用户可视的数据库视图

##### 以下为踩雷记录：

- Django连接现有mysql数据库

   - 首先把settings.py里的设置给改了，如下：
   
      ```
      DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 你的数据库名称,
           'USER': 访问mysql数据库的用户名,
           'PASSWORD': 访问mysql数据库的密码,
           'HOST': '127.0.0.1',
           'PORT': '3306'
       }
      }
      ```
   
   - 然后就是新建一个app
   
   - 在settings.py里面添加完app以后就是导入models.py
   
      ```
      python3 manage.py inspectdb > ./app/models.py
      ```
      
   - 如果数据库很大，表很多，请参考：
      
      https://medium.com/cashify-engineering/generating-django-models-from-a-database-f4d03883cc5b
      
      或者前往 https://www.google.com 输入关键词 Django inspectdb
      
- Django连接现有mysql数据库视图(view)
   
   - 建议手写（笑）
   
   - 和models.py里的代码有点类似，但只需要声明db_column、 primary_key、blank、null的参数就可以了，注意要有class Meta以及声明db_table
   
- Vue的admin页面跳转

   - 之前一直不会使用vue跳转到django自带的admin界面，现在会惹。在Vue页面中使用如下代码：
   
     ```
     this.$router.go(0)
     ```
     但是可能会出现页面卡顿的情况，不过既然是django自己的页面，目前来看十分顺滑～

- Django使用原生SQL语句

   - 使用所谓的Manager.raw(raw_sql= , params=[], ...)，注意这只能完成SELECT操作
     网上查了好多可是没有什么比较好的答案，根本不知道主键要放在哪。话不多说，上图：
     ```
     sql = 'SELECT * FROM eleme.view_order WHERE ordercode = %s'
     orders = ElemedbViewOrder.objects.raw(sql, [order_id])
     ```
     
   - 采用游标的方法，不仅能SELECT还可以UPDATE、DELETE、INSERT
     这里是比较简单的用法，没有什么七七八八的map，我也只用了mysql这么1个数据库。如下：
     ```
     from django.db import connection
     
     cursor = connection.cursor()
     sql = 'select addressCode, contact, gender, address, phone, tag, user_username ' \
           'from view_useraddress vua natural join view_user vu ' \
           'where vua.user_userName = vu.userName and vu.userName = %s'
     cursor.execute(sql, [user])
     users = cursor.fetchall()  # 返回的是一个个tuple
     ```
