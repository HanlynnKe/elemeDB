from django.contrib import admin
from .models import *
from .view_models import *
# Register your models here.
admin.site.register(ElemedbUser)
admin.site.register(ElemedbUseraddr)
admin.site.register(ElemedbUserfav)
admin.site.register(ElemedbRstrt)
admin.site.register(ElemedbRstrtmenu)
admin.site.register(ElemedbUserorder)
admin.site.register(ElemedbDelivery)
admin.site.register(ElemedbDeliveryperson)
# admin.site.register(ElemedbViewUser)
# admin.site.register(ElemedbViewFav)
# admin.site.register(ElemedbViewUserAddr)
# admin.site.register(ElemedbViewOrder)
# admin.site.register(ElemedbViewRstrt)
# admin.site.register(ElemedbViewMenu)
