import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape information from Linkedin profiles
    Manually scrape the information from the Linkedin profile"""
    api_endpoint= linkedin_profile_url
   # header_dic = {"Authorization": f'Bearer {os.environ.get("API_KEY_FOR_ENDPOINT")}'}

  
    response= requests.get(api_endpoint)

    data =response.json()

    data = {
        k: v

        for k, v in data.items()

        if v not in ([]," "," ", None)

            and k not in ["people_also_viewed", "certifications"]     
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data