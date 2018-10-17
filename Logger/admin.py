from django.contrib import admin
from Logger.models import Record, Trace, Run, Process

# Register your models here.
class RunAdmin(admin.ModelAdmin):
    fields = ['runId','runStatus','startedDatetime','errorDatetime','completedDatetime','process']
    list_display = ['runId','runStatus','startedDatetime','errorDatetime','completedDatetime']
class ProcessAdmin(admin.ModelAdmin):
    fields = ['uid','name','status','process','native_id','exitcode','attempt','workdir',
            'container','queue','cpus','memory','disk','time','env','error_action',
            'submittedDatetime','startedDatetime','completedDatetime','duration','script']
    list_display = ['uid','runStatus','submittedDatetime','startedDatetime','completedDatetime','status']

admin.site.register(Run,RunAdmin)
admin.site.register(Process,ProcessAdmin)
