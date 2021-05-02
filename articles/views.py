from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
from articles.models import Articles,User
import  json
from django.db.models import Q
from django.forms.models import model_to_dict
import jwt
from article.token_auth import token_auth

# Create your views here.
def  get_html(request):
    return  render(request,'test.html')
def get_content(request):
    return  HttpResponse("奥里给")
def create_artcle(data):
    try:
        data = json.loads(data)
    except Exception as ex:
        print(str(ex))
    article =  Articles.objects.create(
        **data
    )
    return article.id

def get_or_create_articles(request):
    try:
        if request.method == 'POST':
            article_id=create_artcle(request.body)
            return  JsonResponse({
                "code":200,
                "message":"success",
                "data":{
                    "id":article_id
                }
            })
        else:
            #articles=Articles.objects.all()

            offest = request.GET.get('offest', 0)
            limit = request.GET.get("limit", 10)
            q = request.GET.get("q")
            title = request.GET.get("title")
            sub_title = request.GET.get("subTitle")
            content = request.GET.get("content")
            description = request.GET.get("description")
            articles = Articles.objects.filter(Q(title__icontains=(title)) | Q(sub_title__icontains=str(sub_title)) |
                                Q(description__icontains=str(description)) | Q(key_words__icontains=str(q)) | Q(content__icontains=str(content)))
            #articles_item = list(map(lambda  article:{"title":article.title},articles))
            json_list=[ model_to_dict(article) for article in articles ]

            data={
                "code": 200,
                "message": "success",
                "data": {
                    "list":json_list,
                    "pagination":{
                        "offest":offest,
                        "limit":limit,
                        "totalCount":100
                    },
                }
            }
            return  JsonResponse(data)
    except Exception as ex:
        print(str(ex))

def get_article_or_update_or_delete(request,id):
    if request.method == 'GET':
        #id = request.GET.get("id")
        article = Articles.objects.get(id=id)
        data = {
            "code": 200,
            "message": "success",
            "data": model_to_dict(article),
        }
        return JsonResponse(data)

    if request.method == 'PUT':
        Articles.objects.filter(id=id).update(**(json.loads(request.body)))
        articles = Articles.objects.get(id=id)
        data = {
            "code": 200,
            "message": "success",
            "data": model_to_dict(Articles.objects.get(id=id)),
        }
        return JsonResponse(data)

    if request.method == 'DELETE':
        try:
            Articles.objects.filter(id=id).delete()
            return JsonResponse({
                "code": 200,
                "message": "success",
                "data": ''
            })
        except Exception as ex:
            print(str(ex))




def register(request):
    data = json.loads(request.body)

    User.objects.create(**data)

    return JsonResponse({"code":200})



def login(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')
    user = User.objects.filter(email=email,password=password)
    if not user:
        return  JsonResponse({"code":400})

    # response = JsonResponse({"code":200})
    # print(request)
    # response.set_cookie("key","123")
    #
    # request.session['key']="4577"

    payload = {
        "email": email
    }

    token = jwt.encode(payload, "SECRET_KEY", algorithm="HS256").decode('utf-8')



    return JsonResponse({
        "code":200,
        "authToken":token
    })



from rest_framework.views import  APIView
from rest_framework.response import Response
from article.token_auth import TokenAuth
from articles.serializers import ArtilceSerializer
class ArticlesView(APIView):
    authentication_classes = (TokenAuth,)
    # authentication_classes = ()
    def get(self,request):

        atricles = Articles.objects.all()
        # params = {
        #     "title":request.GET.get("title"),
        #     "email":request.GET.get("email"),
        #     "offest":request.GET.get("offest"),
        # }
        # articleserializers = ArtilceSerializer(data=params)
        #
        # if  articleserializers.is_valid():   #articleserializers.errors解析并返回
        #     return Response({
        #         "code":200,
        #         "errors":articleserializers.errors
        #     })
        # {'email': [ErrorDetail(string='Enter a valid email address.', code='invalid')],
        #  'offest': [ErrorDetail(string='A valid integer is required.', code='invalid')]}

        return Response({
            "code":200,
            "data":[],

        })
    def post(self,request):
        return Response({
            "code": 200,
            "data": [],

        })



































'''
{    "title": "12345",
        "sub_title": "123789",
        "key_words": "奥里给奥里给奥里给yeyeyyeyeye111100000",
        "description": "这是一个文章",
        "article_type": 1,
        "is_hot": true,
        "is_published": true,
        "image": "http://dummyimage.com/200x100/02adea&text=this is frontpage",
        "image_title": "玛卡巴卡",
        "content": "这是所有文章的其中一个文章"
    }
'''