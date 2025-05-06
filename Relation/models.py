from django.db import models
from django.core.validators import ValidationError
from User.models import User


class Relation(models.Model):
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    class Meta:
        verbose_name = 'Relation'
        verbose_name_plural = 'Relations'
        db_table = 'Relation'
        unique_together = ('follower', 'following')
    def clean(self):
        if self.following == self.follower:
            raise ValidationError("A user cannot follow themselves.")
# Create your models here.
