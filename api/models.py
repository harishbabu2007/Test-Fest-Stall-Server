from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import uuid

# Create your models here.
import random

class QrCodes(models.Model):
   stall_name = models.CharField(max_length=500)
   stall_location = models.CharField(max_length=500)
   uuid=models.CharField(max_length=1000)
   image=models.ImageField(upload_to='qrcode',blank=True)

   def save(self,*args,**kwargs):
      self.uuid = str(uuid.uuid4())

      qrcode_img=qrcode.make(self.uuid)
      canvas=Image.new("RGB", (400,400),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'image{random.randint(0,9999)}.png',File(buffer),save=False)
      canvas.close()

      super().save(*args,**kwargs)

   def __str__(self):
    return self.stall_name

class Viewer(models.Model):
  name = models.CharField(max_length=500)
  password = models.CharField(max_length=500)
  coins = models.IntegerField(default=0)

  def __str__(self):
    return self.name

class Viewed_Qr_code(models.Model):
  viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
  qr_code = models.ForeignKey(QrCodes, on_delete=models.CASCADE)

  def __str__(self):
    return self.viewer.name