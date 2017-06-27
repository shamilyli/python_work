from django.conf.urls import url

from . import views

urlpatterns = [
	#index
	url(r'^$', views.index, name='index'),

	# showing all topics
	url(r'^topics/$', views.topics, name = 'topics'),

	#detail for the topic
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]