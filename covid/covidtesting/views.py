from django.shortcuts import render, redirect
from .models import CovidDetails

# Create your views here.
def home_page(request):
    return render(request, "home.html", {})

def details_page(request):
    return render(request, "details_page.html", {})

def about(request):
    return render(request, "about.html", {})

def validate_details(request):
    # Write code
    if request.method == "POST":
        true_count = 0
        covid_details = CovidDetails()

        covid_details.breathing_problem = request.POST.get("breathing_problem")
        if covid_details.breathing_problem == "True":
            true_count += 1

        covid_details.fever = request.POST.get("fever")
        if covid_details.fever == "True":
            true_count += 1

        covid_details.dry_cough = request.POST.get("dry_cough")
        if covid_details.dry_cough == "True":
            true_count += 1
        
        covid_details.sore_throat = request.POST.get("sore_throat")
        if covid_details.sore_throat == "True":
            true_count += 1      
          
        covid_details.running_nose = request.POST.get("running_nose")
        if covid_details.running_nose == "True":
            true_count += 1
        
        covid_details.asthma = request.POST.get("asthma")
        if covid_details.asthma == "True":
            true_count += 1
        
        covid_details.chronic_lung_disease = request.POST.get("chronic_lung_disease")
        if covid_details.chronic_lung_disease == "True":
            true_count += 1
        
        covid_details.headache = request.POST.get("headache")
        if covid_details.headache == "True":
            true_count += 1
        
        covid_details.heart_disease = request.POST.get("heart_disease")
        if covid_details.heart_disease == "True":
            true_count += 1
        
        covid_details.diabetes = request.POST.get("diabetes")
        if covid_details.diabetes == "True":
            true_count += 1
        
        covid_details.hyper_tension = request.POST.get("hyper_tension")
        if covid_details.hyper_tension == "True":
            true_count += 1
        
        covid_details.fatigue = request.POST.get("fatigue")
        if covid_details.fatigue == "True":
            true_count += 1
        
        covid_details.gastrointestinal = request.POST.get("gastrointestinal")
        if covid_details.gastrointestinal == "True":
            true_count += 1
        
        covid_details.abroad_travel = request.POST.get("abroad_travel")
        if covid_details.abroad_travel == "True":
            true_count += 1
        
        covid_details.contact_with_covid_patient = request.POST.get("contact_with_covid_patient")
        if covid_details.contact_with_covid_patient == "True":
            true_count += 1
        
        covid_details.attended_large_gathering = request.POST.get("attended_large_gathering")
        if covid_details.attended_large_gathering == "True":
            true_count += 1
        
        covid_details.visited_public_exposed_places = request.POST.get("visited_public_exposed_places")
        if covid_details.visited_public_exposed_places == "True":
            true_count += 1
        
        covid_details.family_working_in_public_exposed_places = request.POST.get("family_working_in_public_exposed_places")
        if covid_details.family_working_in_public_exposed_places == "True":
            true_count += 1
        
        covid_details.wearing_masks = request.POST.get("wearing_masks")
        if covid_details.wearing_masks == False:
            true_count += 1
        
        covid_details.sanitization_from_market = request.POST.get("sanitization_from_market")
        if covid_details.sanitization_from_market == "True":
            true_count += 1

        if true_count > 11:
            covid_details.covid_19 = True 
            # covid_details.covid_19 = False
        else:
            covid_details.covid_19 = False

        covid_details.save()

        return render(request, "results_page.html", {"result": covid_details.covid_19})
    else:
        return redirect("/covid/home")
    
def graph(request):

    covid_patients_count = CovidDetails.objects.filter(covid_19 = True)
    non_covid_patients_count = CovidDetails.objects.filter(covid_19 = False)
    return render(request, "graph.html", { "covid_patients_count": covid_patients_count,
                                           "non_covid_patients_count": non_covid_patients_count})