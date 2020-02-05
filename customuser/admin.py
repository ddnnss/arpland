from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


#@admin.register(User)
# class UserAdmin(DjangoUserAdmin):
#     """Define admin model for custom User model with no email field."""
#
#     fieldsets = (
#         (None, {'fields': ('email', 'password',)}),
#         (_('Personal info'), {'fields': ('name', 'phone','organization_name',
#                                          'organization_site','organization_address','organization_description',
#                                          'organization_avatar',)}),
#
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'phone',),
#         }),
#     )
#     list_display = ('email', 'name',  'phone')
#
#     ordering = ('email',)
#     search_fields = ('email', 'name', 'phone','organization_name ')

admin.site.register(User)
# order_number
#     email
#     name
#     phone
#     avatar
#     organization_name
#     organization_site
#     organization_address
#     organization_description
#     organization_avatar
#     organization_vk
#     organization_fb
#     organization_inst
#     organization_yt
#     organization_ok
