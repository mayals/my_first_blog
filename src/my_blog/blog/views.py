from django.shortcuts import render , get_object_or_404
from . import views
from.models import post ,Comment

# posts =[
#    {
#         # item 1
#         'post_subject':'التدوينة الأولى',
#         'post_content':'نص التدوينة الأولى كنص تجريبي',
#         'post_published':'15-8-2019',
#         'post_author':'Ahmad abouissa'
#    },
#    {
#         # item 2
#         'post_subject':'التدوينة الثانية',
#         'post_content':'نص التدوينة الثانية كنص تجريبي',
#         'post_published':'16-8-2019',
#         'post_author':'Saad salim'
#     },
#     {
#         # item 3
#         'post_subject':'التدوينة الثالثة',
#         'post_content':'نص التدوينة الثالثة كنص تجريبي',
#         'post_published':'18-8-2019',
#         'post_author':'Maha nasir',
#     },
#     {
#         # item 4
#         'post_subject':'التدوينة الرابعة',
#         'post_content':'نص التدوينة الرابعة كنص تجريبي',
#         'post_published':'22-8-2019',
#         'post_author':'Sara Ali',
#     },   
# ]


# Create your views here.
def home(request):
    context = {
        'page_title':'الصفحة الرئيسية',
        'posts': post.objects.all() ,  
    }
    return render(request,"blog/index.html", context )



def about(request):

    context = {
        'page_title': 'من أنا' ,
    }
    return render(request ,"blog/about.html",context)


def post_detail(request, post_id):
    thepost = get_object_or_404(post, pk = post_id)
    comments = thepost.comments.filter(active = True)
    context = {
        'page_title': thepost ,
        'item': thepost ,
        'comments':comments ,
    }
    return render(request,'blog/detail.html',context)