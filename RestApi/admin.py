from django.contrib import admin
from RestApi.models import Choices,Question,Answers,Attempts
# Register your models here.
class ChoicesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class AnswersAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class AttemptsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Choices,ChoicesAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answers,AnswersAdmin)
admin.site.register(Attempts,AttemptsAdmin)