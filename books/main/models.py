from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=40, unique=True)
    first_name = models.CharField(_("first_name"), max_length=40)
    last_name = models.CharField(_("last_name"), max_length=40)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # CUSTOM FIELDS
    telephone = models.CharField(max_length=15, blank=True, null=True)
    img = models.ImageField(upload_to='images/')
    rating = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(_("address"), max_length=40)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Adressuser(models.Model):
    idadressuser = models.AutoField(db_column='idAdressUser', primary_key=True)  # Field name made lowercase.
    indexhome = models.IntegerField(db_column='indexHome')  # Field name made lowercase.
    sity = models.CharField(max_length=50)
    streat = models.CharField(max_length=80)
    numberstreat = models.IntegerField(db_column='numberStreat')  # Field name made lowercase.
    numberapartment = models.IntegerField(db_column='numberApartment')  # Field name made lowercase.
    idusers = models.ForeignKey('CustomUser', models.DO_NOTHING, db_column='id')  # Field name made lowercase.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)


class Books(models.Model):
    idbooks = models.AutoField(db_column='idBooks', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=150)
    description = models.TextField()
    idcategory = models.ForeignKey('Category', models.DO_NOTHING, db_column='idCategory')  # Field name made lowercase.
    idcover = models.ForeignKey('Cover', models.DO_NOTHING, db_column='idCover')  # Field name made lowercase.
    idgenre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='idGenre')  # Field name made lowercase.
    idwriter = models.ForeignKey('Writer', models.DO_NOTHING, db_column='idWriter')  # Field name made lowercase.


class Category(models.Model):
    idcategory = models.AutoField(db_column='idCategory', primary_key=True)  # Field name made lowercase.
    category = models.CharField(max_length=50)


class Cover(models.Model):
    idcover = models.AutoField(db_column='idCover', primary_key=True)  # Field name made lowercase.
    cover = models.CharField(max_length=50)
    descriptioncover = models.TextField(db_column='descriptionCover', blank=True,
                                        null=True)  # Field name made lowercase.


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()


class Genre(models.Model):
    namegenre = models.CharField(db_column='nameGenre', max_length=50)  # Field name made lowercase.


class Orderbooks(models.Model):
    idorder = models.AutoField(db_column='idOrder', primary_key=True)  # Field name made lowercase.
    idstatus = models.ForeignKey('Status', models.DO_NOTHING, db_column='idStatus')  # Field name made lowercase.
    idstoreuserone = models.ForeignKey('Storeuser', models.DO_NOTHING,
                                       db_column='idStoreUserOne')  # Field name made lowercase.
    idstoreusertwo = models.ForeignKey('Storeuser', models.DO_NOTHING, db_column='idStoreUserTwo',
                                       related_name='orderbooks_idstoreusertwo_set')  # Field name made lowercase.
    tradenumberone = models.CharField(db_column='tradeNumberOne', max_length=100)  # Field name made lowercase.
    tradenumbertwo = models.CharField(db_column='tradeNumberTwo', max_length=100)  # Field name made lowercase.


class Status(models.Model):
    idstatus = models.AutoField(db_column='idStatus', primary_key=True)  # Field name made lowercase.
    status = models.CharField(max_length=50)


class Storeuser(models.Model):
    idstorebook = models.AutoField(db_column='idStoreBook', primary_key=True)  # Field name made lowercase.
    idbooks = models.ForeignKey(Books, models.DO_NOTHING, db_column='idBooks')  # Field name made lowercase.
    idusers = models.ForeignKey('CustomUser', models.DO_NOTHING, db_column='idUsers')  # Field name made lowercase.


class Writer(models.Model):
    idwriter = models.AutoField(db_column='idWriter', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
