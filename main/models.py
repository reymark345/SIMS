from django.db import models
from datetime import datetime  


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_staff= models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class LibResponsibilityCenter(models.Model):
    code = models.CharField(max_length=128,blank=True, null=True)
    acronym = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lib_responsibility_center'

class LibFundSource(models.Model):
    name = models.CharField(max_length=128,blank=True, null=True)
    cluster = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lib_fund_source'

class LibUacs(models.Model):
    code = models.CharField(max_length=128,blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lib_uacs'

class LibItems(models.Model):
    name = models.CharField(max_length=128,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by_user = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'lib_items'

class LibUnits(models.Model):
    name = models.CharField(max_length=128,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'lib_units'

class Ris(models.Model):
    responsibility_center = models.ForeignKey(LibResponsibilityCenter, models.DO_NOTHING)
    uacs = models.ForeignKey(LibUacs, models.DO_NOTHING)
    fund_source = models.ForeignKey(LibFundSource, models.DO_NOTHING)
    ris_no = models.CharField(max_length=128,blank=True, null=True)
    purpose = models.CharField(max_length=128,blank=True, null=True)
    transaction_year = models.DateTimeField(default=datetime.now,blank=True, null=True)
    created_by_user = models.IntegerField(blank=True, null=True)
    issued_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ris'

class RisItems(models.Model):
    ris = models.ForeignKey(Ris, models.DO_NOTHING)
    item = models.ForeignKey(LibItems, models.DO_NOTHING)
    unit = models.ForeignKey(LibUnits, models.DO_NOTHING)
    uacs = models.ForeignKey(LibUacs, models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)
    total = models.FloatField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ris_items'

class PoReceived(models.Model):
    responsibility_center = models.ForeignKey(LibResponsibilityCenter, models.DO_NOTHING)
    fund_source = models.ForeignKey(LibFundSource, models.DO_NOTHING)
    supplier = models.CharField(max_length=128,blank=True, null=True)
    po_number = models.CharField(max_length=128,blank=True, null=True)
    dv_number = models.CharField(max_length=128,blank=True, null=True)
    remarks = models.CharField(max_length=255,blank=True, null=True)
    transaction_year = models.DateTimeField(default=datetime.now,blank=True, null=True)
    created_by_user = models.IntegerField(blank=True, null=True)
    issued_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'po_received'

class PoReceivedItems(models.Model):
    po_received = models.ForeignKey(PoReceived, models.DO_NOTHING)
    item = models.ForeignKey(LibItems, models.DO_NOTHING)
    unit = models.ForeignKey(LibUnits, models.DO_NOTHING)
    uacs = models.ForeignKey(LibUacs, models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)
    total = models.FloatField(null=True, blank=True, default=0)
    is_food = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now,blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'po_received_items'


class UserDetails(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=128, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    position = models.CharField(max_length=128, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_details'




