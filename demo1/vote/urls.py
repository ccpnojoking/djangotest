from django.conf.urls import url
from . import views

app_name = "vote"

urlpatterns = [
    url(r"^home/$",views.home,name="home"),
    url(r"^list/$",views.qlist,name="list"),
    url(r"^choice/(\d+)/$",views.choice,name="choice"),
    url(r"^count/$",views.count,name="count"),
    url(r"^counts/(\d+)/$",views.counts,name="counts"),
]