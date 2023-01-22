'''from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('Usuário deve ter um email')

        if not username:
            raise ValueError('Usuário deve ter um username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            last_name = last_name,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_activate = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    STORE = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (STORE, 'Loja'),
        (CUSTOMER, 'cliente'),
    )


    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50, unique=True)
    username = models.CharField('Username', max_length=50, unique=True)
    phone_number = models.CharField('Telefone', max_length=10, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    # required fields
    date_joined = models.DateTimeField('Data criação', auto_now_add=True)
    last_login = models.DateTimeField('Último login', auto_now_add=True)
    created_date = models.DateTimeField('')
'''