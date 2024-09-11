from django.contrib import admin
from .models import ( Department,
                    Group, Semestre,
                    ProfDispoWeek,
                    Course, Classroom,
                    Seance, HourRange,
                    )

# Register your models here.



@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    pass



@admin.register(ProfDispoWeek)
class ProfDispoWeekAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    pass

@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    pass

@admin.register(HourRange)
class HourRangeAdmin(admin.ModelAdmin):
    pass
