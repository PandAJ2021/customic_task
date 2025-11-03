from django.contrib.staticfiles import finders
from django.core.exceptions import ValidationError


SHIRT_IMAGES = {
    'yellow': 'shirts/yellow.png',
    'white': 'shirts/white.png',
    'blue': 'shirts/blue.png',
    'black': 'shirts/black.png',
}

FONT_PATHS = {
    'courier': 'fonts/COURIERO.TTF',
    'great_vibes': 'fonts/GreatVibes-Regular-webfont.ttf',
    'lobster': 'fonts/Lobster-Regular.ttf',
    'opensans': 'fonts/OpenSans-Regular.ttf',
    'pacifico': 'fonts/Pacifico.ttf',
    'playfair': 'fonts/PlayfairDisplay-Black.ttf',
    'roboto': 'fonts/Roboto-Black.ttf',
    'times': 'fonts/times.ttf',
    'vermin': 'fonts/Vermin_Verile.otf',
}


def get_static_path(file_path: str):
    abs_path = finders.find(file_path)
    if not abs_path:
        raise FileNotFoundError(f"Static file not found: {file_path}")
    return abs_path

def get_shirt_image_path(color_name: str):
    if color_name not in SHIRT_IMAGES:
        raise ValidationError(f"Invalid color '{color_name}'.")

    return get_static_path(SHIRT_IMAGES[color_name])

def get_font_path(font_name: str):
    if font_name not in FONT_PATHS:
        raise ValidationError(f"Invalid font '{font_name}'.")
    
    return get_static_path(FONT_PATHS[font_name])
