from django.contrib import admin
from .models import Question, User, Category, History, Quiz

admin.site.register(Question)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(History)
admin.site.register(Quiz)