from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=255, null=True)
    quiz = models.JSONField()

class User(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.username


class Category(models.Model):
    soal_choices = [
        ('si', 'siasi'),
        ('va', 'varzeshi'),
        ('el', 'elmi'),
        ('eg', 'eghtesadi'),
        ('fa', 'farhangi')
    ]
    title=models.CharField(null=True,max_length=2,choices=soal_choices)

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=255, null=True)
    category=models.ForeignKey(Category,related_name="q_to_c",on_delete=models.CASCADE)
    description = models.TextField()
    answer_choices=[
        ('A', 'Gozine A'),
        ('B', 'Gozine B'),
        ('C', 'Gozine C'),
        ('D', 'Gozine D')
    ]
    select=models.CharField(max_length=1,choices=answer_choices)
    
    

    def __str__(self) -> str:
        return self.title


class History(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quiz=models.JSONField(null=True)
    score=models.IntegerField(default=0,null=True)

    def __str__(self) -> str:
        return self.user.username
