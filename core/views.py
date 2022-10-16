from django.http import HttpResponse

def home(request):
   text = """<h1>Hi Manohar you done sucessfully deployed AWS beanstalk with S3 bucket using Github Actons!. :)</h1>"""
   return HttpResponse(text)
