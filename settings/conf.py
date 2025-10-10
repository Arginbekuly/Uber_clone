#Project modules
import os
from dotenv import load_dotenv
# from decouple import config


load_dotenv()

"""------------------ SECRET KEY ---------------------"""

SECRET_KEY = 'django-insecure-og)%0kkj75-#uk8+g5r+cy+&&&0gh8(rcw5z7%o4v2l+7f=g89'


"""-------------------- ENV SETTINGS ----------------------"""
ENV_POSSIBLE_OPTIONS = [
    "local",
    "prod",
]

ENV_ID = os.getenv("UBERCLONE_ENV_ID", "local")