from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Wildio API",
        default_version='v1',
        description="Wildio API description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)