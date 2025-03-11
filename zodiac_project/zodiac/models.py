from django.db import models

class DailyPrediction(models.Model):
    zodiac = models.CharField(max_length=50)  # Tên con giáp
    date = models.DateField()  # Ngày dự đoán
    fortune = models.TextField()  # Nội dung dự đoán
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.zodiac} - {self.date}"