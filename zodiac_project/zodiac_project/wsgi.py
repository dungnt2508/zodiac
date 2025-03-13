import os
import sys

# Đường dẫn đến thư mục chứa dự án Django của bạn
path = "/home/gsnake1102/zodiac/zodiac_project"  # Thay "/home/gsnake1102/zodiac" bằng đường dẫn thực tế đến thư mục dự án của bạn
if path not in sys.path:
    sys.path.append(path)

# Chỉ định tệp cấu hình settings của Django
os.environ["DJANGO_SETTINGS_MODULE"] = "zodiac.zodiac_project.settings"  # Thay "zodiac.zodiac_project.settings" bằng tên tệp settings của bạn

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
