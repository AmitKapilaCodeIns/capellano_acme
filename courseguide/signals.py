from django.contrib.auth.models import Group, Permission
from courseguide.models import HoleGuide

# Create groups
editors_group, created = Group.objects.get_or_create(name='Editors')
readers_group, created = Group.objects.get_or_create(name='Readers')

# Assign permissions to groups
add_perm = Permission.objects.get(codename='add_holeguide')
change_perm = Permission.objects.get(codename='change_holeguide')
editors_group.permissions.add(add_perm, change_perm)

# Readers get no special permissions (they can only view))