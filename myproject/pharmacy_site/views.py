from django.shortcuts import render
from .models import ContactInfo, MenuItem, MenuSection, MenuLink, Hero, Feature, Advertisement, Category, Advertisement2, Brand

def index(request):
    # Get active contact info
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    
    # Get active menu items and their related sections and links
    menu_items = MenuItem.objects.filter(is_active=True)
    sections = MenuSection.objects.filter(is_active=True)
    links = MenuLink.objects.filter(is_active=True)
    
    # Get active hero content
    hero = Hero.objects.filter(is_active=True).first()
    
    # Get active features
    features = Feature.objects.filter(is_active=True)
    
    # Get all active advertisements
    side_ads = Advertisement.objects.filter(is_active=True).order_by('order')  # Get all active advertisements ordered by order field
    
    # Get all active advertisements for section 2
    side_ads2 = Advertisement2.objects.filter(is_active=True).order_by('order')
    
    # Get active categories
    categories = Category.objects.filter(is_active=True).order_by('order')
    
    # Get active brands
    brands = Brand.objects.filter(is_active=True).order_by('order')
    
    context = {
        'contact_info': contact_info,
        'menu_items': menu_items,
        'sections': sections,
        'links': links,
        'hero': hero,
        'features': features,
        'side_ads': side_ads,
        'side_ads2': side_ads2,
        'categories': categories,
        'brands': brands,
    }
    
    return render(request, 'pharmacy_site/index.html', context)



