"""ikasOfis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.urls import include, path, re_path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import User, Group

from tutorial.views import people
from tutorial.views import expense
import table
from table.views import index_redirect




# urlpatterns = [
#
#     path('moneyrelations/', include('MoneyRelations.urls')),
#
#     url(r'^jet/', include(('jet.urls', 'jet'))),
#     url(r'^jet/dashboard/', include(('jet.dashboard.urls', 'jet-dashboard'))),
#     path('', admin.site.urls, name='home'),
#
# ]

urlpatterns = (
    #url(r'^$', RedirectView.as_view(url=reverse_lazy('products:list'))),
    url('admin/', admin.site.urls),
    url(r'^people/', people),
    url(r'^expensee/', expense ),
    url(r'^$', table.views.index_redirect, name='index_redirect'),
    url(r'^table/', include('table.urls')),



    # re_path(r' ^ simple-autocomplete / ', include('simple_autocomplete.urls', namespace='simple_autocomplete')),
#url(r'^store/', include('products.urls', namespace='products')),

)


admin.site.site_header = "IKAS Admin"
admin.site.site_title = "IKAS Admin Portalı"
admin.site.index_title = "IKAS Portalına hoşgeldiniz!"
admin.site.unregister(User)
admin.site.unregister(Group)
#urlpatterns += staticfiles_urlpatterns()

#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns =[
#     #path(r'^jet/', 'jet.urls''jet'),  # Django JET URLS
#     path(r/', admin.site.urls),
#
# ]
