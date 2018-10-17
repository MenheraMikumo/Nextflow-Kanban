from Logger.models import Run, Process
import json

# Create your views here.
def log_dealer(request):

    received_log = json.loads(request.body.decode())
    if request.method == 'POST':
        if received_log.get('trace',False):
            uid = received_log['runId'] + '/' + received_log['trace']['hash'] 
            proc = Process.objects.get_or_create(uid=uid)[0]
            proc.runId = received_log['runId']
            proc.runStatus = received_log['runStatus']
            if received_log['runStatus'] == 'process_submitted':
                proc.submittedDatetime = received_log['utcTime']
            elif received_log['runStatus'] == 'process_started':
                proc.startedDatetime = received_log['utcTime']
            elif received_log['runStatus'] == 'process_completed':
                proc.completedDatetime = received_log['utcTime']
            proc.hashtag = received_log['trace']['hash']
            proc.status = received_log['trace']['status']
            proc.name = received_log['trace']['name']
            proc.exitcode = received_log['trace']['exit']
            proc.process = received_log['trace']['process']
            proc.container = received_log['trace'].get('container',None)
            proc.attempt = received_log['trace'].get('attempt',None)
            proc.script = received_log['trace'].get('script',None)
            proc.workdir = received_log['trace']['workdir']
            proc.queue = received_log['trace'].get('queue',None)
            proc.cpus = received_log['trace'].get('cpus',None)
            proc.memory = received_log['trace'].get('memory',None)
            proc.disk = received_log['trace'].get('disk',None)
            proc.time = received_log['trace'].get('time',None)
            proc.env = received_log['trace'].get('env',None)
            proc.error_action = received_log['trace'].get('error_action',None)
            proc.native_id = received_log['trace'].get('native_id',None)
            proc.duration = received_log['trace'].get('duration',None)
            proc.save()
            run = Run.objects.get_or_create(runId=received_log['runId'])[0]
            run.process.add(proc)
            run.save()

        else:
            run = Run.objects.get_or_create(runId=received_log['runId'])[0]
            run.runName = received_log['runName']
            if received_log['runStatus'] == 'started':
                run.startedDatetime = received_log['utcTime']
                run.runStatus = received_log['runStatus']
            elif received_log['runStatus'] == 'error':
                run.errorDatetime = received_log['utcTime']
                run.runStatus = received_log['runStatus']
            elif received_log['runStatus'] == 'completed':
                run.completedDatetime = received_log['utcTime']
                if run.errorDatetime:
                    run.runStatus = 'failed'
                else:
                    run.runStatus = 'success'
            run.save()

    return 0 
