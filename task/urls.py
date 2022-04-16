from rest_framework.routers import DefaultRouter
from task import views

router = DefaultRouter()
router.register("category", views.CategoryViewSet)
router.register("subcategory", views.SubcategoryViewSet)
router.register("advertisement", views.AdvertisementViewSet)

urlpatterns = router.urls
