import datetime

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
    img = models.ImageField(upload_to='avatars/')
    rating = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(_("address"), max_length=40)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username


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
    idcategory = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, db_column='idCategory')  # Field name made lowercase.
    idcover = models.ForeignKey('Cover', on_delete=models.SET_NULL, null=True, db_column='idCover')  # Field name made lowercase.
    idgenre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, db_column='idGenre')  # Field name made lowercase.
    idwriter = models.ForeignKey('Writer', on_delete=models.SET_NULL, null=True, db_column='idWriter')  # Field name made lowercase.
    idAuthorUser = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, db_column='idAuthorUser')  # Field name made lowercase.

    def __str__(self):
        return self.name


class Category(models.Model):
    idcategory = models.AutoField(db_column='idCategory', primary_key=True)  # Field name made lowercase.
    category = models.CharField(max_length=50)
    idAuthorUser = models.ForeignKey('CustomUser', models.DO_NOTHING, db_column='idAuthorUser')  # Field name made lowercase.

    def __str__(self):
        return self.category


class Cover(models.Model):
    idcover = models.AutoField(db_column='idCover', primary_key=True)  # Field name made lowercase.
    cover = models.CharField(max_length=50)
    img = models.ImageField(upload_to='books')
    descriptioncover = models.TextField(db_column='descriptionCover', blank=True,
                                        null=True)
    idAuthorUser = models.ForeignKey('CustomUser', models.DO_NOTHING, db_column='idAuthorUser')  # Field name made lowercase.

    def __str__(self):
        return str(self.cover)


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
    namegenre = models.CharField(db_column='nameGenre', unique=True, max_length=50)  # Field name made lowercase.
    idAuthorUser = models.ForeignKey('CustomUser', models.DO_NOTHING, db_column='idAuthorUser')  # Field name made lowercase.

    def __str__(self):
        return self.namegenre


class OrderRequests(models.Model):
    idorder = models.AutoField(db_column='idOrder', primary_key=True)
    namebookrequest = models.CharField(max_length=1024, db_column='nameBookRequest')
    booktorequest = models.ForeignKey('Books', models.DO_NOTHING, db_column='bookToRequest')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, db_column='category')
    userrequest = models.ForeignKey('CustomUser', models.DO_NOTHING, db_column='userRequest')
    address = models.CharField(db_column='address', max_length=1024)
    dateorder = models.DateTimeField(db_column='dateorder', default=datetime.datetime.now)
    canView = models.BooleanField(db_column='canView', default=True)


class Orderbooks(models.Model):
    idorderbooks = models.AutoField(db_column='idOrderBooks', primary_key=True)
    status = models.IntegerField(db_column='status', null=True, default=0)
    bookone = models.ForeignKey('Books', on_delete=models.CASCADE, null=True, related_name='orderbooks_as_bookone')
    booktwo = models.ForeignKey('Books', on_delete=models.CASCADE, null=True, related_name='orderbooks_as_booktwo')
    addressrequester = models.CharField(db_column='addressRequester', null=True, max_length=1024)
    addressbookowner = models.CharField(db_column='addressBookOwner', null=True, max_length=1024)

    useridone = models.ForeignKey('CustomUser', models.DO_NOTHING, null=True, related_name='orderbooks_as_useridone')
    useridonetoggle = models.CharField(db_column='userIdOneToggle', null=True, max_length=1024, default=0)

    useridtwo = models.ForeignKey('CustomUser', models.SET_NULL, null=True, related_name='orderbooks_as_useridtwo')
    useridtwotoggle = models.CharField(db_column='userIdTwoToggle', null=True, max_length=1024, default=0)

    dateorder = models.DateTimeField(db_column='dateorder', null=True, default=datetime.datetime.now)
    idorder = models.ForeignKey('OrderRequests', on_delete=models.SET_NULL, null=True, db_column='idOrder')


class ActionOrderbooks(models.Model):
    idorderbooks = models.ForeignKey('Orderbooks', on_delete=models.CASCADE, null=True, db_column='idorderbooks')
    statususerone = models.CharField(db_column='statususerone', null=True, default='0', max_length=2)
    dateorderone = models.DateTimeField(db_column='dateorderone', null=True, default=datetime.datetime.now)

    statususertwo = models.CharField(db_column='statususertwo', null=True, default='0', max_length=2)
    dateordertwo = models.DateTimeField(db_column='dateordertwo', null=True, default=datetime.datetime.now)

# idstatus = models.ForeignKey('Status', models.DO_NOTHING, db_column='idStatus')  # Field name made lowercase.
    # idstoreuserone = models.ForeignKey('Storeuser', models.DO_NOTHING,
    #                                    db_column='idStoreUserOne')  # Field name made lowercase.
    # idstoreusertwo = models.ForeignKey('Storeuser', models.DO_NOTHING, db_column='idStoreUserTwo',
    #                                    related_name='orderbooks_idstoreusertwo_set')  # Field name made lowercase.
    # tradenumberone = models.CharField(db_column='tradeNumberOne', max_length=100)  # Field name made lowercase.
    # tradenumbertwo = models.CharField(db_column='tradeNumberTwo', max_length=100)  # Field name made lowercase.



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
    idAuthorUser = models.ForeignKey('CustomUser', models.DO_NOTHING, db_column='idAuthorUser')  # Field name made lowercase.

    def __str__(self):
        return str(self.lastname) + " " + str(self.firstname)
