from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class TenantBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, tenant=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username, tenant=tenant)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
