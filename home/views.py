from django.shortcuts import render,redirect
from .models import Index, Team,FAQ
from blog.models import Blog

# Create your views here.
def home(request):
    return render(request, 'starter-page.html')

def index(request):
    index_items = Index.objects.filter(name__icontains='VAMS').latest('updated_at')
    about_items = Index.objects.filter(name='about_us').latest('updated_at')
    about_right_items = Index.objects.filter(name='index-about-right').latest('updated_at')
    about_bullet_items = Index.objects.filter(name='about_us_bullets')
    faq_items = FAQ.objects.all()[:5]
    service_items = Index.objects.filter(name='services').latest('updated_at')
    index_promonitor_2 = Index.objects.filter(name='index-promonitor-2').latest('updated_at')
    index_promonitor_3 = Index.objects.filter(name='index-promonitor-3').latest('updated_at')
    promonitor_items = Index.objects.filter(name='index-promonitor').latest('updated_at')
    promonitor_feature_items = Index.objects.filter(name='promonitor-features')
    team_items_member  =  Team.objects.all()
    team_items = Index.objects.filter(name="index-team").latest('updated_at')
    blog_items = Blog.objects.all().order_by('-updated_at')[:3]
    context = {
        "index": {
            "company_name": index_items.name,
            "company_slogan":index_items.slogan,
            "description": index_items.description,
        },
        "about": {
            "title": about_items.name,
            "description": about_items.description,
            "bullets":[{'description':item.description} for item in about_bullet_items]
        },
        "about_right": {"description":about_right_items.description},
        "index_about_2":index_promonitor_2,
        "index_about_3":index_promonitor_3,
        "services": {
            "title": service_items.name,
            "description": service_items.description,
        },"promonitor":{
            "title": promonitor_items.name,
            "slogan": promonitor_items.slogan,
            "description": promonitor_items.description,
        },"promonitor_features":promonitor_feature_items,
        "call_to_action": {
            "title": "Call To Action",
            "description": "Duis aute irure dolor in reprehenderit...",
            "link": "#"
        },
        # "portfolio": {
        #     "title": "Portfolio",
        #     "description": "Necessitatibus eius consequatur...",
        #     "categories": [
        #         {"name": "App", "slug": "app"},
        #         {"name": "Card", "slug": "product"},
        #         {"name": "Web", "slug": "branding"}
        #     ],
        #     "items": [
        #         {
        #             "title": "App 1",
        #             "description": "Lorem ipsum dolor sit",
        #             "image": "assets/img/portfolio/portfolio-portrait-1.webp",
        #             "category": {"slug": "app"},
        #             "details_link": "portfolio-details.html"
        #         },
        #         # Add more items...
        #     ]
        # },
        "team": {
            "title": team_items.slogan,
            "description": team_items.description,
            "members": team_items_member
        },
        "recent_posts":blog_items,
        # "pricing": {
        #     "title": "Pricing",
        #     "description": "Necessitatibus eius consequatur...",
        #     "plans": [
        #         {
        #             "name": "Free Plan",
        #             "price": "0",
        #             "features": [
        #                 {"text": "Quam adipiscing vitae proin", "available": True},
        #                 {"text": "Pharetra massa ultricies", "available": False}
        #             ],
        #             "link": "#"
        #         },
        #         # Add more plans...
        #     ]
        # },
        'faqs': faq_items,
        'contact': {
            'address': 'A108 Adam Street...',
            'phone': '+1 5589 55488 55',
            'email': 'info@example.com',
            'map_url': 'https://www.google.com/maps/embed?...'
        }
    }
    return render(request, 'index.html',context)

def blog_details(request, id):
    blog = Blog.objects.get(pk=id)
    return render(request, '')


