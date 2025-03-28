from django.db import models

class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=20, help_text="Enter phone number with country code")
    email = models.EmailField(help_text="Enter email address")
    address = models.TextField(help_text="Enter complete address")
    is_active = models.BooleanField(default=True, help_text="Set to True to display this contact info")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return f"{self.phone_number} - {self.email}"

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return self.title

class MenuSection(models.Model):
    title = models.CharField(max_length=100)
    menu_item = models.ForeignKey(MenuItem, related_name='sections', on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Menu Section"
        verbose_name_plural = "Menu Sections"

    def __str__(self):
        return f"{self.menu_item.title} - {self.title}"

class MenuLink(models.Model):
    section = models.ForeignKey(MenuSection, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, default='#')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Menu Link"
        verbose_name_plural = "Menu Links"

    def __str__(self):
        return self.title

class Hero(models.Model):
    title = models.CharField(max_length=200, help_text="Main heading for the hero section")
    subtitle = models.TextField(help_text="Subtext below the main heading")
    button_text = models.CharField(max_length=50, default="Shop Now", help_text="Text to display on the button")
    button_link = models.CharField(max_length=200, blank=True, null=True, help_text="URL for the button (optional)")
    is_active = models.BooleanField(default=False, help_text="Only one hero section can be active at a time")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.is_active:
            # Set all other instances to inactive
            Hero.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

    def __str__(self):
        return self.title

class Feature(models.Model):
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class (e.g., fas fa-pills)")
    title = models.CharField(max_length=100, help_text="Feature title")
    description = models.TextField(help_text="Feature description")
    order = models.IntegerField(default=0, help_text="Order of appearance")
    is_active = models.BooleanField(default=True, help_text="Whether to display this feature")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def __str__(self):
        return self.title

class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='advertisements/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisements'

    def __str__(self):
        return self.title

class Advertisement2(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='advertisements2/')
    button_text = models.CharField(max_length=50, default="Shop Now")
    button_link = models.CharField(max_length=200, default="#")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Advertisement 2'
        verbose_name_plural = 'Advertisement 2'

    def __str__(self):
        return self.title

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/')
    website_url = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

