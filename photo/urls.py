from django.urls import path, re_path
from photo.views import *
from photo.models import Photo

app_name = "photo"

urlpatterns = [
    path("", photo_list, name="photo_list"),
    path("detail/<int:pk>/", PhotoDetailView.as_view(), name="photo_detail"),
    path("upload/", PhotoUploadView.as_view(), name="photo_upload"),
    path("delete/<int:pk>/", PhotoDeleteView.as_view(), name="photo_delete"),
    path("update/<int:pk>/", PhotoUpdateView.as_view(), name="photo_update"),
    re_path(r"^like/$", post_like, name="post_like"),
    # re_path(r"^tag/(?P<tag>[^/]+(?u))/$", PostTOL.as_view(), name="tagged_object_list"),
    re_path(r"^tag/(?P<tag>[^/]+)/$", PostTOL.as_view(), name="tagged_object_list"),
]
