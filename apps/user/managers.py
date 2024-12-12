from django.contrib.auth.models import UserManager

import re


class CustomUserManager(UserManager):
    def create_user(self, email, phone_number, first_name, last_name, description=None, note=None, image=None, video=None, gender=None, adress=None, birthday=None, password=None, **extra_fields):
        if not email:
            raise ValueError("You must enter an email address to create a user!")
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError("The email address you entered is in an invalid format! Please re-enter: For example: turdalihasanboyev70@gmail.com")
        if not phone_number:
            raise ValueError("You must enter an phone number to create a user!")
        if not re.match(r'^\+?[0-9]{10,15}$', phone_number):
            raise ValueError("The phone number entered is in the wrong format! Please re-enter: For example: +998901234567")
        if not first_name:
            raise ValueError("You must enter an first name to create a user!")
        if not last_name:
            raise ValueError("You must enter an last name to create a user!")
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, description=description, note=note, image=image, video=video, gender=gender, adress=adress, birthday=birthday, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone_number, first_name, last_name, description=None, note=None, image=None, video=None, gender=None, adress=None, birthday=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("For superuser, is_staff=True is required!")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("For superuser, is_superuser=True is required!")
        
        if not email:
            raise ValueError("To create a Super User, an email address is required!")
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError("The email address you entered is in an invalid format! Please re-enter: For example: turdalihasanboyev70@gmail.com")
        if not phone_number:
            raise ValueError("To create a Super User, an phone number is required!")
        if not re.match(r'^\+?[0-9]{10,15}$', phone_number):
            raise ValueError("The phone number entered is in the wrong format! Please re-enter: For example: +998901234567")
        if not first_name:
            raise ValueError("To create a Super User, an first name is required!")
        if not last_name:
            raise ValueError("To create a Super User, an last name is required!")
        
        user = self.create_user(email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, description=description, note=note, image=image, video=video, gender=gender, adress=adress, birthday=birthday, password=password, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user
