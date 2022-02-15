from django.contrib import admin
from .models import TermsAndConditions,Contact,Testimonial,TeamMember,Gallery,FrequentlyQuestion,Service

# Register your models here.
@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','subject','message',)
    list_filter = ('name','email','phone','subject','message',)
    search_fields = ('name','email','phone','subject','message',)
    ordering = ('-create_at',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name','designation','content',)
    list_filter = ('name','designation')
    search_fields = ('name','designation','content',)
    ordering = ('-create_at',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    '''Admin View for TeamMember'''
    list_display = ('name','designation','about',)
    ordering = ('-create_at',)

    @admin.register(Gallery)
    class GalleryAdmin(admin.ModelAdmin):
        '''Admin View for Gallery'''   
        list_display = ('gallery_image',)
        ordering = ('-create_at',)

@admin.register(FrequentlyQuestion)
class FrequentlyQuestionAdmin(admin.ModelAdmin):
    '''Admin View for FrequentlyQuestion'''

    list_display = ('question','answer',)    
    ordering = ('-create_at',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    '''Admin View for Service'''

    list_display = ('icon_class_name','service_name','about_service',)
    ordering = ('-create_at',)