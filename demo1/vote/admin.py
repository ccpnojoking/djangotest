from django.contrib import admin

# Register your models here.

from .models import Questions,Answers

class AnswersAdmin(admin.ModelAdmin):
    list_display = ["id","Acontent","Acount","Aquestion",]
    list_filter = ["acount","aquestion"]
    list_per_page = 3
    search_fields = ["id","acontent","acount","aquestion",]



class AnswersInlines(admin.StackedInline):
    model = Answers
    extra = 2

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["id","Qcontent","Qpub_date",]
    search_fields = ["id","qcontent"]
    list_per_page = 3
    inlines = [AnswersInlines,]




admin.site.register(Questions,QuestionsAdmin)
admin.site.register(Answers,AnswersAdmin)