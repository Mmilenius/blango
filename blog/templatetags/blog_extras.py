from django import template
from django.contrib.auth import get_user_model
import logging

register = template.Library()
user_model = get_user_model()
logger = logging.getLogger(__name__)

@register.simple_tag
def row(extra_classes=""):
    """Створює відкриваючий тег рядка"""
    return f'<div class="row {extra_classes}">'

@register.simple_tag
def col():
    """Створює відкриваючий тег колонки"""
    return '<div class="col">'

@register.simple_tag
def endrow():
    """Закриваючий тег для рядка"""
    return '</div>'

@register.simple_tag
def endcol():
    """Закриваючий тег для колонки"""
    return '</div>'

@register.filter(name='add_class')
def add_class(field, css_class):
    """Додає CSS клас до поля форми"""
    return field.as_widget(attrs={"class": css_class})

@register.filter
def author_details(author):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    return name

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    logger.debug("Loaded %d recent posts for post %d", len(posts), post.pk)
    return {"title": "Recent Posts", "posts": posts}