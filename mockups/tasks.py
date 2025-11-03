import os
import uuid
from celery import shared_task
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from .models import Result, Mockup
from .utils import get_font_path, get_shirt_image_path


@shared_task
def generate_mockup_images_task(mockup_id):

    mockup = Mockup.objects.get(task_id=mockup_id)
    
    # Convert hex color to RGB tuple
    font_color = tuple(int(mockup.text_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

    font_path = get_font_path(mockup.font)
    text_content = mockup.text

    for color in mockup.shirt_colors:

        image_path = get_shirt_image_path(color)
        image = Image.open(image_path).convert("RGBA")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype(font_path, size=40)

        draw.text((150, 150), text_content, fill=font_color, font=font)

        # Save image
        filename = f"mockup_{color}_{uuid.uuid4().hex}.png"
        output_dir = os.path.join(settings.MEDIA_ROOT, "mockups")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, filename)
        image.save(output_path, "PNG")

        Result.objects.create(
            mockup=mockup,
            image_url=f"mockups/{filename}"
        )
