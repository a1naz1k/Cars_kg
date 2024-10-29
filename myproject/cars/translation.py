from .models import Cars
from modeltranslation.translator import TranslationOptions,register

@register(Cars)

class CarsTranslationOptions(TranslationOptions):
    fields = ('title', 'cars_name', 'description', 'color',)
