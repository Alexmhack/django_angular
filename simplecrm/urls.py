from django.contrib import admin
from django.urls import path
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
	import debug_toolbar

	# django-debug-toolbar url
	urlpatterns += [
		path('__debug__', include(debug_toolbar.urls)),
	]
