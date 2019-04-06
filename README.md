# 哈尔滨工业大学（深圳）- 数据库系统 - 实验3

根据手机上的饿了么软件设计数据库系统，采用***django + mysql***的结构设计后台及DBMS

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
   
      `python3 manage.py inspectdb > ./app/models.py`
      
   - 如果数据库很大，表很多，请参考：
      
      https://medium.com/cashify-engineering/generating-django-models-from-a-database-f4d03883cc5b
      
      或者前往 https://www.google.com 输入关键词 Django inspectdb
      
- Django连接现有mysql数据库视图(view)
   
   - 建议手写（笑）
   
   - 和models.py里的代码有点类似，但只需要声明db_column、 primary_key、blank、null的参数就可以了，注意要有class Meta以及声明db_table
