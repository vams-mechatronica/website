from django.shortcuts import render
from .models import Index

# Create your views here.
def home(request):
    return render(request, 'starter-page.html')

def index(request):
    index_items = Index.objects.filter(name__icontains='VAMS').latest('updated_at')
    about_items = Index.objects.filter(name='about_us').latest('updated_at')
    about_bullet_items = Index.objects.filter(name='about_us_bullets')
    service_items = Index.objects.filter(name='services').latest('updated_at')
    promonitor_items = Index.objects.filter(name='index-promonitor').latest('updated_at')
    promonitor_feature_items = Index.objects.filter(name='promonitor-features') 
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
        },"services": {
            "title": service_items.name,
            "description": service_items.description,
        },"promonitor":{
            "title": promonitor_items.name,
            "slogan": promonitor_items.slogan,
            "description": promonitor_items.description,
        },"promonitor_features":[{'description':item.description} for item in promonitor_feature_items],
        "call_to_action": {
            "title": "Call To Action",
            "description": "Duis aute irure dolor in reprehenderit...",
            "link": "#"
        },
        "portfolio": {
            "title": "Portfolio",
            "description": "Necessitatibus eius consequatur...",
            "categories": [
                {"name": "App", "slug": "app"},
                {"name": "Card", "slug": "product"},
                {"name": "Web", "slug": "branding"}
            ],
            "items": [
                {
                    "title": "App 1",
                    "description": "Lorem ipsum dolor sit",
                    "image": "assets/img/portfolio/portfolio-portrait-1.webp",
                    "category": {"slug": "app"},
                    "details_link": "portfolio-details.html"
                },
                # Add more items...
            ]
        },
        "team": {
            "title": "Team",
            "description": "Necessitatibus eius consequatur...",
            "members": [
                {
                    "name": "Walter White",
                    "position": "CEO",
                    "bio": "Explicabo voluptatem...",
                    "image": "assets/img/person/person-m-7.webp",
                    "twitter": "#",
                    "facebook": "#",
                    "instagram": "#",
                    "linkedin": "#"
                },
                # Add more members...
            ]
        },
        "pricing": {
            "title": "Pricing",
            "description": "Necessitatibus eius consequatur...",
            "plans": [
                {
                    "name": "Free Plan",
                    "price": "0",
                    "features": [
                        {"text": "Quam adipiscing vitae proin", "available": True},
                        {"text": "Pharetra massa ultricies", "available": False}
                    ],
                    "link": "#"
                },
                # Add more plans...
            ]
        },'faqs': [
            {'question': 'Non consectetur...', 'answer': 'Feugiat pretium...'},
            # Add more FAQ items here...
        ],
        'recent_posts': [
            {'title': 'Eum ad dolor et...', 'date': 'December 12', 'author': 'Julia Parker', 'category': 'Politics', 'image_url': '/static/img/blog/blog-post-1.webp', 'url': '#'},
            # Add more posts here...
        ],
        'contact': {
            'address': 'A108 Adam Street...',
            'phone': '+1 5589 55488 55',
            'email': 'info@example.com',
            'map_url': 'https://www.google.com/maps/embed?...'
        }
    }
    return render(request, 'index.html',context)