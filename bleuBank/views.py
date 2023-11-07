from django.shortcuts import render
from django.core.files.storage import default_storage
from django.http import JsonResponse
from bleu_api.client import *
# Create your views here.
def landing(request):
    context = {
    }
    return render(request, 'bleuBank/landing.html', context)

def single_kyc_verification(request):

    client = BleuAPIClient(client_id="4mfq2291m54gtg4t50gh83bcaa", client_secret="5uo8j2pq1dfmsmirkoim6rmse3og78ee0el86eltd6oh96fi3ao")
    front_side_path = default_storage.save('media/front_side.jpg', request.FILES['front_side'])
    back_side_path = default_storage.save('media/back_side.jpg', request.FILES['back_side'])
    selfie_image_path = default_storage.save('media/selfie_image.jpg', request.FILES['selfie_image'])

    verification = client.single_kyc_verification(selfie_image_path, front_side_path, back_side_path)
    if client.RESPONSE_CODES[verification['responseCode']] != 'SUCCESS':
        data = {'error': client.RESPONSE_CODES[verification['responseCode']].replace("_", " ").title()}
    else:
        data = {'success': client.RESPONSE_CODES[verification['responseCode']].replace("_", " ").title()}
    return JsonResponse(data)