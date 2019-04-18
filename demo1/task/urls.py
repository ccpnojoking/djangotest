from django.conf.urls import url
from . import views

app_name = "task"

urlpatterns = [
    url(r'^home/$', views.home,name="home"),
    url(r"^list/$",views.list,name="list"),
    url(r"^detail/(\d+)/$",views.detail,name="detail"),
    url(r"^delete/(\d+)/$",views.delete,name="delete"),
    url(r"^addrole/(\d+)/$",views.addrole,name="addrole"),
    url(r"^addrolehand$",views.addrolehand,name="addrolehand"),
]