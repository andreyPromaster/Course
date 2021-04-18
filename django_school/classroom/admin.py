from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from classroom.forms import CustomUserCreationForm, CustomUserChangeForm
from classroom.models import Quiz, Question, Answer, Student, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active', 'is_student', 'is_teacher')
    list_filter = ('email', 'is_staff', 'is_active', 'is_student', 'is_teacher')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_teacher')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_teacher')}
        ),
    )
    search_fields = ('username','email',)
    ordering = ('username','email',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'subject')
    list_filter = ('subject', 'owner')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'text')
    search_fields = ('text',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')



