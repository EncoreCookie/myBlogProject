# 导入模型以及django自带的User类.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# 创建文章分类表
class Category(models.Model):
# 对应SQL中的varchar类型，长度最多100
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

# 创建文章标签表
class Tag(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

# 创建文章表
class Post(models.Model):
# 文章标题
	title = models.CharField(max_length = 70)
# 文章正文，因为会很长，要对应SQL中的text
	body = models.TextField()
# 文章的创建日期与最后修改的日期，对应SQL中的Date
	create_time = models.DateTimeField()
	modified_time = models.DateTimeField()
# 文章摘要，可以为空
	excerpt = models.CharField(max_length = 200,blank=True)
# 关联文章分类表，一篇文章只能有一个分类，即一对多
	category = models.ForeignKey(Category)
# 关联文章标签表，一篇文章可以有多个标签，即多对多,可以为空
	tags = models.ManyToManyField(Tag,blank=True)
# 用多对多关系关联django中内置的USER模型
	author = models.ForeignKey(User)
# 用于统计阅读量
	views = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})
# 每被调用，自增1
	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])
#定义Post的排列方式，(最新的排在前面),别问这段代码的原理是什么，不解释，这是框架，看原理就去看源码
	class Meta:
		ordering = ['-create_time']