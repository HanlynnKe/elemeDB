# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ElemedbDelivery(models.Model):
    deliverycode = models.CharField(db_column='deliveryCode', primary_key=True,
                                    max_length=15)  # Field name made lowercase.
    userorder_ordercode = models.ForeignKey('ElemedbUserorder', models.DO_NOTHING,
                                            db_column='userOrder_orderCode',
                                            related_name="userOrder_orderCode_deliv")  # Field name made lowercase.
    deliveryperson_deliverypcode = models.ForeignKey('ElemedbDeliveryperson', models.DO_NOTHING,
                                                     db_column='deliveryPerson_deliveryPCode',
                                                     related_name="deliveryPerson_deliveryPCode_deliv")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elemedb_delivery'
        unique_together = (('deliverycode', 'deliveryperson_deliverypcode', 'userorder_ordercode'),)


class ElemedbDeliveryperson(models.Model):
    deliverypcode = models.CharField(db_column='deliveryPCode', primary_key=True,
                                     max_length=15)  # Field name made lowercase.
    deliverypname = models.CharField(db_column='deliveryPName', max_length=24)  # Field name made lowercase.
    deliverypphone = models.CharField(db_column='deliveryPPhone', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elemedb_deliveryPerson'


class ElemedbRstrt(models.Model):
    rstrtname = models.CharField(db_column='rstrtName', primary_key=True, max_length=24)  # Field name made lowercase.
    rstrtclass = models.CharField(db_column='rstrtClass', max_length=15)  # Field name made lowercase.
    rstrtaddr = models.CharField(db_column='rstrtAddr', max_length=96)  # Field name made lowercase.
    rstrtphone = models.CharField(db_column='rstrtPhone', max_length=15)  # Field name made lowercase.
    wrkinhrsfrom = models.TimeField(db_column='wrkinHrsFrom')  # Field name made lowercase.
    wrkinhrsto = models.TimeField(db_column='wrkinHrsTo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elemedb_rstrt'


class ElemedbRstrtmenu(models.Model):
    dishcode = models.CharField(db_column='dishCode', primary_key=True, max_length=15)  # Field name made lowercase.
    dishname = models.CharField(db_column='dishName', max_length=20)  # Field name made lowercase.
    dishprice = models.FloatField(db_column='dishPrice')  # Field name made lowercase.
    dishsaleamount = models.IntegerField(db_column='dishSaleAmount')  # Field name made lowercase.
    rstrt_rstrtname = models.ForeignKey(ElemedbRstrt, models.DO_NOTHING,
                                        db_column='rstrt_rstrtName',
                                        related_name="rstrt_rstrtName_menu")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elemedb_rstrtMenu'
        unique_together = (('dishcode', 'rstrt_rstrtname'),)


class ElemedbUser(models.Model):
    username = models.CharField(db_column='userName', primary_key=True, max_length=24)  # Field name made lowercase.
    userphone = models.CharField(db_column='userPhone', max_length=11)  # Field name made lowercase.
    logincode = models.CharField(db_column='loginCode', max_length=16)  # Field name made lowercase.
    paycode = models.CharField(db_column='payCode', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elemedb_user'


class ElemedbUseraddr(models.Model):
    addresscode = models.IntegerField(db_column='addressCode', primary_key=True)  # Field name made lowercase.
    contact = models.CharField(max_length=24)
    gender = models.CharField(max_length=3)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=96)
    tag = models.CharField(max_length=12, blank=True, null=True)
    user_username = models.ForeignKey(ElemedbUser, models.DO_NOTHING,
                                      db_column='user_userName',
                                      related_name="user_userName_addr")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elemedb_userAddr'
        unique_together = (('addresscode', 'user_username'),)


class ElemedbUserfav(models.Model):
    favID = models.IntegerField(db_column="favID", primary_key=True)
    user_username = models.ForeignKey(ElemedbUser, models.DO_NOTHING, db_column='user_userName',
                                      related_name="user_userName_fav")  # Field name made lowercase.
    rstrt_rstrtname = models.ForeignKey(ElemedbRstrt, models.DO_NOTHING, db_column='rstrt_rstrtName',
                                        related_name="rstrt_rstrtName_fav")  # Field name made lowercase.
    deliveryleast = models.IntegerField(db_column='deliveryLeast')  # Field name made lowercase.
    distance = models.FloatField()
    leasttime = models.IntegerField(db_column='leastTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elemedb_userFav'
        unique_together = (('user_username', 'rstrt_rstrtname'),)


class ElemedbUserorder(models.Model):
    ordercode = models.CharField(db_column='orderCode', primary_key=True, max_length=20)  # Field name made lowercase.
    pay = models.FloatField()
    ordertime = models.DateTimeField(db_column='orderTime')  # Field name made lowercase.
    rstrtmenu_dishcode = models.ForeignKey(ElemedbRstrtmenu, models.DO_NOTHING,
                                           db_column='rstrtMenu_dishCode',
                                           related_name="rstrtMenu_dishCode_ord")  # Field name made lowercase.
    rstrtmenu_rstrt_rstrtname = models.ForeignKey(ElemedbRstrtmenu, models.DO_NOTHING,
                                                  db_column='rstrtMenu_rstrt_rstrtName',
                                                  related_name="rstrtMenu_rstrt_rstrtName_ord")  # Field name made lowercase.
    useraddr_addresscode = models.ForeignKey(ElemedbUseraddr, models.DO_NOTHING, db_column='userAddr_addressCode',
                                             related_name="userAddr_addressCode_ord")  # Field name made lowercase.
    useraddr_user_username = models.ForeignKey(ElemedbUseraddr, models.DO_NOTHING, db_column='userAddr_user_userName',
                                               related_name="userAddr_user_userName_ord")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elemedb_userOrder'
        unique_together = (('ordercode', 'rstrtmenu_dishcode', 'rstrtmenu_rstrt_rstrtname', 'useraddr_addresscode',
                            'useraddr_user_username'),)
