from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "Favorite Quote",
                "message": "Jeremiah 29:11 "}
        return data
    
class AboutPageView (TemplateView):
    template_name = "resume.html"
    def get_context_data(self):
        data = {"message_title" : "Education",
                "message1": "Senior High School: Camarines Sur National High school",
                "message": "Elementary: Julian B. Meliton"}
        return data

class ContactInfoPageView (TemplateView):
    template_name = "contactInfo.html"
    def get_context_data(self):
        data = {"message_title" : "Sean Daniel Estor",
                "message1": "Zone 2b Happy Homes Urban Jimenez",
                "message2": "Email: sean_daniel123@yahoo.com",               
                "message3": "Mobile No. 09075039909"}
        return data

