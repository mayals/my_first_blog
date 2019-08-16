from django.shortcuts import render
from . import views

posts =[
   {
        'post_subject':'التدوينة الأولى',
        'post_content':'نص التدوينة الأولى كنص تجريبي',
        'post_published':'15-8-2019',
        'post_author':'Ahmad abouissa'
   },
   {
        'post_subject':'التدوينة الثانية',
        'post_content':'نص التدوينة الثانية كنص تجريبي',
        'post_published':'16-8-2019',
        'post_author':'Saad salim'
    },
    {
        'post_subject':'التدوينة الثالثة',
        'post_content':'نص التدوينة الثالثة كنص تجريبي',
        'post_published':'18-8-2019',
        'post_author':'Maha nasir',
    },
    {
        'post_subject':'التدوينة الرابعة',
        'post_content':'نص التدوينة الرابعة كنص تجريبي',
        'post_published':'22-8-2019',
        'post_author':'Sara Ali',
    },   
]


# Create your views here.
def home(request):
    context = {
    
        'page_title':'الصفحة الرئيسية',
        'posts': posts   
    }
    return render(request,"blog/index.html", context )