from django.db import models

# Create your models here.
from django.db.models import JSONField
from datetime import datetime, timedelta, date

class setcust(models.Model):
    cstno = models.AutoField(primary_key=True, verbose_name = "客戶編號")
    cstpatcode = models.CharField(max_length=20,blank=True,null=True, verbose_name = "病歷號碼")  
    cststaff =  models.CharField(max_length=10,blank=True,null=True, verbose_name = "員工編號") 
    cstname = models.CharField(max_length=50,blank=True,null=True, verbose_name = "客戶姓名")
    cstbirth = models.DateField(blank=True,null=True, verbose_name = "出生日期")    
    sex_choice = ( (0,'女'), (1, '男'), (2,'多元'),(9,'-')) 
    cstsex = models.IntegerField( choices=sex_choice, default=9, verbose_name = "性別" )
    cstlogin = models.CharField(max_length=30,blank=True,null=True, verbose_name = "登入帳號")
    cstpassword = models.CharField(max_length=120,blank=True,null=True, verbose_name = "通行密碼")  
    cstmobile = models.CharField(max_length=30,blank=True,null=True, verbose_name = "行動電話")
    cstemail = models.EmailField(max_length = 254,blank=True,null=True, verbose_name = "電子信箱")
    cstzip = models.CharField(max_length = 10,blank=True,null=True, verbose_name = "郵遞區號")    
    cstaddress = models.CharField(max_length = 254,blank=True,null=True, verbose_name = "通訊地址")
    cstduedate = models.DateField(blank=True,null=True, verbose_name = "到職日期")   
    cstresign = models.DateField(blank=True,null=True, verbose_name = "離職日期")           
    inswho = models.IntegerField(blank=True,null=True, verbose_name = "建立人員")  
    insdate = models.DateTimeField(auto_now_add=True,blank=True,null=True, verbose_name = "建立時間")  
    modwho = models.IntegerField(blank=True,null=True, verbose_name = "最後修改") 
    moddate = models.DateTimeField(auto_now=True,blank=True,null=True, verbose_name = "最後修改時間") 

    class Meta:
        db_table = 'setcust'

    # GeeksModel
 
    # class Person(models.Model):
#     SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     name = models.CharField(max_length=60)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    # MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    # name = models.CharField(max_length=60)
    # medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

    # class Meta:
    #     db_table = 'setcust'
#     #     unique_together = (('cmp_id', 'pass_no', 'pass_tp', 'xseq'),)          
# staff = []
# staff.append(['蔡凱宙','kaijow.tsai@gmail.com','','0001'])
# staff.append(['蔡迪淮','huai4346@gmail.com','0928055753','0002'])
# staff.append(['謝永姺','shean8753@gmail.com','0922393867','0005'])
# staff.append(['張宜珍','jenny654321@gmail.com','0905285652','0006'])
# staff.append(['馬能嫻','marria06130613@gmail.com','0917257639','0010'])
# staff.append(['林照玲','angeline818821@gmail.com','0989355034','0021'])
# staff.append(['曾秀琴','ey882114@gmail.com','0929311506','0027'])
# staff.append(['陳乙玉','haluchenx@gmail.com','0953642557','0028'])
# staff.append(['周佩蓉','ju.jungart@gmail.com','0909327111','0030'])
# staff.append(['鄭玲','sara7830g@gmail.com','0963101780','0038'])
# staff.append(['古恩綺','candice149133@gmail.com','0955939543','0039'])
# staff.append(['許曉盈','h.y.hsu731@gmail.com','0911952258','0041'])
# staff.append(['葉心渝','iloveamerica03@gmail.com','0988525579','0042'])
# staff.append(['吳聲清','vance.wsc@gmail.com','0910110831','dev'])
# i = 0
# while i < len(staff):
#     person = staff[i]
#     cust = setcust.objects.create(cststaff=person[3],cstname=person[0],cstmobile=person[2],cstemail=person[1])    
#     cust.save()
#     i += 1


# .\manage.py makemigrations
#  python .\manage.py migrate
