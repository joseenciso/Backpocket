from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

#from .modeles import OrderLineItem


#@receiver(post_save, sender=OorderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    # sender or the sinal | instance or the module and | bool sent by django=instance or update | kw argument
    """ Updata order total on lineitem update/create """
