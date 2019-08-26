from django.contrib import admin
from .models import web1
from .models import News
from .models import tb_Registration
from .models import basic,employee


# Register your models here.
admin.site.register(web1)
admin.site.register(News)
admin.site.register(tb_Registration)
admin.site.register(basic)
admin.site.register(employee)