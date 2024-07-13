from .models import Hotel
from modeltranslation.translator import register, TranslationOptions

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('name_hotel', 'description', 'address', 'city', 'country')