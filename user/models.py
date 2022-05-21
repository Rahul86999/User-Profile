from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager

class UserProfile(AbstractBaseUser, PermissionsMixin):
	profile_image = models.ImageField(null=True, blank=True, upload_to="profile/")
	name = models.CharField(_('Name'), max_length=100)
	username = models.CharField(_('Username'), max_length=100,unique=True)
	email = models.EmailField(_('Email'), unique=True)
	phone_no = models.CharField(max_length=15)
	comments = models.CharField(_('Comments '), max_length=500,blank=True,null=True)
	is_active = models.BooleanField(_('active'), default=True)
	is_staff = models.BooleanField(_('staff'), default=False)
	is_superuser = models.BooleanField(_('superuser'), default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
	    verbose_name = _('user')
	    verbose_name_plural = _('users')
	
	def get_profile_image(self):
		if self.profile_image:
			return profile_image
		else:
			return None