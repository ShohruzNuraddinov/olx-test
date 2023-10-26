from django.urls import path, include
from ads.views import AdsListView

urlpatterns = [path("", AdsListView.as_view(), name="ads-list")]
