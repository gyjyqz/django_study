import  jwt
from articles.models import User
def token_auth(token):
    payload = jwt.decode(token,"SECRET_KEY",algorithm="HS256")
    email=payload.get("email")
    user = User.objects.filter(email=email)
    if  not user:
        return  False
    return  True