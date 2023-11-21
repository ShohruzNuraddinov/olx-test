from django.urls import path, include
from ads.views import AdsListView, MainCategoryListView, FilterCategoryListView, VipAdsListView, AdsCreateView, FilterAdsListView, AttributeValueCreateView, AttributeOptionValueCreateView

urlpatterns = [
    path("ads/", AdsListView.as_view(), name="ads-list"),
    path('ads/add/', AdsCreateView.as_view(), name='ads-create'),
    path('ads/vip/', VipAdsListView.as_view(), name='vip_list'),
    path('ads/filter/', FilterAdsListView.as_view(), name='ads_filter'),
    path("category/main/", MainCategoryListView.as_view(), name="ads-list"),
    path("category/filter/", FilterCategoryListView.as_view(), name="ads-list"),
    path('attribute/create/', AttributeValueCreateView.as_view(),
         name='attribute-create'),
    path('attribute/option/create/', AttributeOptionValueCreateView.as_view(),
         name='attribute-option-create')
]
