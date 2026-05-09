"""Create placeholder product images and static fallback if files are missing (e.g. fresh prod volume)."""

from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont

# Matches fixtures/goods/products.json image paths
FIXTURE_IMAGE_NAMES = [
    'goods_images/set_of_tea_table_and_three_chairs.jpg',
    'goods_images/set_of_tea_table_and_two_chairs.jpg',
    'goods_images/double_bed.jpg',
    'goods_images/kitchen_table.jpg',
    'goods_images/kitchen_table_2.jpg',
    'goods_images/corner_sofa.jpg',
    'goods_images/strange_table.jpg',
    'goods_images/sofa.jpg',
    'goods_images/office_chair.jpg',
    'goods_images/plants.jpg',
    'goods_images/flower.jpg',
]


def _save_jpeg_placeholder(path: Path, label: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new('RGB', (800, 600), color=(241, 245, 249))
    draw = ImageDraw.Draw(img)
    draw.rectangle([24, 24, 776, 576], outline=(148, 163, 184), width=3)
    text = label[:80]
    try:
        font = ImageFont.load_default()
    except OSError:
        font = None
    draw.text((48, 48), text, fill=(15, 23, 42), font=font)
    img.save(path, 'JPEG', quality=85)


def _save_png_placeholder(path: Path, label: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new('RGBA', (640, 480), color=(248, 250, 252, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([16, 16, 624, 464], outline=(100, 116, 139), width=2)
    draw.text((32, 32), label, fill=(30, 41, 59))
    img.save(path, 'PNG')


class Command(BaseCommand):
    help = 'Ensure demo media files exist under MEDIA_ROOT and static placeholder image'

    def handle(self, *args, **options):
        media_root = Path(settings.MEDIA_ROOT)
        created = 0

        for rel in FIXTURE_IMAGE_NAMES:
            dest = media_root / rel
            if not dest.exists():
                _save_jpeg_placeholder(dest, rel)
                created += 1

        from goods.models import Product

        for product in Product.objects.exclude(image='').iterator():
            name = product.image.name
            if not name:
                continue
            dest = media_root / name
            if not dest.exists():
                _save_jpeg_placeholder(dest, product.name or name)
                created += 1

        static_img = Path(settings.BASE_DIR) / 'static' / 'deps' / 'images' / 'Not found image.png'
        if not static_img.exists():
            _save_png_placeholder(static_img, 'No image')
            created += 1

        if created:
            self.stdout.write(self.style.SUCCESS(f'seed_demo_media: created {created} placeholder file(s)'))
        else:
            self.stdout.write('seed_demo_media: all media files already present')
