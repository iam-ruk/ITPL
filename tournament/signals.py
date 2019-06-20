from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Match,MatchDescription


@receiver(post_save, sender=Match)
def create_matchdescription(sender, instance, created, **kwargs):
    if created:
        x=MatchDescription.objects.create(match=instance)
        x.save()
