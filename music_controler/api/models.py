from django.db import models
import string
import random

# Create your models here.


def generate_unqiue_code():
    codeLength = 6

    while True:
        rmcode = ''.join(random.choices(string.ascii_uppercase, k=codeLength))
        if Room.objects.filter(code=rmcode).count() == 0:
            break
    
    return rmcode

class Room(models.Model):
    code = models.CharField(max_length=8, default=generate_unqiue_code, unique =True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    vote_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)