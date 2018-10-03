from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
#每一个类都是django.db.models.Model的子类为一个模型   每一个模型代表一张表
#每一个字段都是Field类的一个实例
@python_2_unicode_compatible # 当你想支持python2版本的时候才需要这个装饰器
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):  # 在python2版本中使用的是__unique__
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
#用于保存字符数据的CharField和用于保存时间类型的DateTimeField，它们告诉Django每一个字段保存的数据类型。
@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
