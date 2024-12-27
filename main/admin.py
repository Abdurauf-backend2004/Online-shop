from django.contrib import admin

from main.models import *

class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('id','mahsulot_nomi','chiqarilgan_sana','yaroqlilik_muddati','mavjud_miqdori')
    list_display_links = ('id','mahsulot_nomi')
#
# class MahsulotInline(admin.StackedInline):
#     model = Mahsulot
#     extra = 1
# class BuyurtmaAdmin(admin.ModelAdmin):
#     list_display = ('mijoz_id','mahsulot_id','jami_narx','sana','status')
#     inlines = (MahsulotInline,)





admin.site.register(Mahsulot,MahsulotAdmin)
admin.site.register(Mijoz)
admin.site.register(Buyurtma)
