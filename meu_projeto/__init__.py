from __future__ import absolute_import, unicode_literals

#Impede que o Django carregue antes do Celery
from .celery import app as celery_app


__all__ = ('celery_app')