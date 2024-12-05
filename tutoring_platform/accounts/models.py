from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings

# User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('learner', 'Learner'),
        ('tutor', 'Tutor'),
        ('admin', 'Admin'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='learner')
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Fields required for superuser creation

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Subject Model
class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Tutor Profile Model
class TutorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tutor_profile"
    )
    bio = models.TextField(blank=True, null=True)
    expertise = models.CharField(max_length=255)
    availability = models.TextField()
    rating = models.FloatField(default=0.0)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/tutors/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tutor: {self.user.email}"


# Learner Profile Model
class LearnerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="learner_profile"
    )
    bio = models.TextField(blank=True, null=True)
    goals = models.TextField(blank=True, null=True)
    preferred_subjects = models.ManyToManyField(Subject, related_name="learners")
    learning_pace = models.CharField(
        max_length=20,
        choices=[
            ('fast', 'Fast'),
            ('moderate', 'Moderate'),
            ('slow', 'Slow')
        ],
        default='moderate'
    )
    profile_picture = models.ImageField(
        upload_to="profile_pictures/learners/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Learner: {self.user.email}"
