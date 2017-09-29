from django.db import models
from django import forms

# Create your models here.
GENDER_CHOICES = (
    ('--None--','--None--'),
    ('Male', 'Male'),
    ('Female', 'Female')
)

Q_CHOICES = (
    ('choice', '--Choose-'),
    ('B.E.', 'B.E.'),
    ('MBA', 'MBA'),
    ('MCA', 'MCA')
)

class Userform(models.Model):
    email = models.EmailField(max_length=70,blank=False, null= False, unique= True)
    name = models.CharField(max_length=100, null=False)
    qualification = models.CharField(max_length=4, choices= Q_CHOICES )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='--None--')
    licen = models.BooleanField(default=False)
    
    
    '''def save(self, *args, **kwargs):
    # ... other things not important here
        self.email = self.email.lower().strip() # Hopefully reduces junk to ""
        if self.email != "": # If it's not blank
            if not email_re.match(self.email): # If it's not an email address
               raise ValidationError(u'%s is not an email address, dummy!' % self.email)
        if self.email == "":
            self.email = None
        super(Userform, self).save(*args, **kwargs)'''
    
