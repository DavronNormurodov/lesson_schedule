from django.db.models.signals import post_save, pre_save, pre_init
from django.dispatch import receiver

from references.models import Room


@receiver(pre_save, sender=Room)
def update_room(sender, instance, *args, **kwargs):
    print('pre save working')
    print(sender)
    print(instance)


@receiver(post_save, sender=Room)
def update_room(sender, instance, created, **kwargs):
    print('post save working')
    print(sender)
    print(instance)
    print(created)
    print(instance._state.adding, instance._state.db)
    if created:
        print(instance.title)
        # instance.title = 'new obj created'
        # instance.save()


# post_save.connect(update_room, sender=Room)


@receiver(pre_init, sender=Room)
def update_room(sender, *args, **kwargs):
    print('pre_init working')
    print(sender)
    print(args, kwargs)

