from .models import *


class ElemedbViewUser(models.Model):
    username = models.CharField(db_column='userName', primary_key=True, max_length=24)
    userphone = models.CharField(db_column='userPhone', max_length=11)

    class Meta:
        managed = False
        db_table = "view_user"


class ElemedbViewUserAddr(models.Model):
    addresscode = models.IntegerField(db_column='addressCode', primary_key=True)
    contact = models.CharField(db_column='contact', max_length=11)
    gender = models.CharField(db_column='gender', max_length=3)
    phone = models.CharField(db_column='phone', max_length=11)
    address = models.CharField(db_column='address', max_length=96)
    tag = models.CharField(db_column='tag', max_length=12, blank=True, null=True)
    user_username = models.CharField(db_column='user_userName', max_length=24)

    class Meta:
        managed = False
        db_table = "view_useraddress"


class ElemedbViewFav(models.Model):
    username = models.CharField(db_column='userName', max_length=24, primary_key=True)
    rstrtname = models.CharField(db_column='restaurantName', max_length=24)
    deliveryleast = models.IntegerField(db_column='deliveryLeast')
    distance = models.FloatField(db_column='distance')
    leasttime = models.IntegerField(db_column='leastTime')

    class Meta:
        managed = False
        db_table = "view_fav"


class ElemedbViewRstrt(models.Model):
    rstrtname = models.CharField(db_column='restaurantName', primary_key=True, max_length=24)
    rstrtclass = models.CharField(db_column='restaurantClass', max_length=15)
    rstrtaddr = models.CharField(db_column='restaurantAddress', max_length=96)
    rstrtphone = models.CharField(db_column='restaurantPhone', max_length=15)
    wrkinhrsfrom = models.TimeField(db_column='workingHoursFrom')
    wrkinhrsto = models.TimeField(db_column='workingHoursTo')
    class Meta:
        managed = False
        db_table = "view_rstrt"


class ElemedbViewMenu(models.Model):
    rstrtname = models.CharField(db_column='restaurantName', max_length=24, primary_key=True)
    dishname = models.CharField(db_column='dishName', max_length=20)  # Field name made lowercase.
    dishprice = models.FloatField(db_column='dishPrice')  # Field name made lowercase.
    dishsaleamount = models.IntegerField(db_column='SaleAmount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "view_menu"


class ElemedbViewOrder(models.Model):
    ordercode = models.CharField(db_column='orderCode', primary_key=True, max_length=20)
    username = models.CharField(db_column='userName', max_length=24)
    rstrtname = models.CharField(db_column='restaurantName', max_length=24)
    dishname = models.CharField(db_column='dishName', max_length=24)
    dishprice = models.FloatField(db_column='dishPrice')
    pay = models.FloatField(db_column='sum2pay')
    ordertime = models.DateTimeField(db_column='ordertime')
    contact = models.CharField(db_column='contactName', max_length=24)
    phone = models.CharField(db_column='contactPhone', max_length=11)
    address = models.CharField(db_column='contactAddress', max_length=96)
    deliveryPName = models.CharField(db_column='deliveryPName', max_length=24)
    deliveryPPhone = models.CharField(db_column='deliveryPPhone', max_length=11)

    class Meta:
        managed = False
        db_table = "view_order"
