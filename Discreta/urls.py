from django.conf.urls import patterns, include, url

from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('Home.views',
    url(r'^$','home',name='home'),
    url(r'^about/$','about',name='about'),
    url(r'^contacto/$','contacto',name='contact'),
    url(r'^contact/thanks/$','thankyou',name='thanks'),


)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'Discreta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

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

)