from django.contrib import admin
from .models import Header, Education, Skill, Experience, Project, Contact


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    pass  # By default, all fields will be available in admin interface


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
