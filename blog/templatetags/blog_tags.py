from ..models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count

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
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)