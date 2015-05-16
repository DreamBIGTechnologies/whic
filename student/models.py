from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    
   """User profile model. This profile can be retrieved by calling
    get_profile() on the User model"""

CAMPUS_CHOICES = (
		
		('SIUC', 'Southern Illinois University - Carbondale'),
		('UofC', 'University of Chicago'),
	
)

ETHNICITY_CHOICES = (
		
		('AA', 'African American'),
		('WH',  'Caucasian American'),
		('AS', 'Asain American'),
		('NA', 'Native American'),
		('LA', 'Latino American'),
		('OT', 'Not Specified/Other'),
		
)
	
YEAR_IN_SCHOOL = (
		
		('FR', 'Freshman'),
		('SO', 'Sophomore'),
		('JR', 'Junior'),
		('SR', 'Senior'),
		('GRAD', 'Graduate Student'),
	
)

user = models.OneToOneField(User)
major = models.CharField(max_length=100)
minor = models.CharField(max_length=100)

	
is_greek = models.BooleanField()
is_usg = models.BooleanField()
is_athlete = models.BooleanField()
	
campus = models.CharField(max_length=1, choices=CAMPUS_CHOICES)
ethnicity = models.CharField(max_length=1, choices=ETHNICITY_CHOICES)
year = models.CharField(max_length=1, choices=YEAR_IN_SCHOOL)
	
def __str__(self):
	return self.account.username