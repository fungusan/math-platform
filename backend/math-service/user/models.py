from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key = True,    
                               default = uuid.uuid4, 
                               editable = False)
    user_name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 128) # Store the hashed password