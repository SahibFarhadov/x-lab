from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from slugify import slugify
from django.conf import settings

# Kateqoriyalar ucun kateqoriya modeli
class Kateqoriya(models.Model):
    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'
    kateqoriya_adi = models.CharField('Kateqoriya adı', max_length=150)
    kateqoriya_slug = models.SlugField(editable=False, unique=True)

    def __str__(self):
        return f"{self.kateqoriya_adi}"

    def save(self, *args, **kwargs):
        self.kateqoriya_slug = slugify(self.kateqoriya_adi, replacements = [['Ə','E'],['ə','e']])
        super().save(*args, **kwargs)

# Butun bloglar ucun blog modeli
class Blog(models.Model):
    class Meta:
        verbose_name = 'Məqalə'
        verbose_name_plural = 'Məqalələr'
    basliq_sekli = models.ImageField(upload_to = "uploads/%d.%m.%Y",default = 'uploads/default.jpg',null=True,blank=True)
    basliq = models.CharField('Məqalə başlığı', max_length = 200)
    kontent = CKEditor5Field('Məqalə kontenti', config_name = 'extends')
    yaradilma_tarixi = models.DateTimeField('Yaranma tarixi', auto_now_add = True)
    deyisdirilme_tarixi = models.DateTimeField('Yaranma tarixi', auto_now = True)
    blog_slug = models.SlugField(editable=False, unique = True)
    blog_kateqoriya = models.ManyToManyField(Kateqoriya, verbose_name = 'Kateqoriyaları seçin.')
    yayinda_mi = models.BooleanField('Yayına buraxılsın?', default = False)
    yeni_mi = models.BooleanField('Yeni məqalə?', default = True)
    karuselde = models.BooleanField('Karuseldə', default = False)
    istifadeci = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='İstifadəçi',on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.basliq} meqalesi"

    def save(self, *args, **kwargs):
        self.blog_slug = slugify(self.basliq, replacements = [['Ə','E'],['ə','e']])
        super().save(*args, **kwargs)