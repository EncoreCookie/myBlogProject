from ..models import Post,Category
from django import template

register = template.Library()
# 定义最新文章标签
@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-create_time')[:num]
# 定义归档标签，dates函数会返回一个日期集合，参数1是返回创建时间，参数二是精确到月份，参数三是降序排列
@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')
#定义模块标签
@register.simple_tag
def get_categories():
    return Category.objects.all()