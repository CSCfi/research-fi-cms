from django.core.management import call_command
from django.http import HttpResponse, HttpResponseServerError
from basicauth.decorators import basic_auth_required

# Management command for making database backup
def make_db_backup():
    call_command('dbbackup', '-z', '-scms')

# Management command for making media backup
def make_media_backup():
    call_command('mediabackup', '-z', '-scms')

# Create database backup
@basic_auth_required
def backup_db(request):
    try:
        make_db_backup()
    except:
        return HttpResponseServerError()
    return HttpResponse(status=200)

# Create media backup
@basic_auth_required
def backup_media(request):
    try:
        make_media_backup()
    except:
        return HttpResponseServerError()
    return HttpResponse(status=200)

# Create database and media backup
@basic_auth_required
def backup_db_and_media(request):
    try:
        make_db_backup()
        make_media_backup()
    except:
        return HttpResponseServerError()
    return HttpResponse(status=200)