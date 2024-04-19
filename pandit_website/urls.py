from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 
from . import views;
from contacts import views as contact_view
from services import views as mainservices
from services import views as home
from django.conf import settings  # new
from django.conf.urls.static import static  # new
from booking import views as bookingform
from django.contrib.sitemaps.views import sitemap  # new
from services.models import Typesofpuja

from pandit_website.sitemaps import TypesofpujaSitemap
from .views import RobotsTxtView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path('accounts/', include('django.contrib.auth.urls')),
    path("", home.home, name="home"),
    path('home/details/<int:id>', mainservices.details, name='detailshome'),
    path('about/', views.about, name='about'),
    path('all_service/', mainservices.mainservices, name='all_services'),
    path('festive/', mainservices.festive_service, name='festival_puja' ),
    path('festive/details/<int:id>', mainservices.details, name='details'),
    path('hawan/', mainservices.hawan_service, name='hawan_service' ),
    path('hawan/details/<int:id>', mainservices.details, name='details'),
    path('katha/', mainservices.katha_service, name='katha_service' ),
    path('katha/details/<int:id>', mainservices.details, name='details'),
    path('shanti_puja/', mainservices.santi_service, name='shanti_puja' ),
    path('shanti_puja/details/<int:id>', mainservices.details, name='details'),
    path('sanskar_vidhi/', mainservices.sanskar_service, name='sanshkar_vidhi' ),
    path('sanskar_vidhi/details/<int:id>', mainservices.details, name='details'),
    path('sthapan_puja/', mainservices.sthapan_service, name='sthapan_service' ),
    path('sthapan_puja/details/<int:id>', mainservices.details, name='details'),
    path('contact/',contact_view.contact_view,name='contact'),
    path('destination_wedding/', views.destination_wedding, name='havan' ),
    path('nri_service/', views.nri_service, name='nri_service' ),
    path('termandservice/', views.termandservice, name='termandservice' ),
    path('book_now/<int:id>', bookingform.my_form_view, name='book_now'),
    path('book_now/booking_success/<int:id>', bookingform.succsess, name='succsess'),
    path("robots.txt", RobotsTxtView.as_view(content_type="text/plain"), name="robots"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"home/details/<int:id>": TypesofpujaSitemap}},
    ),
    
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new