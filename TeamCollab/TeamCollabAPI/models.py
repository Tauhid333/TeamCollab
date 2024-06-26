from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    email            = models.EmailField(unique=True)
    first_name       = models.CharField(max_length=30)
    last_name        = models.CharField(max_length=30)
    date_joined      = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table            = "Users"

    def __str__(self):
        return self.first_name + self.last_name
    
class Project(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.TextField()
    owner           = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table            = "Projects"

    def __str__(self):
        return self.name

class ProjectMember(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    ]
    project             = models.ForeignKey(Project, related_name='members', on_delete=models.CASCADE)
    user                = models.ForeignKey(User, related_name='project_memberships', on_delete=models.CASCADE)
    role                = models.CharField(max_length=10, choices=ROLE_CHOICES)

    class Meta:
        db_table            = "Project Members"

    def __str__(self):
        return f"{self.user.username} - {self.project.name}"

class Task(models.Model):
    STATUS = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]
    PRIORITY = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    title                     = models.CharField(max_length=100)
    description               = models.TextField()
    status                    = models.CharField(max_length=20, choices=STATUS)
    priority                  = models.CharField(max_length=20, choices=PRIORITY)
    assigned_to               = models.ForeignKey(User, related_name='tasks', on_delete=models.SET_NULL, null=True, blank=True)
    project                   = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    created_at                = models.DateTimeField(auto_now_add=True)
    due_date                  = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    content                  = models.CharField(max_length=100)
    user                     = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    task                     = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    created_at               = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table             = 'Comments'
        



