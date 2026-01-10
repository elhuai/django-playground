from django.core.exceptions import ValidationError
from pathlib import Path


def validate_image_size(image):
    max_size_mb = 5  # 5MB
    max_size_bytes = max_size_mb * 1024 * 1024  # 轉換為 bytes
    if image.size > max_size_bytes:
        error_message = f"圖片大小不得超過 {max_size_mb}MB"
        raise ValidationError(error_message)


def validate_image_extension(image):
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    ext = Path(image.name).suffix.lower()

    if ext not in valid_extensions:
        error_message = f"不支援的檔案格式。支援的格式: {', '.join(valid_extensions)}"
        raise ValidationError(error_message)


def validate_image_dimensions(image):
    max_width = 4000  # 放寬到 4000px
    max_height = 4000  # 放寬到 4000px

    if image.width > max_width or image.height > max_height:
        error_message = f"圖片尺寸不符合目標尺寸: {max_width}x{max_height}, 目前尺寸: {image.width}x{image.height}"
        raise ValidationError(error_message)
