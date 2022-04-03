from django.shortcuts import render
import base64
import requests


def identify(request):
    if request.method == 'POST':
        image = request.POST['gardenImage']
        with open(image, "rb") as file:
            images = [base64.b64encode(file.read()).decode("ascii")]

        your_api_key = "RNqSKxLgycdT4nmd6HFZVyRI3KOe9IPkHYcIoWP2YPrO8u9ivZ"
        json_data = {
            "images": images,
            "modifiers": ["similar_images", "health_all"],
            "plant_details": ["common_names", "url", "wiki_description", "taxonomy"]
        }

        response = requests.post(
            "https://api.plant.id/v2/identify",
            json=json_data,
            headers={
                "Content-Type": "application/json",
                "Api-Key": your_api_key
            }).json()
        details = {}
        for suggestion in response["suggestions"]:
            details['name'] = suggestion["plant_name"]
            details['common_name'] = suggestion["plant_details"]["common_names"]
            details['url'] = suggestion["plant_details"]["url"]
        return render(request, 'identifyPlant/identify.html', {'details': details})
    else:
        return render(request, 'identifyPlant/identify.html')
