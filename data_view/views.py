from django.shortcuts import render
import sqlite3
from sqlite3 import Error
# Create your views here.
from django.shortcuts import render
from django.template import loader
import pandas as pd
import json
from sqlalchemy import create_engine
from .models import data_view
from django.db import connection
from django.core import mail
from django.core.mail import send_mail


# Create your views here.

def index(request):
    con = str(data_view.objects.all().query)
    df = pd.read_sql_query(con, connection)
    total_rows = len(df.index)
    bien = total_rows + 1
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    s = df.groupby('ville')['prix_m2_ttc'].mean()
    mean_records = s.reset_index().to_json(orient ='records')
    mean = []
    mean = json.loads(mean_records)
    st = df.groupby('ville')['prix_m2_ttc'].std()
    std_records = st.reset_index().to_json(orient ='records')
    std = []
    std = json.loads(std_records)
    return render(request, 'data/view.html',{'df': data,'bien':bien, 'mean':mean, 'std':std})
def emails(request):
    return render(request, 'data/mail.html')
def sendMail(request):
    subject = request.POST.get('objet')
    body = request.POST.get('msg')
    froms = request.POST.get('emailfrom')
    to = request.POST.get('emailto')
    send_mail(
        subject,
        body,
        froms,
        [to],
        fail_silently=False,
    )
    return render('message envoyé')