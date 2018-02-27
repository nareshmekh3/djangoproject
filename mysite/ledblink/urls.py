from django.conf.urls import url
from ledblink import views

urlpatterns=[
	
        #url(r'^$',views.HomePageView, name='home'),
        #url(r'^$',views.led1,name='led1'),
        #url(r'^$',views.LedPageView.as_view(), name='led'),
         #url(r'^$',views.blinker),
     #url(r'^$',views.index, name='index'),
         url(r'^led/$',views.led,name='led'),
        # url(r'^temp/$',views.temp,name='temp'),
         #url(r'^$',views.led,name='led'),
         #url(r'^$',views.led1),
        #url(r'^$',views.led,name='led'),

        
        #url(r'^admin/',views.blinker,name='index'),
]
