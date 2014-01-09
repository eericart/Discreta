from django.conf.urls import patterns, include, url

from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('Home.views',
    url(r'^$','home',name='home'),
    url(r'^about/$','about',name='about'),
    url(r'^contacto/$','contacto',name='contact'),
    url(r'^contact/thanks/$','thankyou',name='thanks'),
    url(r'^contact/thanks/$','thankyou',name='thanks'),
    url(r'^profesores/page/(?P<pagina>.*)/$','profesores_v',name='profesores'),
    url(r'^profesor/(?P<id_prof>.*)/$','singleProfe_v',name='single_profe'),
    url(r'^api/get_profe/$', 'get_profe', name='get_profe'),



)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
    url (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
 )
urlpatterns += patterns('account.views',
    #Sigup, sign & sign out
    url(r'^login/$','login_v',name='login_v'),
    url(r'^logout/$','logout_v',name='logout_v'),
    url(r'^signup/$','sign_up',name='sign_up'),
    url(r'^index/$','home_profile',name='home_p'),

)

urlpatterns += patterns('ws.views',
    url(r'^ws/User/$','wsUser_view',name= "ws_user_url"),
    url(r'^ws/Profesor/$','wsProf_view',name= "ws_prof_url"),
)

