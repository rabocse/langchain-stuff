import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape information from Linkedin profiles
    Manually scrape the information from the Linkedin profile"""
    api_endpoint= linkedin_profile_url
    header_dic = {"Authorization": f'Bearer {os.environ.get("API_KEY_FOR_ENDPOINT")}'}

  
    response= requests.get(api_endpoint)

    return response