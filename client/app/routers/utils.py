from fastapi.templating import Jinja2Templates


service_api_url = 'http://localhost:8000'

templates = Jinja2Templates(directory="client/app/templates")