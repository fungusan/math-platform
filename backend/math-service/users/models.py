from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, user_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(email=self.normalize_email(email), user_name=user_name)
        user.set_password(password)  # Hashes the password
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Renamed from user_id for convention
    user_name   = models.CharField(max_length=200)
    email       = models.EmailField(max_length=254, unique=True)  # Add unique for integrity
    is_active   = models.BooleanField(default=True)  # Required for AbstractBaseUser
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD  = 'email'  # Use email for login instead of username
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.email