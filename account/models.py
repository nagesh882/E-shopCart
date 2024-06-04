from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# I create custom user model as account with their superadmin model with account manager

class AccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, **extra_fields):

        if not username:
            raise ValueError("Username field is required!")

        if not email:
            raise ValueError("Email field is required!")
        
        email = self.normalize_email(email)
        user_account = self.model(
            email = email,
            username = username,
            first_name = first_name,
            last_name = last_name,
            **extra_fields
        )
        user_account.set_password(password)
        user_account.save(using=self._db)
        return user_account

    def create_superuser(self, email, username, first_name, last_name, password=None, **extra_fields):

        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff field must have true")
        
        if extra_fields.get("is_admin") is not True:
            raise ValueError("is_admin field must have true")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser field must have true")

        email = self.normalize_email(email)
        user_account = self.create_user(
            email = email,
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password,
            **extra_fields
        )
        user_account.save(using=self._db)
        return user_account

class Account(AbstractBaseUser):
    account_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # instead of username we use email field
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = AccountManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User Account"

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True