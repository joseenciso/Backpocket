from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    # sender or the sinal | instance or the module and | bool sent by django=instance or update | kw argument
    """ Update order total on lineitem update/create """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    # sender or the sinal | instance or the module and | bool sent by django=instance or update | kw argument
    """ Updata order total on lineitem delete """
    print('Delete Signal')
    instance.order.update_total()
