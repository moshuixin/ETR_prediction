from django.conf.urls import url
from prognose.views import views
from prognose.views import prognose_views

urlpatterns = [
    url(r'^$',
        views.home,
        name='home'),
    url(r'about/$',
        views.about,
        name='about'),
    url(r'^getCompanyForDropdown/$', prognose_views.getCompanyForDropdown, name='getCompanyForDropdown'),
    url(r'^getIndustryForAllCompany/$', prognose_views.getIndustryForAllCompany, name='getIndustryForAllCompany'),
    url(r'^getValuesForPredict/$', prognose_views.getValuesForPredict, name='getValuesForPredict'),

]