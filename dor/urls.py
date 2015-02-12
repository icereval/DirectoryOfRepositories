from django.conf.urls import url, include, patterns
from django.contrib import admin
from dor import views
from dor import models
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
#import rest_framework_swagger
from dor import api

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'repos', views.RepositoryViewSet)
router.register(r'journals', views.JournalViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'taxonomy', views.TaxonomyViewSet)
router.register(r'standards', views.StandardsViewSet)
router.register(r'contenttype', views.ContentTypeViewSet)

# Dictionary of models to be used in one template
model_list = {
    'queryset': models.Taxonomy.objects.all(),
    'template_object_name': 'taxonomy',
    'extra_context': {
        'standards': models.Standards.objects.all(),
        'content-types': models.ContentType.objects.all()
    }
}

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^swag/', include('rest_framework_swagger.urls')),
    url(r'^routes/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^$', views.index, name='index'),
    url(r'^ajax_search/', 'dor.views.repositorySearch'),
    url(r'^search/', 'dor.views.repositoryList'),
    url(r'^submissions/$', 'dor.views.submission'),
    url(r'^api/repos/$', api.RepoList.as_view()),
    url(r'^api/repos/[a-zA-Z/]+/$', api.RepoDetail.as_view()),
)
