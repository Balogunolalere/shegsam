from fastapi import FastAPI, File, UploadFile, status, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse,HTMLResponse
from pydantic import EmailStr
from deta import Deta
from typing import Optional
from mailjet_rest import Client
import os 
import cloudinary 
from cloudinary import uploader

app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

deta = Deta(deta_key)
sub_db = deta.Base('shegsam_subscribers')

cloudinary.config(
  cloud_name = 'noiro',  
  api_key = api_key,  
  api_secret = api_secret  
)
car = deta.Base("car_db")


@app.get('/', response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/cars', response_class=HTMLResponse)
def index(request:Request):
    data = next(car.fetch())
    return templates.TemplateResponse('car.html', {'request': request, 'data':data})

@app.get('/detail/', response_class=HTMLResponse)
def detail(request:Request, key: Optional[str] = None):
    if key != None:
        data = car.get(key)
    return templates.TemplateResponse('car-single.html', {'request': request, 'data':data})    


@app.post('/subscribe')
def sub(request:Request, email: Optional[EmailStr] = Form(...)):
    user = ({
            'email':email,
            })
    sub_db.put(user)
    resp = RedirectResponse(url="/",status_code=status.HTTP_302_FOUND)
    return resp

@app.post('/email')
def Contact_form(request:Request, email: EmailStr = Form(...),  firstname: str = Form(...),  lastname: str = Form(...),  message: str = Form(...), subject: str = Form(...)):
    mailjet = Client(auth=('api_key', 'api_secret'), version='v3.1')
    data = {
  'Messages': [
		{
			"From": {
				"Email": "info@shegsamcargo.com",
				"Name": "shegsam cargo"
			},
			"To": [
				{
					"Email": "info@shegsamcargo.com",
				    "Name": "shegsam cargo"
				}
			],
			"TemplateID": 3381773,
			"TemplateLanguage": True,
			"Subject": "Contact Form",
			"Variables": {
        "firstname": firstname ,
        "lastname": lastname ,
        "email": email ,
        "subject": subject,
        "message": message
        }
                }
            ]
        }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
    resp = RedirectResponse(url="/",status_code=status.HTTP_302_FOUND)
    return resp


@app.middleware("http")
async def fix_mime_type(request: Request, call_next):
    response = await call_next(request)
    content_types = {
        ".ttf" :"font/ttf",
        ".woff": "font/woff", 
        ".woff2": "font/woff2"
    }
    for e in content_types:
        if request.url.path.endswith(e): response.headers["Content-Type"] = content_types[e]
    return response

@app.post('/upload_cars/')
def upload_post(request:Request,price : str = Form(...),model: str = Form(...), car_name:str = Form(...), car_description:str = Form(...),car_details:str = Form(...), car_image: UploadFile = File(...) , car_image_1:Optional[UploadFile] = File(None), car_image_2:Optional[UploadFile] = File(None), car_image_3:Optional[UploadFile] = File(None), car_image_4:Optional[UploadFile] = File(None)):
    user = {'car_name':car_name, 'car_description':car_description,'car_details':car_details, 'model':model,'price':price}
    if car_image != None:
        cars = cloudinary.uploader.upload(car_image.file)
        user['image_url'] = cars['url']
    if car_image_1 != None:
        car_1 = cloudinary.uploader.upload(car_image_1.file)
        user['image_url_1'] = car_1['url']
    if car_image_2 != None:
        car_2 = cloudinary.uploader.upload(car_image_2.file)
        user['image_url_2'] = car_2['url']
    if car_image_3 != None:
        car_3 = cloudinary.uploader.upload(car_image_3.file)
        user['image_url_3'] = car_3['url']
    if car_image_4 != None:
        car_4 = cloudinary.uploader.upload(car_image_4.file)
        user['image_url_4'] = car_4['url']
    upload = car.put(user)
    resp = RedirectResponse(url="/admin/dashboard",status_code=status.HTTP_302_FOUND)
    return resp




@app.patch('/upload_cars/{id}')
def upload_post(id:str, car_name:str,car_description:str,car_details:str, car_image: UploadFile = File(...), car_image_1:Optional[UploadFile] = File(None), car_image_2:Optional[UploadFile] = File(None), car_image_3:Optional[UploadFile] = File(None), car_image_4:Optional[UploadFile] = File(None), car_image_5:Optional[UploadFile] = File(None), car_image_6:Optional[UploadFile] = File(None), car_image_7:Optional[UploadFile] = File(None), car_image_8:Optional[UploadFile] = File(None), car_image_9:Optional[UploadFile] = File(None), car_image_10:Optional[UploadFile] = File(None)):
    user = {'car_name':car_name, 'car_description':car_description,'car_details':car_details}
    if car_image != None:
        cars = cloudinary.uploader.upload(car_image.file)
        user['image_url'] = cars['url']
    if car_image_1 != None:
        car_1 = cloudinary.uploader.upload(car_image_1.file)
        user['image_url_1'] = car_1['url']
    if car_image_2 != None:
        car_2 = cloudinary.uploader.upload(car_image_2.file)
        user['image_url_2'] = car_2['url']
    if car_image_3 != None:
        car_3 = cloudinary.uploader.upload(car_image_3.file)
        user['image_url_3'] = car_3['url']
    if car_image_4 != None:
        car_4 = cloudinary.uploader.upload(car_image_4.file)
        user['image_url_4'] = car_4['url']
    if car_image_5 != None:
        car_5 = cloudinary.uploader.upload(car_image_5.file)
        user['image_url_5'] = car_5['url']
    if car_image_6 != None:
        car_6 = cloudinary.uploader.upload(car_image_6.file)
        user['image_url_6'] = car_6['url']
    if car_image_7 != None:
        car_7 = cloudinary.uploader.upload(car_image_7.file)
        user['image_url_7'] = car_7['url']
    if car_image_8 != None:
        car_8 = cloudinary.uploader.upload(car_image_8.file)
        user['image_url_8'] = car_8['url']
    if car_image_9 != None:
        car_9 = cloudinary.uploader.upload(car_image_9.file)
        user['image_url_9'] = car_9['url']
    if car_image_10 != None:
        car_10 = cloudinary.uploader.upload(car_image_10.file)
        user['image_url_10'] = car_10['url']
    
    upload = car.put(user)
    return upload


@app.get('/admin/dashboard', response_class=HTMLResponse)
def index(request:Request):
    items = next(car.fetch())
    return templates.TemplateResponse('admin.html', {'request': request, 'items':items})

@app.post('/admin/delete')
def delete(delete:str = Form(...)):
    car.delete(delete)
    resp = RedirectResponse(url="/admin/dashboard",status_code=status.HTTP_302_FOUND)
    return resp
