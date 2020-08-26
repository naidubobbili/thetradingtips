from django.db import models
#from datetime import datetime

# Create your models here.


class topic(models.Model):
    Title=models.CharField(default='TheTradingTips',max_length=200)
    Text=models.TextField(default='TheTradingTips')
    #Pic=models.ImageField(default='Cover_Photos/tradingtips.jpg',upload_to='Cover_Photos')
    Pic=models.CharField(default='https://1.bp.blogspot.com/-R4caXMiOVOU/X0WbF5oOnTI/AAAAAAAAAlw/QPyd7ZD7zSMODp5cI5knre1rJamDmwl3wCNcBGAsYHQ/s640/tradingtips.jpg',max_length=250)
    #DetailPagePic=models.ImageField(default='DetailPage.jpg/DetailPagePhotos',upload_to='DetailPagePhotos')
    #uploaded_on=models.TextField(default='TheTradingTips')

    uploaded_on=models.DateTimeField(auto_now_add=True)
    is_uploaded=models.BooleanField(default=True)

    def __str__(self):
        return self.Title
