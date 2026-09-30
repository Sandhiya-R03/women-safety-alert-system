from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def health(request): return JsonResponse({'status':'ok','database':'not configured','project':'SheShield API'})
def dashboard(request): return JsonResponse({'active_safeguards':3,'trusted_contacts':4,'verified_resources':8,'privacy_first':True})
def resources(request):
 return JsonResponse({'resources':[
 {'name':'Women Police Station','type':'Police','distance':'1.2 km','phone':'112'},
 {'name':'City Emergency Hospital','type':'Hospital','distance':'2.1 km','phone':'108'},
 {'name':'SafeRide Pickup Point','type':'Safe Zone','distance':'0.8 km','phone':''},
 {'name':'Community Support Centre','type':'Support','distance':'3.4 km','phone':'181'}]})
def internships(request):
 return JsonResponse({'opportunities':[
 {'title':'Women Safety Tech Intern','organisation':'SafeTech Labs','mode':'Hybrid','skills':['React','Django','APIs']},
 {'title':'Community Safety Research Intern','organisation':'Nirbhaya Foundation','mode':'On-site','skills':['Research','Communication']},
 {'title':'UI/UX Design Intern','organisation':'CareConnect','mode':'Remote','skills':['Figma','UX Research']},
 {'title':'Cyber Safety Intern','organisation':'SecureHer Initiative','mode':'Hybrid','skills':['Cybersecurity','Awareness']}]})
def emergency_contacts(request):
 return JsonResponse({'contacts':[
 {'name':'Amma / Guardian','phone':'+91 90000 00001'},
 {'name':'Best Friend','phone':'+91 90000 00002'},
 {'name':'College Security','phone':'+91 90000 00003'},
 {'name':'Hostel Warden','phone':'+91 90000 00004'}]})
@csrf_exempt
def create_alert(request):
 if request.method!='POST': return JsonResponse({'message':'POST an alert payload to simulate SOS.'},status=405)
 try: payload=json.loads(request.body or '{}')
 except json.JSONDecodeError: payload={}
 return JsonResponse({'status':'simulated','message':'SOS workflow accepted. No real notification was sent.','payload':payload},status=201)
