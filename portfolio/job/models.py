from django.db import models

# Create your models here.
# 一般來說一個app一個model，不過他也允許多個
# 他這樣就可以將job這樣的內容存放到database之中，是一種ORM(給你建立schema)
# 而且就算換不同的database system語法也不用改，只用修改setting
class Job(models.Model):
    # Documentation可查: django model field(field type)可以看他欄位的設定的方法
    # upload_to是設置image的位置，他是指在MEDIA folder中的image folder裡面

    image = models.ImageField(upload_to='images/')
    # 設定最大字數，可以確保說畫面顯示區塊，不會有個區塊大小不一的問題，也限制長度節省資源
    summary = models.CharField(max_length=200)