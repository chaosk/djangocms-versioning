from distutils.version import LooseVersion

import django


DJANGO_GTE_20 = LooseVersion(django.get_version()) >= LooseVersion('2.0')
DJANGO_GTE_21 = LooseVersion(django.get_version()) >= LooseVersion('2.1')
