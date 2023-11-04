from django.urls import path, include
from ads.views import AdsListView, MainCategoryListView, FilterCategoryListView

urlpatterns = [
    path("", AdsListView.as_view(), name="ads-list"),
    path("category/main/", MainCategoryListView.as_view(), name="ads-list"),
    path("category/filter/", FilterCategoryListView.as_view(), name="ads-list"),
]
