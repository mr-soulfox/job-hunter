from linkedin_api import Linkedin
from os import environ
from os import path


def get_user_info(link: str):
    clean_link: str = (link.split("?")[0]).split("/in/")[1]
    logged_api: Linkedin = Linkedin(environ.get("LINKEDIN_EMAIL"), environ.get("LINKEDIN_PASSWORD"))
    profile: dict = logged_api.get_profile(clean_link)
    contact: dict = logged_api.get_profile_contact_info(clean_link)
