# -*- coding: utf-8 -*-

from survey.models import Question, Category, Survey, Response, AnswerText, AnswerRadio, AnswerSelect, AnswerInteger, AnswerSelectMultiple
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from actions import export_as_excel
from models import *
from .models import AnswerBase

class QuestionInline(admin.TabularInline):
	model = Question
	ordering = ('category',)
	extra = 0

class CategoryInline(admin.TabularInline):
	model = Category
	extra = 0

class SurveyAdmin(admin.ModelAdmin):
	inlines = [CategoryInline, QuestionInline]
	actions = (export_as_excel, )

class AnswerBaseInline(admin.StackedInline):
	fields = ('question', 'body')
	readonly_fields = ('question',)
	extra = 0

class AnswerTextInline(AnswerBaseInline):
	model= AnswerText  

class AnswerRadioInline(AnswerBaseInline):
	model= AnswerRadio 

class AnswerSelectInline(AnswerBaseInline):
	model= AnswerSelect 

class AnswerSelectMultipleInline(AnswerBaseInline):
	model= AnswerSelectMultiple

class AnswerIntegerInline(AnswerBaseInline):
	model= AnswerInteger 

class ResponseAdmin(admin.ModelAdmin):
	list_display = ('interviewer', 'survey', 'respuesta') 
	inlines = [AnswerTextInline, AnswerRadioInline, AnswerSelectInline, AnswerSelectMultipleInline, AnswerIntegerInline]	
	readonly_fields = ('survey', 'created', 'updated', 'interview_uuid','respuesta')
	list_filter = ('survey', 'interviewer',)
	actions = (export_as_excel, )






#admin.site.register(Question, QuestionInline)
#admin.site.register(Category, CategoryInline)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Response, ResponseAdmin)

