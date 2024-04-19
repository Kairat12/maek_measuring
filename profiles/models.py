from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django_auth_ldap.backend import populate_user, LDAPBackend

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, related_name='profile', on_delete=models.PROTECT)
    givenName = models.CharField(max_length=100, blank=True, help_text="Введите имя")
    lastName = models.CharField(max_length=100, blank=True)
    patronymicName = models.CharField(max_length=100, blank=True, help_text="Введите отчество")
    timesheet_number = models.CharField(max_length=5, blank=True, null=True)
    company = models.CharField(max_length=500, blank=True)
    department = models.CharField(max_length=500, blank=True)
    position = models.CharField(max_length=500, blank=True)
    mail = models.EmailField(max_length=100, blank=True)
    is_worker = models.BooleanField(verbose_name=u'Статус сотрудника', default=True)
    create_date = models.DateTimeField('Data created', auto_now_add=True)
    update_date = models.DateTimeField('Date updated', auto_now=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return '{self.lastName}_{self.givenName}'.format(
            self=self)  # '{self.lastName}_{self.givenName}'.format(self=self) "%s %s" % (self.lastName, self.givenName)

    def get_full_name(self):
        return '{self.lastName} {self.givenName}'.format(self=self)

    def get_fullest_name(self):
        return '{self.lastName} {self.givenName} {self.patronymicName}'.format(self=self)

    def get_full_name_and_position(self):
        return '{self.lastName} {self.givenName}-{self.position}'.format(self=self)

    def get_full_name_and_position_comma(self):
        return '{self.givenName} {self.lastName}, {self.position}'.format(self=self)


@receiver(populate_user, sender=LDAPBackend)
def ldap_auth_handler(user, ldap_user, **kwargs):
    if user and ldap_user:
        print("Populating user: ", user)
        # logger.info(' | Populating user: {}'.format(user))
        try:
            lan = ldap_user.attrs.get("sn", [])[0]
        except IndexError:
            lan = ""
        try:
            gin = ldap_user.attrs.get("givenName", [])[0]
        except IndexError:
            gin = ""
        try:
            pan = ldap_user.attrs.get("middleName", [])[0]
        except IndexError:
            pan = ""
        try:
            tin = ldap_user.attrs.get("employeeNumber", [])[0]
        except IndexError:
            tin = ""
        try:
            com = ldap_user.attrs.get("company", [])[0]
        except IndexError:
            com = ""
        try:
            dep = ldap_user.attrs.get("department", [])[0]
        except IndexError:
            dep = ""
        try:
            tit = ldap_user.attrs.get("title", [])[0]
        except IndexError:
            tit = ""
        try:
            mail = ldap_user.attrs.get("mail", [])[0]
        except IndexError:
            mail = ""

        if not user.pk:
            # there is a weak point. If user was creted earlier, but not assigned Profile,
            # then "user" objects passes first condition, but in Profile...get can't find Profile
            print("Creating profile")
            user.save()  # saving user explicitly because othewise I can't save profile
            new_profile = Profile.objects.create(
                givenName=gin,
                lastName=lan,
                patronymicName=pan,
                timesheet_number=tin,
                company=com,
                department=dep,
                position=tit,
                mail=mail)
            new_profile.user = user
            boss_users = ['kkozhabay', 'ndastanuly', 'krakhimov', 'azhantore', 'szhelkushinov', 'vvasilev', 'asmolenskiy',
                          'eaqmaganbet', 'tislamov', 'bbaimuratuly', 'smomynov', 'admin1', 'admin2'
                          ]
            new_profile.user.is_active = True if new_profile.user.username in boss_users else False
            new_profile.save()
            print("Successfully")
        else:
            print("Updating profile")
            try:
                profile = Profile.objects.get(user=user)
                profile.givenName = gin
                profile.lastName = lan
                profile.patronymicName = pan
                profile.timesheet_number = tin
                profile.company = com
                profile.department = dep
                profile.position = tit
                profile.mail = mail
                boss_users = ['kkozhabay', 'ndastanuly', 'krakhimov', 'azhantore', 'szhelkushinov', 'vvasilev',
                              'asmolenskiy',
                              'eaqmaganbet', 'tislamov', 'bbaimuratuly', 'smomynov', 'admin1', 'admin2'
                              ]
                profile.user.is_active = True if profile.user.username in boss_users else False
                profile.save()
                print("Successfully")
            except Profile.DoesNotExist:
                print("There is no such a Profile to update for ", user)
                # logger.info(' | There is no such a Profile to update for {}'.format(user))
            except Profile.MultipleObjectsReturned:
                print("Multiple Profiles found for ", user)
                # logger.info(' | Multiple Profiles found for {}'.format(user))
    else:
        print("Something went wrong with User-Profile associsating")
        # logger.info(' | Something went wrong with User-Profile associsating')