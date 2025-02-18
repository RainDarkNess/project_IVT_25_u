# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adressuser(models.Model):
    idadressuser = models.AutoField(db_column='idAdressUser', primary_key=True)  # Field name made lowercase.
    indexhome = models.IntegerField(db_column='indexHome')  # Field name made lowercase.
    sity = models.CharField(max_length=50)
    streat = models.CharField(max_length=80)
    numberstreat = models.IntegerField(db_column='numberStreat')  # Field name made lowercase.
    numberapartment = models.IntegerField(db_column='numberApartment')  # Field name made lowercase.
    idusers = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUsers')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adressuser'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Books(models.Model):
    idbooks = models.AutoField(db_column='idBooks', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=150)
    description = models.TextField()
    idcategory = models.ForeignKey('Category', models.DO_NOTHING, db_column='idCategory')  # Field name made lowercase.
    idcover = models.ForeignKey('Cover', models.DO_NOTHING, db_column='idCover')  # Field name made lowercase.
    idgenre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='idGenre')  # Field name made lowercase.
    idwriter = models.ForeignKey('Writer', models.DO_NOTHING, db_column='idWriter')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'books'


class Category(models.Model):
    idcategory = models.AutoField(db_column='idCategory', primary_key=True)  # Field name made lowercase.
    category = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'category'


class Cover(models.Model):
    idcover = models.AutoField(db_column='idCover', primary_key=True)  # Field name made lowercase.
    cover = models.CharField(max_length=50)
    descriptioncover = models.TextField(db_column='descriptionCover', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cover'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Genre(models.Model):
    namegenre = models.CharField(db_column='nameGenre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genre'


class Orderbooks(models.Model):
    idorder = models.AutoField(db_column='idOrder', primary_key=True)  # Field name made lowercase.
    idstatus = models.ForeignKey('Status', models.DO_NOTHING, db_column='idStatus')  # Field name made lowercase.
    idstoreuserone = models.ForeignKey('Storeuser', models.DO_NOTHING, db_column='idStoreUserOne')  # Field name made lowercase.
    idstoreusertwo = models.ForeignKey('Storeuser', models.DO_NOTHING, db_column='idStoreUserTwo', related_name='orderbooks_idstoreusertwo_set')  # Field name made lowercase.
    tradenumberone = models.CharField(db_column='tradeNumberOne', max_length=100)  # Field name made lowercase.
    tradenumbertwo = models.CharField(db_column='tradeNumberTwo', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderbooks'


class Status(models.Model):
    idstatus = models.AutoField(db_column='idStatus', primary_key=True)  # Field name made lowercase.
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'status'


class Storeuser(models.Model):
    idstorebook = models.AutoField(db_column='idStoreBook', primary_key=True)  # Field name made lowercase.
    idbooks = models.ForeignKey(Books, models.DO_NOTHING, db_column='idBooks')  # Field name made lowercase.
    idusers = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUsers')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storeuser'


class Users(models.Model):
    idusers = models.AutoField(db_column='idUsers', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=80)
    password = models.CharField(max_length=100)
    dateregistration = models.DateField(db_column='dateRegistration')  # Field name made lowercase.
    rating = models.FloatField(blank=True, null=True)
    phone = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'users'


class Writer(models.Model):
    idwriter = models.AutoField(db_column='idWriter', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'writer'
