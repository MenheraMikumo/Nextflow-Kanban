from django.db import models

# Create your models here.
class Trace(models.Model):
    task_id = models.IntegerField()
    status = models.CharField(max_length=128)
    hash = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    exit = models.IntegerField()
    submit = models.IntegerField()
    start = models.IntegerField()
    process = models.CharField(max_length=128)
    tag = models.CharField(max_length=128, blank=True, null=True)
    module = models.CharField(max_length=128, blank=True, null=True)
    container = models.CharField(max_length=128, blank=True, null=True)
    attempt = models.CharField(max_length=128)
    script = models.CharField(max_length=128)
    scratch = models.CharField(max_length=128, blank=True, null=True)
    workdir = models.CharField(max_length=128)
    queue = models.CharField(max_length=128, blank=True, null=True)
    cpus = models.CharField(max_length=128, blank=True, null=True)
    memory = models.CharField(max_length=128, blank=True, null=True)
    disk = models.CharField(max_length=128, blank=True, null=True)
    time = models.CharField(max_length=128, blank=True, null=True)
    env = models.CharField(max_length=128, blank=True, null=True)
    native_id = models.IntegerField(blank=True, null=True)
    error_action = models.CharField(max_length=128, blank=True, null=True)
    complete = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    realtime = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Record(models.Model):
    runName = models.CharField(max_length=128)
    runId = models.CharField(max_length=128)
    runStatus = models.CharField(max_length=128)
    utcTime = models.DateTimeField(blank=True, null=True)
    trace = models.ForeignKey(Trace, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.runName


class Process(models.Model):
    uid = models.CharField(max_length=128, primary_key=True)
    runId = models.CharField(max_length=128)
    runStatus = models.CharField(max_length=128)
    startedDatetime = models.DateTimeField(blank=True, null=True)
    submittedDatetime = models.DateTimeField(blank=True, null=True)
    completedDatetime = models.DateTimeField(blank=True, null=True)   
    hashtag = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    exitcode = models.IntegerField(blank=True, null=True)
    process = models.CharField(max_length=128, blank=True, null=True)
    container = models.CharField(max_length=128, blank=True, null=True)
    attempt = models.IntegerField(blank=True, null=True)
    script = models.TextField(max_length=1024, blank=True, null=True)
    workdir = models.CharField(max_length=128, blank=True, null=True)
    queue = models.CharField(max_length=128, blank=True, null=True)
    cpus = models.IntegerField(blank=True, null=True)
    memory = models.CharField(max_length=16, blank=True, null=True)
    disk = models.CharField(max_length=16, blank=True, null=True)
    time = models.CharField(max_length=128, blank=True, null=True)
    env = models.CharField(max_length=128, blank=True, null=True)
    error_action = models.CharField(max_length=128, blank=True, null=True)
    native_id = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.uid

class Run(models.Model):
    runName = models.CharField(max_length=128, blank=True, null=True)
    runId = models.CharField(max_length=128, primary_key=True)
    runStatus = models.CharField(max_length=128, blank=True, null=True)
    startedDatetime = models.DateTimeField(blank=True, null=True)
    errorDatetime = models.DateTimeField(blank=True, null=True)
    completedDatetime = models.DateTimeField(blank=True, null=True)   
    process = models.ManyToManyField(Process, blank=True)

    def __str__(self):
        return self.runId
